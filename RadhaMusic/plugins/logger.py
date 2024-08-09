from pyrogram import filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from RadhaMusic import app
from RadhaMusic.core.userbot import assistants
from RadhaMusic.misc import SUDOERS
from RadhaMusic.utils.database import add_off, add_on, get_client
from RadhaMusic.utils.decorators.language import language


@app.on_message(filters.command(["logger"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)


@app.on_message(filters.new_chat_members)
async def new(_, message: Message):
    if app.id in [user.id for user in message.new_chat_members]:
        add = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        new = f"<b>✫ <u>ɴᴇᴡ ɢʀᴏᴜᴘ</u> :</b>\n\n<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n<b>ᴄʜᴀᴛ ᴛɪᴛʟᴇ :</b> {message.chat.title}\n\n<b>ᴀᴅᴅᴇᴅ ʙʏ :</b> {add} | <code>{message.from_user.id}</code>"
        await app.send_message(LOG_GROUP_ID, new)


@app.on_message(filters.left_chat_member)
async def left(_, message: Message):
    if app.id == message.left_chat_member.id:
        remove = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        left = f"<b>✫ <u>ʟᴇғᴛ ɢʀᴏᴜᴘ</u> :</b>\n\n<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n<b>ᴄʜᴀᴛ ᴛɪᴛʟᴇ :</b> {message.chat.title}\n\n<b>ʀᴇᴍᴏᴠᴇᴅ ʙʏ :</b> {remove} | <code>{message.from_user.id}</code>"
        await app.send_message(LOG_GROUP_ID, left)
        for num in assistants:
            hm = await get_client(num)
            try:
                await hm.leave_chat(message.chat.id)
            except:
                pass
