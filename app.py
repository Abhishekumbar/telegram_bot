import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
QWEN_API_KEY = os.getenv("QWEN_API_KEY")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    response = requests.post(
        "https://api.qwen.ai/chat",
        headers={"Authorization": f"Bearer {QWEN_API_KEY}"},
        json={"message": user_msg}
    )

    try:
        reply = response.json().get("response", "No response")
    except:
        reply = "Error"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
