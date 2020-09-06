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


@register(outgoing=True, pattern="^.db$")
async def ghost(event):
    if not event.reply_to_msg_id:
        await event.edit("`I Wont Glitch A Ghost!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    await bot.download_file(reply_message.media)
    await event.edit("`Downloading Media..`")
    if event.is_reply:
    data = await check_media(reply_message)
        if isinstance(data, bool):
            await event.edit("`Unsupported Files...`")
            return
    else:
        await event.edit("`Reply to Any Media Sur`")
        return

    try:
    value = int(event.pattern_match.group(1))
        if value > 8:
            raise ValueError
    except ValueError:
        value = 2
    await event.edit("```Glitching This Media```")
    await asyncio.sleep(2)
    file_name = "ghost.png"
    to_download_directory = TEMP_DOWNLOAD_DIRECTORY
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloaded_file_name = await bot.download_media(
        reply_message,
        downloaded_file_name,
    )
        ghost_file = downloaded_file_name
    if replied.sticker and replied.sticker.file_name.endswith(".tgs")
        await event.edit("`Uploading Glitched Media...`")
    nosave = await event.client.send_file(
                 event.chat_id, ghost_file, force_document=False, reply_to=event.reply_to_msg_id
             )
    await event.delete()
    if ghost_file is None:
        ghost_file = dls_loc
    im = Image.open(ghost_file).convert('RGB')
    im_invert = ImageOps.invert(im)
    im_invert.save(Converted)
    await message.client.send_sticker(
        message.chat.id,
        sticker=Converted,
        reply_to_message_id=replied.message_id)
    await message.delete()
    for files in (dls_loc, ghost_file, Converted):
        if files and os.path.exists(files):
            os.remove(files)
