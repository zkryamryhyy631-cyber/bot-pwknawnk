import os, asyncio, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "OK"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    if lang and lang.startswith("ar"):
        await update.message.reply_text("اهلا! البوت شغال ✅")
    else:
        await update.message.reply_text("Hello! Bot is working ✅")

def run_flask():
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def run_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    run_bot()