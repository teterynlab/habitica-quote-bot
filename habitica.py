import json
import random
import requests
import os

def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_random_quote():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return quote["quote"], quote["source"]

def send_daily_quote():
    quote, source = get_random_quote()
    telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if telegram_token and chat_id:
        requests.post(
            f"https://api.telegram.org/bot{telegram_token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"🧠 *{quote}*\n\n📚 _{source}_",
                "parse_mode": "Markdown"
            }
        )