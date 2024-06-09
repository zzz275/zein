from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from zein import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from zein.core.call import VIP
from zein.utils.database import is_music_playing, music_off
from zein.utils.decorators import AdminRightsCheck
from zein.utils.inline import close_markup


@app.on_message(command(["مؤقتا", "cpause"]))
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await VIP.pause_stream(chat_id)
    
    buttons = [
        [
            InlineKeyboardButton(
                text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
    ]

    await message.reply_text(
        _["admin_2"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
