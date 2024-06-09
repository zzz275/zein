import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import AUTO_GCAST, AUTO_GCAST_MSG
from zein import app
from zein.utils.database import get_served_chats_clone

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://graph.org/file/760169f7f8dd536c50793.jpg"

MESSAGES = f"""**🌹𝗟𝗼𝗼𝗸𝗶𝗻𝗴 𝗙𝗼𝗿 𝗔𝗴𝗲𝗻𝘁 𝗪𝗼𝗿𝗸 𝗜𝗻 𝗡𝗲𝘄 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺 𝗝𝘂𝘀𝘁 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗠𝗲 𝗪𝗵𝗼 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗪𝗼𝗿𝗸 𝗔𝘀 𝗔 𝗔𝗴𝗲𝗻𝘁.

𝗠𝘀𝗴 𝗛𝗲𝗿𝗲 :- @OkWinAgent

𝗦𝗮𝗹𝗹𝗲𝗿𝘆 𝗦𝘁𝗮𝗿𝘁𝘀 𝘄𝗶𝘁𝗵 𝟮 𝗔𝗰𝘁𝗶𝘃𝗲 𝗣𝗹𝗮𝘆𝗲𝗿.

🎁𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿 𝗹𝗶𝗻𝗸 :- https://okwin.one/#/register?invitationCode=8284112316

➻ 𝗟𝗼𝘀𝘀 𝗥𝗲𝗳𝘂𝗻𝗱 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 ✅
➥ 𝗣𝗿𝗲𝗱𝗶𝗰𝘁𝗶𝗼𝗻 » @OK_WIN_PREDICTIONS**"""
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ Click & Get ₹100 ๏",
                url=f"https://okwin.one/#/register?invitationCode=8284112316",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/TG_VC_BOT?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_message_to_chats(client: Client, message: Message):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(20)
                except Exception as e:
                    pass
    except Exception as e:
        pass


async def continuous():
    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass
        await asyncio.sleep(100000)


if AUTO_GCASTS:
    asyncio.create_task(continuous())
