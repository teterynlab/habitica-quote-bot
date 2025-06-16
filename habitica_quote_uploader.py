import requests
import json
import os
from datetime import date

import requests
import os

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram credentials not set.")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        print("Telegram message sent:", response.status_code)
    except Exception as e:
        print("Failed to send Telegram message:", e)

USER_ID = os.getenv("HABITICA_USER_ID")
API_TOKEN = os.getenv("HABITICA_API_TOKEN")
API_URL = "https://habitica.com/api/v3"

HEADERS = {
    "x-api-user": USER_ID,
    "x-api-key": API_TOKEN,
    "Content-Type": "application/json"
}

with open("quotes.json", encoding="utf-8") as f:
    quotes = json.load(f)

today = date.today().isoformat()
quote = next((q for q in quotes if q["date"] == today), None)

if not quote:
    print("No quote found for today.")
    exit(0)

tasks = requests.get(f"{API_URL}/tasks/user?type=dailys", headers=HEADERS).json()
quote_task = next((t for t in tasks["data"] if t["text"] == "Цитата дня"), None)

if not quote_task:
    resp = requests.post(f"{API_URL}/tasks/user", headers=HEADERS, json={
        "type": "daily",
        "text": "Цитата дня",
        "notes": f'{quote["en"]}\n{quote["ru"]}\nИсточник: {quote["source"]}',
        "frequency": "daily"
    })
    print("Created new task:", resp.json())
send_telegram_message(f"🆕 Создана задача 'Цитата дня': {quote['en']}")
else:
    task_id = quote_task["id"]
    resp = requests.put(f"{API_URL}/tasks/{task_id}", headers=HEADERS, json={
        "notes": f'{quote["en"]}\n{quote["ru"]}\nИсточник: {quote["source"]}'
    })
    print("Updated task:", resp.json())
send_telegram_message(f"✅ Habitica 'Цитата дня' обновлена: {quote['en']}")