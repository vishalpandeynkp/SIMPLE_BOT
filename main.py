import logging
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, get_total_users

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetch credentials from environment variables
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  # Bot Owner's Telegram ID

app = Client("stats_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    add_user(user_id)  # Store user in database

    # Send private log to owner
    log_message = f"🆕 **New User Started the Bot**\n\n👤 Name: {first_name}\n🆔 User ID: `{user_id}`"
    if username:
        log_message += f"\n📛 Username: @{username}"
    client.send_message(OWNER_ID, log_message)

    # Send start message to user
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("SEX HUB", url="https://t.me/+70o-6QJJdiRjYWI1")],
        [InlineKeyboardButton("INSTA VIRAL", url="https://t.me/+7lbq-sgx1WAwNzQ9")],
        [InlineKeyboardButton("PAID DALAL", url=f"https://t.me/DADA_PROMO")]
    ])
    message.reply_text(
        "👋 Welcome to the bot!\n\nClick the buttons below to continue:",
        reply_markup=keyboard
    )

@app.on_message(filters.command("stats"))
def stats_command(client, message):
    total_users = get_total_users()
    message.reply_text(f"📊 **Bot Stats**\n\n👥 Total Users: `{total_users}`")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    app.run()
