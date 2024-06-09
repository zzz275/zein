import asyncio

from pyrogram import filters
from pyrogram.enums import ParseMode

from zein import app
from zein.misc import SUDOERS
from zein.utils.database import get_assistant
from zein.utils.vip_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(
        ["atag", "aall", "تاك بالمساعد", "amentionall"], prefixes=["/", "@", ""]
    )
    & SUDOERS
)
async def tag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "الـتاك شـغال اصـلا يـسطا..،..  🚶‍♂️🤸‍♂️"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** اكـتب الامـر بـعده اي رسـاله يـقلبي..،..  👀🩷"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += (
                f"\n⊚ [{m.user.first_name}](tg://openmessage?user_id={m.user.id})\n"
            )
            if usernum == 5:
                await replied.reply_text(usertxt, ParseMode.MARKDOWN)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f'\n⊚ <a href="tg://openmessage?user_id={m.user.id}">{m.user.first_name}</a>\n'

            if usernum == 5:
                await userbot.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /acancel ||",
                    ParseMode.HTML,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        [
            "astopmention",
            "بس تاك المساعد",
            "ايقاف تاك المساعد",
            "aallstop",
            "astopall",
            "acancelmention",
            "aoffmention",
            "amentionoff",
            "aalloff",
            "acancelall",
            "aallcancel",
        ],
        prefixes=["/", "@", ""],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**الـتاك وقـف.،. 🤔**")

    else:
        await message.reply_text("**الـتاك واقـف.،. 🤔**")
        return
