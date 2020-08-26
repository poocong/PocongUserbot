import os
import textwrap

from PIL import Image, ImageFont, ImageDraw

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from io import BytesIO
from PIL import Image
import asyncio
import time
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo
from userbot.utils import progress, humanbytes, time_formatter
from userbot import (TEMP_DOWNLOAD_DIRECTORY, CMD_HELP, bot)
from userbot.events import register
import datetime
from collections import defaultdict
import math
import os
import requests
import zipfile
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (DocumentAttributeFilename, DocumentAttributeSticker,
                               InputMediaUploadedDocument, InputPeerNotifySettings,
                               InputStickerSetID, InputStickerSetShortName,
                               MessageMediaPhoto)

THUMB_IMAGE_PATH = "./thumb_image.jpg"


@register(outgoing=True, pattern="^.mmf(?: |$)(.*)")
async def memify(message):
    replied = message.reply_to_message
    if not replied:
        await message.err("LMAO no one's gonna help you, if u use .help now then u **Gey**")
        await message.client.send_sticker(
            sticker="CAADAQADhAAD3gkwRviGxMVn5813FgQ", chat_id=message.chat.id)
        return
    if not (replied.photo or replied.sticker or replied.animation):
        await message.err("Bruh, U Comedy me? Read help or gtfo (¬_¬)")
        return
    if not os.path.isdir(THUMB_IMAGE_PATH):
        os.makedirs(THUMB_IMAGE_PATH)
    await message.edit("He he, let me use my skills")
    dls = await message.client.download_media(
        message=message.reply_to_message,
        file_name=THUMB_IMAGE_PATH,
        progress=progress,
        progress_args=(message, "Trying to Posses given content")
    )
    dls_loc = os.path.join(THUMB_IMAGE_PATH, os.path.basename(dls))
    if replied.sticker and replied.sticker.file_name.endswith(".tgs"):
        await message.edit("OMG, an Animated sticker ⊙_⊙, lemme do my bleck megik...")
        png_file = os.path.join(THUMB_IMAGE_PATH, "meme.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {dls_loc} {png_file}"
        stdout, stderr = (await runcmd(cmd))[:2]
        os.remove(dls_loc)
        if not os.path.lexists(png_file):
            await message.err("This sticker is Gey, i won't memify it ≧ω≦")
            raise Exception(stdout + stderr)
        dls_loc = png_file
    elif replied.animation:
        await message.edit("Look it's GF. Oh, no it's just a Gif ")
        jpg_file = os.path.join(THUMB_IMAGE_PATH, "meme.jpg")
        await take_screen_shot(dls_loc, 0, jpg_file)
        os.remove(dls_loc)
        if not os.path.lexists(jpg_file):
            await message.err("This Gif is Gey (｡ì _ í｡), won't memify it.")
            return
        dls_loc = jpg_file
    await message.edit("Decoration Time ≧∇≦, I'm an Artist")
    webp_file = await draw_meme_text(dls_loc, message.input_str)
    await message.client.send_sticker(chat_id=message.chat.id,
                                      sticker=webp_file,
                                      reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)


async def draw_meme_text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype("userbot/utils/fontx.ttf", int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(xy=(((i_width - u_width) / 2) - 1, int((current_h / 640)*i_width)),
                      text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=(((i_width - u_width) / 2) + 1, int((current_h / 640)*i_width)),
                      text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=((i_width - u_width) / 2, int(((current_h / 640)*i_width)) - 1),
                      text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=(((i_width - u_width) / 2), int(((current_h / 640)*i_width)) + 1),
                      text=u_text, font=m_font, fill=(0, 0, 0))

            draw.text(xy=((i_width - u_width) / 2, int((current_h / 640)*i_width)),
                      text=u_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 1, i_height - u_height - int((20 / 640)*i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, i_height - u_height - int((20 / 640)*i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height - u_height - int((20 / 640)*i_width)) - 1),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height - u_height - int((20 / 640)*i_width)) + 1),
                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(
                xy=((i_width - u_width) / 2, i_height - u_height - int((20 / 640)*i_width)),
                text=l_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad

    image_name = "memify.webp"
    webp_file = os.path.join(THUMB_IMAGE_PATH, image_name)
    img.save(webp_file, "WebP")
    return webp_file



CMD_HELP.update({
    "memify": 
        "`.mmf` texttop ; textbottom\
        \nUsage: Reply a sticker/image/gif and send with cmd."
})
