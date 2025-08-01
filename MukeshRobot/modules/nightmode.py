from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon import functions, types
from telethon.tl.types import ChatBannedRights
from MukeshRobot import BOT_NAME
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register
from MukeshRobot.modules.sql.night_mode_sql import (
    add_nightmode,
    get_all_chat_id,
    is_nightmode_indb,
    rmnightmode,
)


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    elif isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    else:
        return None


hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=False,
    pin_messages=False,
    change_info=False,
)


@register(pattern="^/nightmode")
async def close_ws(event):
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply("🤦🏻‍♂️You are not admin so you can't use this command...")
            return

    if not event.is_group:
        await event.reply("You Can Only Enable Night Mode in Groups.")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.reply("This Chat is Has Already Enabled Night Mode.")
        return
    add_nightmode(str(event.chat_id))
    await event.reply(
        f"Added Chat {event.chat.title} With Id {event.chat_id} To Database. **This Group Will Be Closed On 12Am(IST) And Will Opened On 06Am(IST)**"
    )


@register(pattern="^/rmnight")
async def disable_ws(event):
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply("🤦🏻‍♂️You are not admin so you can't use this command...")
            return

    if not event.is_group:
        await event.reply("You Can Only Disable Night Mode in Groups.")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.reply("This Chat is Has Not Enabled Night Mode.")
        return
    rmnightmode(str(event.chat_id))
    await event.reply(
        f"Removed Chat {event.chat.title} With Id {event.chat_id} From Database."
    )


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
                int(warner.chat_id),
                f"12:00 Am, Group Is Closing Till 6 Am. Night Mode Started ! \n**Powered By {BOT_NAME}**",
            )
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=hehes
                )
            )
        except Exception as e:
            logger.info(f"Unable To Close Group {warner} - {e}")


# Run everyday at 12am
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=59)
scheduler.start()


async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
                int(warner.chat_id),
                f"06:00 Am, Group Is Opening.\n**Powered By {BOT_NAME}**",
            )
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=openhehe
                )
            )
        except Exception as e:
            logger.info(f"Unable To Open Group {warner.chat_id} - {e}")


# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open, trigger="cron", hour=6, minute=1)
scheduler.start()

__help__ = """
*ᴀᴅᴍɪɴs ᴏɴʟʏ*

 ❍ /nightmode *:* ᴀᴅᴅs ɢʀᴏᴜᴘ ᴛᴏ ɴɪɢʜᴛᴍᴏᴅᴇ ᴄʜᴀᴛs
 ❍ /rmnight *:* ʀᴇᴍᴏᴠᴇs ɢʀᴏᴜᴘ ғʀᴏᴍ ɴɪɢʜᴛᴍᴏᴅᴇ ᴄʜᴀᴛs

*ɴᴏᴛᴇ:* ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴄʜᴀᴛs ɢᴇᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴏsᴇᴅ ᴀᴛ 12 ᴀᴍ(ɪsᴛ) ᴀɴᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴏᴘᴇɴɴᴇᴅ ᴀᴛ 6 ᴀᴍ(ɪsᴛ) ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ɴɪɢʜᴛ sᴘᴀᴍs.

☆............𝙱𝚈 » [⏤͟͟͞͞𓆩 𝐁ᴏᴛ ꭙ 𝐌ᴀᴋᴇʀ𓆪](https://t.me/AboutBotMaker)............☆
"""

__mod_name__ = "⚡Nɪɢʜᴛ⚡"
