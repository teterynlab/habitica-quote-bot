import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from habitica import send_daily_quote, get_random_quote
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот с цитатами из фантастики. Напиши /quote для новой цитаты.")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, source = get_random_quote()
    await update.message.reply_text(f"🧠 *{text}*\n\n📚 _{source}_", parse_mode="Markdown")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши /quote для новой цитаты.")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    logger.info("Бот запущен.")
    app.run_polling()

def run_cron():
    send_daily_quote()

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "bot"
    if mode == "cron":
        run_cron()
    else:
        run_bot()