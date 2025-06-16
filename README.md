# 🧠 Habitica Quote Uploader · Daily Motivational Habit Tracker

Automatically uploads a **daily motivational quote** to your Habitica account as a **Daily Task**, with optional **Telegram notifications**.  
Perfect for keeping yourself inspired and consistent — like a sci-fi pilot running daily routines in space ✨

---

## 🚀 Features

- ⏱ 180+ motivational quotes from **sci-fi books, games and films**
- 🔁 Automatically updates your **"Daily Quote"** task every day
- ⚙️ Works with **Habitica API**
- ☁️ Deployable via **GitHub Actions** or **Docker**
- 📲 Sends **Telegram notifications** when update is successful

---

## 📷 Screenshot

> _“Empires fall. Will endures.”_  
> — *EVE Online RP*

Habitica Daily task updated:

```
🗓 Цитата дня  
✅ Empires fall. Will endures.  
🔁 Империи рушатся. Воля — вечна.  
📚 Источник: EVE Online (RP)
```

---

## 🛠 Setup Instructions

### 🔐 1. Get Your Habitica API Credentials

From https://habitica.com/user/settings/api  
- Copy your `User ID`
- Copy your `API Token`

---

### 📥 2. Clone or Download This Repo

```bash
git clone https://github.com/yourusername/habitica-quote-uploader.git
cd habitica-quote-uploader
```

---

### 🐳 3. Run with Docker (Manual)

```bash
docker build -t habitica-quotes .
docker run --rm habitica-quotes
```

---

### ☁️ 4. Automate with GitHub Actions

1. Add the following secrets to your repo:
   - `HABITICA_USER_ID`
   - `HABITICA_API_TOKEN`
   - `TELEGRAM_BOT_TOKEN` *(optional)*
   - `TELEGRAM_CHAT_ID` *(optional)*

2. Workflow auto-runs daily via `.github/workflows/daily-quote.yml`

---

## 🧾 Environment Variables

| Name                  | Required | Description                            |
|-----------------------|----------|----------------------------------------|
| `HABITICA_USER_ID`    | ✅       | Your Habitica user ID                  |
| `HABITICA_API_TOKEN`  | ✅       | Your Habitica API token                |
| `TELEGRAM_BOT_TOKEN`  | ⬛       | Token from @BotFather (optional)       |
| `TELEGRAM_CHAT_ID`    | ⬛       | Your chat ID or group ID (optional)    |

---

## 📚 Quote Sources

- *Frank Herbert – Dune*
- *Isaac Asimov – Foundation*
- *Ursula K. Le Guin – Earthsea*
- *Mass Effect*, *Dark Souls*, *The Witcher*, *EVE Online*, *Interstellar* and more.

Quotes are in both English and Russian and rotate daily over 6 months.

---

## 🤖 Telegram Notifications (Optional)

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Get your `chat_id` via [@userinfobot](https://t.me/userinfobot)
3. Add both values as secrets in GitHub

---

## 📈 SEO Tags

> `Habitica API`, `habit tracker automation`, `GitHub Actions Habitica`, `daily quote bot`, `sci-fi motivation`, `self-discipline assistant`, `Docker habitica`, `habitica telegram bot`

---

## 💡 License

MIT — use freely, star if useful ⭐  
