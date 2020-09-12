# Originally from Bothub
# Port to UserBot by @heyworld
#Copyright (C) 2020 azrim.


import glob
import os
import shutil
import time

import deezloader
import requests
from bs4 import BeautifulSoup
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from telethon import events
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

from userbot import (
    CMD_HELP,
    DEEZER_ARL_TOKEN,
    LASTFM_USERNAME,
    TEMP_DOWNLOAD_DIRECTORY,
    bot,
    lastfm,
)
from userbot.events import register
from userbot.utils import progress
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from telethon.errors.rpcerrorlist import YouBlockedUserError
try:
 import subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

# For getvideosong


def getmusicvideo(cat):
    search = cat
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }
    html = requests.get(
        "https://www.youtube.com/results?search_query=" + search, headers=headers
    ).text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if "/watch?v=" in link.get("href"):
            # May change when Youtube Website may get updated in the future.
            video_link = link.get("href")
            break
    video_link = "http://www.youtube.com/" + video_link
    command = 'youtube-dl -f "[filesize<50M]" --merge-output-format mp4 ' + video_link
    os.system(command)



@register(outgoing=True, pattern="^.spd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading music taking some times,  Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)


@register(outgoing=True, pattern=r"^\.vsong(?: |$)(.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Wait..! I am finding your videosong..`")
    elif reply.message:
        query = reply.message
        await event.edit("`Wait..! I am finding your videosong..`")
    else:
        await event.edit("`What I am Supposed to find?`")
        return
    getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await event.edit("`Yeah..! i found something..`")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await event.edit("`Uploading video.. Please wait..`")
    os.system("cp *mp4 thumb.mp4")
    os.system("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
    thumb_image = "thumb.jpg"
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        thumb=thumb_image,
        allow_cache=False,
        caption=query,
        supports_streaming=True,
        reply_to=reply_to_id,
        attributes=[
            DocumentAttributeVideo(
                duration=duration,
                w=width,
                h=height,
                round_message=False,
                supports_streaming=True,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]", loa)
        ),
    )
    await event.delete()
    os.remove(thumb_image)
    os.system("rm -rf *.mkv")
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.webm")

@register(outgoing=True, pattern="^.netease(?: |$)(.*)")
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.reply("```Please unblock @WooMaiBot and try again```")
              return
          await netase.edit("`Sending Your Music...`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()


@register(outgoing=True, pattern="^.dzd(?: |$)(.*)")
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await Deezlod.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              details = await conv.get_response()
              song = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await Deezlod.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
              return
          await bot.send_file(Deezlod.chat_id, song, caption=details.text)
          await Deezlod.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, details.id, song.id])
          await Deezlod.delete()          
    
CMD_HELP.update({
        "music":
        ".spd`<Artist - Song Title>\
            \nUsage:For searching songs from Spotify.\
            \n\n`.netease` <Artist - Song Title>\
            \nUsage:Download music with @WooMaiBot\
            \n\n>`.vsong` **Artist - Song Title**"
            \nUsage: Finding and uploading videoclip.\
            \n\n`.dzd` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer.\
            \n\n`.deezload` <spotify/deezer link> <Format>\
            \nUsage: Download music from deezer.\
            \n\n Well deezer is not available in India so create an deezer account using vpn. Set DEEZER_ARL_TOKEN in vars to make this work.\
            \n\n *Format= `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`.\
            \n\n\n Guide:Video guide of arl token: [here](https://www.youtube.com/watch?v=O6PRT47_yds&feature=youtu.be) or Read [This](https://notabug.org/RemixDevs/DeezloaderRemix/wiki/Login+via+userToken)."
})


