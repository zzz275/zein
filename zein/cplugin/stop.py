from pyrogram import Client, filters
from pyrogram.types import Message

from config import BANNED_USERS
from zein.core.call import VIP
from zein.utils.database import set_loop
from zein.utils.decorators import AdminRightsCheck
from zein.utils.inline import close_markup


@Client.on_message(
    filters.command(
        ["end", "stop", "cend", "cstop"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await VIP.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
