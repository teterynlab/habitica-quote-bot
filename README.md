# 🛰️ Habitica Quote Bot

An automated bot that updates the *"Quote of the Day"* task in [Habitica](https://habitica.com) every morning using a predefined list of quotes — and sends notifications to a Telegram group about success or failure.

---

## ⚙️ Features

- ⏰ Runs automatically every day at **07:00 UTC** using `cron` inside a Docker container
- 🧠 Posts daily quotes (English + Russian) to your Habitica task
- 📤 Sends a Telegram message on success or error
- 🐳 Fully containerized with GitHub Actions deployment to Azure Container Registry & Web App

---

## 🧱 Structure

- `main.py` — the main bot script
- `quotes.json` — a 180-day list of motivational quotes with metadata
- `Dockerfile` — based on `python:3.11-slim`, with built-in `cron`
- `README.md` — you're reading it

---

## 🔐 Required Environment Variables

| Variable               | Description                                  |
|------------------------|----------------------------------------------|
| `HABITICA_USER_ID`     | Your Habitica user ID                        |
| `HABITICA_API_TOKEN`   | API token to authenticate with Habitica      |
| `TELEGRAM_BOT_TOKEN`   | Bot token for Telegram notifications         |
| `TELEGRAM_CHAT_ID`     | Telegram chat ID to receive messages         |
| `ENV`                  | Optional: environment name (e.g. `production`) |
| `TZ`                   | Optional: timezone, e.g. `Europe/Tbilisi`    |

---

## 🚀 How It Works

1. The container runs `cron` on startup
2. Every day at 07:00 UTC:
   - The bot looks up today's quote in `quotes.json`
   - Updates or creates the `Quote of the Day` task in your Habitica account
   - Sends a success message (including the quote) to Telegram
3. If any error occurs, it sends an error message to Telegram instead

---

## 🔄 CI/CD Pipeline

The bot is built and deployed using GitHub Actions