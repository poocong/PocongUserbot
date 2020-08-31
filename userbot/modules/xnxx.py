import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import io
import math
import urllib.request
from os import remove
from PIL import Image
import random
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.events import register
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker


@register(outgoing=True, pattern=r"^\.o(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SaitamaRobot"
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@SaitamaRobot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=701937965))
            await conv.send_message(f'/{wall} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.reply(event.chat_id, response.message)

