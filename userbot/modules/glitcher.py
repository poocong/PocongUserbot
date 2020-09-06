import asyncio
import io
import os
import random
import re
import textwrap
from random import randint, uniform

from glitch_this import ImageGlitcher
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from telethon import events, functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

THUMB_IMAGE_PATH = "./thumb_image.jpg"

Glitched = TEMP_DOWNLOAD_DIRECTORY + "glitch.gif"

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


@register(outgoing=True, pattern=r"^\.glitch(?: |$)(.*)")
async def glitch(event):
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
    file_name = "glitch.png"
    to_download_directory = TEMP_DOWNLOAD_DIRECTORY
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloaded_file_name = await bot.download_media(
        reply_message,
        downloaded_file_name,
    )
    glitch_file = downloaded_file_name
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    glitch_img = glitcher.glitch_image(img, value, color_offset=True, gif=True)
    DURATION = 200
    LOOP = 0
    glitch_img[0].save(
        Glitched,
        format="GIF",
        append_images=glitch_img[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    await event.edit("`Uploading Glitched Media...`")
    nosave = await event.client.send_file(
        event.chat_id, Glitched, force_document=False, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    os.remove(Glitched)
    await bot(
        functions.messages.SaveGifRequest(
            id=types.InputDocument(
                id=nosave.media.document.id,
                access_hash=nosave.media.document.access_hash,
                file_reference=nosave.media.document.file_reference,
            ),
            unsave=True,
        )
    )
    os.remove(glitch_file)
