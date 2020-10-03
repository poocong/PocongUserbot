import io
import os
import random
import re
import textwrap

from telethon import events, functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from random import randint, uniform
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from telethon.tl.types import DocumentAttributeFilename




@register(outgoing=True, pattern=r"^\.wall(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XBOTGBOT"
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@XBOTGBOT") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1152386221))
            await conv.send_message(f'/{wall} {link}')
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @XBOTGBOT dulu Goblok!!```")
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


CMD_HELP.update({"wallpaper": ">`.wall` <query>."
                 "\nUsage: Search some wallpaper picture."})
