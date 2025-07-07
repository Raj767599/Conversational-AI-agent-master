import os
from click import prompt
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from calendar_utils import check_availability_and_book

load_dotenv()  # .env se env vars load karo

# .env file mein likho: GOOGLE_API_KEY=your-gemini-key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(user_input: str) -> str:
    llm_prompt = (
        f"User wants to book a meeting: '{user_input}'. "
        "Extract the meeting date and start/end time in this JSON format ONLY: "
        '{"date": "YYYY-MM-DD", "start_time": "HH:MM", "end_time": "HH:MM"}'
    )
    reply = llm.invoke(llm_prompt)
    if not reply:
        return "Sorry, I couldn't understand your request. Please try again."
    return check_availability_and_book(reply)
