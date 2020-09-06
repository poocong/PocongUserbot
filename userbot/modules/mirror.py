import asyncio
import io
import os
import random
import re
import textwrap
from asyncio.exceptions import TimeoutError
from random import randint, uniform

from glitch_this import ImageGlitcher
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from telethon import events, functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

Converted = TEMP_DOWNLOAD_DIRECTORY + "sticker.webp"

@register(outgoing=True, pattern=r"^\.mirror(?: |$)(.*)")
async def glitch(event):
    if not event.reply_to_msg_id:
        await event.edit("`Balas di Sticker Goblok!!!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Balas di Sticker Goblok!!!`")
        return
    await bot.download_file(reply_message.media)
    await event.edit("`Processing....`")
    if event.is_reply:
        data = await check_media(reply_message)
        if isinstance(data, bool):
            await event.edit("`File tidak di dukung...`")
            return
    else:
        await event.edit("`Reply to Any Media Sur`")
        return

    try:
        value = int(event.pattern_match.group(1))
        if value > 9:
            raise ValueError
    except ValueError:
        value = 2
    await event.edit("```Mirror This Media```")
    await asyncio.sleep(2)
    file_name = "mirror.png"
    to_download_directory = TEMP_DOWNLOAD_DIRECTORY
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloaded_file_name = await bot.download_media(
        reply_message,
        downloaded_file_name,
    )
    mirror_flip_file = downloaded_file_name
    mirror = ImageOps()
    im = Image.open(mirror_flip_file).convert('RGB')
    im.save(Converted, quality=95)
    await event.edit("`Uploading Mirror Media...`")
    await event.client.send_file(
        event.chat_id, sticker=Converted, force_document=False, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    os.remove(sticker=Converted)
    
    
    
    
