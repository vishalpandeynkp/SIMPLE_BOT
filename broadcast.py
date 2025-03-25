from pyrogram import Client, filters
from users import load_users
import asyncio

YOUR_ADMIN_ID = 7439669272  # अपना टेलीग्राम ID डालो

@Client.on_message(filters.user(YOUR_ADMIN_ID) & filters.command("broadcast"))
async def broadcast(client, message):
    users = load_users()
    text = message.text.split(maxsplit=1)

    if len(text) < 2:
        await message.reply_text("Usage: `/broadcast Your message here`")
        return

    msg_to_send = text[1]
    success = 0
    failed = 0

    for user_id in users.keys():
        try:
            await client.send_message(int(user_id), msg_to_send)
            success += 1
            await asyncio.sleep(0.5)  # स्पैम अवॉइड करने के लिए
        except Exception:
            failed += 1

    await message.reply_text(f"✅ Broadcast Done!\n\n✅ Success: {success}\n❌ Failed: {failed}")
