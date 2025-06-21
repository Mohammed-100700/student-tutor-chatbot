# Class 1–12 Student Tutor Chatbot

An educational chatbot built with FastAPI and OpenRouter’s free large language models. It serves as a virtual tutor for students from Class 1 to Class 12, answering academic questions using markdown-formatted responses. The application supports session-based memory (in-memory only) and is deployed on Render.

---

## Render Deployment

- [https://student-tutor-chatbot.onrender.com/docs](https://student-tutor-chatbot.onrender.com/docs)

---

## API Usage Instructions

### Click the endpoint in the Swagger UI

```http
POST /chat
```

### Example Request Body (copy and paste it)

```json
{
  "session_id": "test001",
  "message": "Explain the difference between speed and velocity for class 9."
}
```

### Response Body (reply from the bot)

```json
{
  "reply": "**Understanding Speed and Velocity: A Clear Explanation for Class 9 Students**\n\n1. **Introduction:**\n   - Both speed and velocity relate to motion but have distinct differences.\n\n2. **Key Concepts:**\n   - **Speed:** A scalar quantity that measures how fast an object is moving. It does not include direction.\n   - **Velocity:** A vector quantity that includes both speed and direction, describing how fast an object moves in a specific direction.\n\n3. **Formulas:**\n   - Speed = Distance / Time (\\( \\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}} \\))\n   - Velocity = Displacement / Time (\\( \\text{Velocity} = \\frac{\\text{Displacement}}{\\text{Time}} \\))\n\n4. **Examples:**\n   - **Speed:** If a car travels at 60 km/h, its speed is 60 km/h.\n   - **Velocity:** If the car is moving north at 60 km/h, its velocity is 60 km/h north.\n\n5. **Displacement vs. Distance:**\n   - **Distance:** Total path traveled.\n   - **Displacement:** Straight-line distance from start to end point.\n   - **Example:** Traveling in a circle: displacement is zero (if returning to the start), but distance is the circumference.\n\n6. **Common Misconceptions:**\n   - While speed and velocity both measure motion, velocity includes direction, making it a vector.\n\n7. **Advanced Note:**\n   - In circular motion, speed remains constant, but velocity changes due to direction changes.\n\nThis structured approach clarifies the differences using relatable examples and formulas, helping students grasp the concepts effectively."
}
```
---

## Environment Variable Setup

To use the OpenRouter API, set your API key in a `.env` file:

### `.env`

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
---

## Local Setup Guide

Follow the steps below to run the chatbot locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Mohammed-100700/student-tutor-chatbot.git
cd student-tutor-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Environment Variable

Create a `.env` file with your API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 6. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 7. Test via Swagger UI

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

Use the `/chat` endpoint to start a tutoring conversation.

---

## Screenshot

![image](https://github.com/user-attachments/assets/cef66274-065f-44ae-ae3f-ca91bda085a3)
![image](https://github.com/user-attachments/assets/d1d9e0ad-e6d3-4b89-83a1-a25afa83019d)



---
