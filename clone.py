from pyrogram import Client, filters

YOUR_ADMIN_ID = 123456789  # अपना टेलीग्राम ID डालो
YOUR_TARGET_CHAT_ID = -1001234567890  # जिस ग्रुप/चैट में मैसेज भेजना है उसकी ID

@Client.on_message(filters.user(YOUR_ADMIN_ID) & filters.command("clone"))
async def clone_message(client, message):
    if not message.reply_to_message:
        await message.reply_text("Reply to a message to clone it.")
        return

    msg = message.reply_to_message

    if msg.text:
        await client.send_message(YOUR_TARGET_CHAT_ID, msg.text)
    elif msg.photo:
        await client.send_photo(YOUR_TARGET_CHAT_ID, msg.photo.file_id, caption=msg.caption)
    elif msg.video:
        await client.send_video(YOUR_TARGET_CHAT_ID, msg.video.file_id, caption=msg.caption)
    elif msg.audio:
        await client.send_audio(YOUR_TARGET_CHAT_ID, msg.audio.file_id, caption=msg.caption)
    elif msg.document:
        await client.send_document(YOUR_TARGET_CHAT_ID, msg.document.file_id, caption=msg.caption)
    else:
        await message.reply_text("Unsupported message type.")

    await message.reply_text("✅ Message cloned successfully!")
