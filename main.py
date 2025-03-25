import logging
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetch credentials from environment variables
API_ID = int(os.getenv("API_ID", "23961027"))
API_HASH = os.getenv("API_HASH", "f3add6d66bd20a3ae78e385e81f1df8a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7826130565:AAEwSSOuqvr3_w2RRxt52Tsm2SQ7MDsonHY)

app = Client("heroku_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("NOGHTY AMERICA", url="https://t.me/+70o-6QJJdiRjYWI1")],
        [InlineKeyboardButton("INSTA VIRAL", url="https://t.me/+7lbq-sgx1WAwNzQ9")]
    ])
    message.reply_text(
        "👋 Welcome to the bot!\n\nClick the buttons below to continue:",
        reply_markup=keyboard
    )

@app.on_message(filters.command("help"))
def help_command(client, message):
    message.reply_text("ℹ️ **Help Menu**\n\nUse `/start` to get the link buttons.")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    app.run()
