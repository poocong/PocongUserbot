import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError

@register(outgoing=True, pattern=r"^\.gid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Balas di Pesan Goblok!!.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Balas di Pesan Goblok!!```")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Balas di Pesan Goblok!!.```")
       return
    await event.edit("```Membongkar ID..```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```you blocked bot```")
              return
          if response.text.startswith("Hello,"):
             await event.edit("```Profil Buriq Tidak Punya ID..```")
          else: 
             await event.edit(f"{response.message.message}")



CMD_HELP.update({
    "get_uid":
    "`.gid`"
    "\nUsage: Reply in message to get user ID."
})
