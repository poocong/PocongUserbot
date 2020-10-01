import os
from telethon import events, functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot.utils import defender_kanger
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot
import io
import os
import random
import re
import textwrap
from random import randint, uniform
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from telethon.tl.types import DocumentAttributeFilename


@register(outgoing=True, pattern=r"^\.o(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@xbotgroup_xbot"
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@xbotgroup_xbot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1281618755))
            await conv.send_message(f'/{wall} {link}')
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @xbotgroup_xbot dulu Goblok!!```")
            return
        else:
            downloaded_file_name = await event.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
            )
            os.remove(downloaded_file_name)
            await event.delete()
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])