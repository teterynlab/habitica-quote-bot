#!/usr/bin/env python3

import os
import requests
import json
from datetime import date

def send_telegram(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("⚠️ Telegram config missing.")
        return
    try:
        resp = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        })
        print("Telegram status:", resp.status_code)
    except Exception as e:
        print("Telegram send error:", str(e))

try:
    with open("quotes.json", encoding="utf-8") as f:
        quotes = json.load(f)

    today = date.today().isoformat()
    quote = next((q for q in quotes if q["date"] == today), None)

    if not quote:
        raise Exception("❌ No quote found for today.")

    user_id = os.getenv("HABITICA_USER_ID")
    api_token = os.getenv("HABITICA_API_TOKEN")
    headers = {
        "x-api-user": user_id,
        "x-api-key": api_token,
        "Content-Type": "application/json"
    }

    api_url = "https://habitica.com/api/v3"
    tasks = requests.get(f"{api_url}/tasks/user?type=dailys", headers=headers).json()
    quote_task = next((t for t in tasks["data"] if t["text"] == "Цитата дня"), None)

    note = f'{quote["en"]}\n{quote["ru"]}\nИсточник: {quote["source"]}'

    if not quote_task:
        resp = requests.post(f"{api_url}/tasks/user", headers=headers, json={
            "type": "daily",
            "text": "Цитата дня",
            "notes": note,
            "frequency": "daily"
        })
        send_telegram(f"🆕 Создана задача 'Цитата дня': *{quote['en']}*")
    else:
        task_id = quote_task["id"]
        resp = requests.put(f"{api_url}/tasks/{task_id}", headers=headers, json={
            "notes": note
        })
        send_telegram(f"✅ Обновлена 'Цитата дня': *{quote['en']}*")

except Exception as e:
    error_message = f"❌ Ошибка при обновлении Habitica: `{str(e)}`"
    send_telegram(error_message)
    print(error_message)