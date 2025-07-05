from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://files.catbox.moe/h4jbqw.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [⏤͟͟͞͞𓆩 𝐁ᴏᴛ ꭙ 𝐌ᴀᴋᴇʀ𓆪](https://t.me/AboutBotMaker)♨️
  
╚═════ஜ۩۞۩ஜ════╝
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍ᴏᴡɴᴇʀ📍",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "📍ʀᴇᴘᴏ📍",
                        url="https://t.me/AboutBotMaker",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
