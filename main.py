from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

# loading .env
load_dotenv()

app = FastAPI(title="Class 1-12 Student Tutor Chatbot")

# constants
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "deepseek/deepseek-r1-distill-llama-70b:free"
SYSTEM_PROMPT = "You are a helpful, accurate educator tutor."

sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str

# implementation of chatbot and used HTTPException to show http codes
@app.post("/chat", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    session_id = chat_request.session_id.strip()
    user_message = chat_request.message.strip()

    if not OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="Missing API key.")

    if not session_id or not user_message:
        raise HTTPException(status_code=400, detail="Session_ID and message required.")

    if session_id not in sessions:
        sessions[session_id] = [{"role": "system", "content": SYSTEM_PROMPT}]

    sessions[session_id].append({"role": "user", "content": user_message})

    payload = {
        "model": MODEL_NAME,
        "messages": sessions[session_id],
        "stream": False
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers
        )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=response.text)

    bot_reply = response.json()["choices"][0]["message"]["content"]
    sessions[session_id].append({"role": "bot", "content": bot_reply})

    return ChatResponse(reply=bot_reply)