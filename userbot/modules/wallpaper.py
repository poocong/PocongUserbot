import asyncio
import os
from random import choice, randint

import requests
from bs4 import BeautifulSoup as soup
from PIL import Image

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, WALL_API
from userbot.events import register

down_p = str(TEMP_DOWNLOAD_DIRECTORY.rstrip("/"))


@register(outgoing=True, pattern=r"^\.wall ?(.*)")
async def wallp(event):
    if not os.path.isdir(down_p):
        os.makedirs(down_p)
        json_rep = r.get(
            f"https://wall.alphacoders.com/api2.0/get.php?auth={WALL_API}&method=search&term={term}"
        ).json()
        if not json_rep.get("success"):
            msg.edit_text(f"An error occurred! Report this")
        else:
            wallpapers = json_rep.get("wallpapers")
            if not wallpapers:
                msg.edit_text("No results found! Refine your search.")
                return
            else:
                index = randint(0, len(wallpapers) - 1)  # Choose random index
                wallpaper = wallpapers[index]
                wallpaper = wallpaper.get("url_image")
                wallpaper = wallpaper.replace("\\", "")
                event.send_photo(
                    chat_id,
                    photo=wallpaper,
                    caption='Preview')
                event.send_document(
                    chat_id,
                    document=wallpaper,
                    filename='wallpaper',
                    caption=caption)


CMD_HELP.update({"wallpaper": ">`.wall` <query>."
                 "\nUsage: Search some wallpaper picture."})
