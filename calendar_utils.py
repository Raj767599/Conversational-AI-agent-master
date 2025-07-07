from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'service_account.json'
load_dotenv()  # .env se env vars load karo
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
calendar_service = build('calendar', 'v3', credentials=creds)
calendar_id = os.getenv("GOOGLE_CALENDAR_ID") or 'primary'

import json

def check_availability_and_book(parsed_input: str) -> str:
    try:
        data = json.loads(parsed_input)
        date_str = data["date"]        # e.g. "2024-07-09"
        start_time_str = data["start_time"]  # e.g. "15:00"
        end_time_str = data["end_time"]      # e.g. "16:00"
    except Exception as e:
        return "Sorry, I couldn't extract time info. Error: " + str(e)

    # DateTime object banao
    start_time = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")

    event = {
        'summary': 'Appointment with AI Bot',
        'start': {'dateTime': start_time.isoformat() + 'Z'},
        'end': {'dateTime': end_time.isoformat() + 'Z'},
    }

    calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
    return f"Booked from {start_time.strftime('%Y-%m-%d %H:%M')} to {end_time.strftime('%H:%M')} UTC"

