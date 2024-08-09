import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class Krish(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="RadhaMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            parse_mode=ParseMode.HTML,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\n<b>ɪᴅ :</b> <code>{self.id}</code>\n<b>ɴᴀᴍᴇ :</b> {self.name}\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{self.username}",
            )
            await self.set_bot_commands(
                [
                    BotCommand("start", "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
                    BotCommand("help", "ᴏᴘᴇɴ ᴛʜᴇ ʙᴏᴛ ʜᴇʟᴘ ᴍᴇɴᴜ"),
                    BotCommand("ping", "ᴄʜᴇᴄᴋ ᴛʜᴀᴛ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ"),
                    BotCommand("auth", "ᴀᴅᴅ ᴀ ᴜꜱᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪꜱᴛ ᴏꜰ ᴛʜᴇ ɢʀᴏᴜᴘ"),
                    BotCommand("unauth", "ʀᴇᴍᴏᴠᴇ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴀᴜᴛʜ ʟɪꜱᴛ ᴏꜰ ᴛʜᴇ ɢʀᴏᴜᴘ"),
                    BotCommand("reboot", "ʀᴇꜱᴛᴀʀᴛꜱ ᴛʜᴀ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ"),
                    BotCommand("stats", "ꜱʜᴏᴡꜱ ᴛʜᴇ ꜱᴛᴀᴛꜱ ᴏꜰ ᴛʜᴇ ʙᴏᴛ"),
                    BotCommand("play", "ꜱᴛᴀʀᴛꜱ ᴘʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛᴇᴅ ꜱᴏɴɢ"),
                    BotCommand("vplay", "ꜱᴛᴀʀᴛꜱ ᴘʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛᴇᴅ ꜱᴏɴɢ ᴀꜱ ᴠɪᴅᴇᴏ"),
                    BotCommand("skip", "ᴍᴏᴠᴇꜱ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ"),
                    BotCommand("pause", "ᴘᴀᴜꜱᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ ꜱᴏɴɢ"),
                    BotCommand("resume", "ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜꜱᴇᴅ ꜱᴏɴɢ"),
                    BotCommand("end", "ᴄʟᴇᴀʀ ᴛʜᴇ Qᴜᴇᴜᴇ ᴀɴᴅ ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ"),
                    BotCommand("lyrics", "ꜱᴇᴀʀᴄʜᴇꜱ ʟʏʀɪᴄꜱ ᴏꜰ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ꜱᴏɴɢ"),
                    BotCommand("song", "ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ"),
                    BotCommand("loop", "ʟᴏᴏᴘꜱ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ꜱᴏɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ"),
                    BotCommand("shuffle", "ʀᴀɴᴅᴏᴍʟʏ ꜱʜᴜꜰꜰʟᴇ ᴛʜᴇ Qᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪꜱᴛ."),
                    BotCommand(
                        "seek", "ꜱᴇᴇᴋ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ ᴛᴏ ɢɪᴠᴇɴ ᴅᴜʀᴀᴛɪᴏɴ (ɪɴ ꜱᴇᴄᴏɴᴅꜱ)"
                    ),
                    BotCommand(
                        "seekback",
                        "ꜱᴇᴇᴋ ʙᴀᴄᴋ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ ᴛᴏ ɢɪᴠᴇɴ ᴅᴜʀᴀᴛɪᴏɴ (ɪɴ ꜱᴇᴄᴏɴᴅꜱ)",
                    ),
                ]
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
