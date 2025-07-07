# Conversational Calendar Booking Bot 🗓️💬

This app lets users chat to book Google Calendar appointments using a natural conversation.

## 🧠 Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI + Langchain
- **LLM**: OpenAI or Gemini (via API key)
- **Calendar**: Google Calendar (via Service Account)

## ⚙️ Setup

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Add your `.env` file with:
```
OPENAI_API_KEY=your-api-key
GOOGLE_CALENDAR_ID=your-calendar-id
```

3. Place your Google `service_account.json` in the project root.

4. Run backend:
```bash
uvicorn main:app --reload
```

5. Run Streamlit UI:
```bash
streamlit run streamlit_app.py
```

## 🚀 Deployment
Deploy on Railway, Render, or Fly.io. Ensure environment variables and `service_account.json` are securely added.

## 📌 Note
Use a test calendar and service account with editor access.
