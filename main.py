import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

# TOKEN — Render'dagi Environment Variables bo‘limida 'BOT_TOKEN' deb nomlangan o‘zgaruvchidan olinadi
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🚀 /start buyrug'i keldi")
    await update.message.reply_text("Salom! Men AI-Ustoz botman. /help buyrug‘ini bosing.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"📩 Xabar keldi: {update.message.text}")
    await update.message.reply_text(f"Siz yozdingiz: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("✅ Bot ishga tushyapti...")
    app.run_polling()

if __name__ == "__main__":
    main()

