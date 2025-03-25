import logging
import os
import requests
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
        "👋 Welcome to the bot!/n/ Bot clone ke liye ye command use kare /clone\n\nClick the buttons below to continue:",
        reply_markup=keyboard
    )

@app.on_message(filters.command("stats"))
def stats_command(client, message):
    total_users = get_total_users()
    message.reply_text(f"📊 **Bot Stats**\n\n👥 Total Users: `{total_users}`")

@app.on_message(filters.command("clone") & filters.user(OWNER_ID))
def clone_bot(client, message):
    if len(message.command) < 2:
        message.reply_text("❌ Usage: `/clone <bot_token>`")
        return

    bot_token = message.command[1]

    # Get bot info from Telegram API
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe").json()
    if not response.get("ok"):
        message.reply_text("❌ Invalid Bot Token!")
        return
    
    bot_username = response["result"]["username"]
    
    clone_code = f"""
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "{bot_token}"

app = Client("clone_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("SEX HUB", url="https://t.me/+70o-6QJJdiRjYWI1")],
        [InlineKeyboardButton("INSTA VIRAL", url="https://t.me/+7lbq-sgx1WAwNzQ9")],
    ])
    message.reply_text(
        "👋 Welcome to the cloned bot  /clone !\n\nClick the buttons below to continue:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    app.run()
    """

    with open(f"{bot_username}_clone.py", "w") as file:
        file.write(clone_code)

    message.reply_text(f"✅ Clone script generated for @{bot_username}! Check `{bot_username}_clone.py`.")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    app.run()
