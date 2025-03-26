import asyncio
import os
from pyrogram import Client, filters
from pymongo import MongoClient

# MongoDB से यूज़र्स लोड करने के लिए सेटअप
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://vishalpandeynkp:Bal6Y6FZeQeoAoqV@cluster0.dzgwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_URL)
db = client["TelegramBot"]
users_collection = db["Users"]

# बॉट और एडमिन ID सेट करें
OWNER_ID = int(os.getenv("6972508083"))  # अपना टेलीग्राम ID डालो

# Pyrogram Client (Main Bot)
app = Client("broadcast_bot")

# सभी यूज़र्स लोड करने वाला फंक्शन
def load_users():
    return [user["user_id"] for user in users_collection.find()]

# ब्रॉडकास्ट कमांड
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    users = load_users()
    text = message.text.split(maxsplit=1)

    if len(text) < 2:
        await message.reply_text("❌ **Usage:** `/broadcast Your message here`")
        return

    msg_to_send = text[1]
    success = 0
    failed = 0

    for user_id in users:
        try:
            await client.send_message(int(user_id), msg_to_send)
            success += 1
            await asyncio.sleep(0.5)  # स्पैम अवॉइड करने के लिए थोड़ा इंतजार
        except Exception:
            failed += 1

    await message.reply_text(f"✅ **Broadcast Done!**\n\n✅ **Success:** {success}\n❌ **Failed:** {failed}")

# बॉट को रन करने के लिए
if __name__ == "__main__":
    app.run()
