from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# ========================
# توکن بات و آماده‌سازی Dispatcher
TOKEN = "8217430645:AAHXxrDL14VqWD_Kg6WXV2RL8IWvNE6hr-g"
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
# ========================

app = Flask(__name__)

# دستور /start
def start(update, context):
    update.message.reply_text("سلام! بات شما فعال شد.")

# دستور /help
def help_command(update, context):
    update.message.reply_text("دستورات موجود:\n/start\n/help")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

# مسیر webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# صفحه تست سلامت
@app.route("/")
def index():
    return "Bot is running!"

# ========================
# بخش اصلی برای Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
