import asyncio
import io
import os
import random
import re
import urllib.request
from os import remove

import cv2
import numpy as np
from PIL import Image, ImageDraw
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    MessageMediaPhoto,
)

from userbot import bot, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register


@register(outgoing=True, pattern=r"^\.tiny$")
async def ultiny(event):
   if not event.reply_to_msg_id:
        await event.edit("`Reply to Any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    await event.edit("`Processing..`")
    if reply_message.photo:
        transform = await bot.download_media(
            reply_message,
            "tiny.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "tiny.tgs",
        )
    im1 = Image.open("userbot/resource/remix_blank.png")
        os.system("lottie_convert.py tiny.png tiny.tgs")
        transform = "tiny.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "tiny.mp4",
        )
        extractMetadata(createParser(video))
        os.system(
            "ffmpeg -i tiny.mp4 -vframes 1 -an -s 480x360 -ss 1 tiny.png"
        )
        transform = "tiny.png"
    else:
        transform = await bot.download_media(
            reply_message,
            "tiny.png",
        )
    try:
        iik = cv2.VideoCapture(transform)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(transform)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(transform)

