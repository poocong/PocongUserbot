import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import io
import math
import urllib.request
from os import remove
from PIL import Image
import random
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.events import register
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker

@register(outgoing=True, pattern="^.itos$")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("sir this is not a image message reply to image message")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("sir, This is not a image ")
       return
    chat = "@buildstickerbot"
    await event.edit("Making a sticker")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=164977173))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("unblock me (@buildstickerbot) and try again")
              return
          if response.text.startswith("Hi!"):
             await event.edit("Can you kindly disable your forward privacy settings for good?")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
          await bot.send_read_acknowledge(conv.chat_id)
            
@register(outgoing=True, pattern="^.gets$")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Balas di Sticker Goblok!!")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("Balas di Sticker Tolol!!")
       return
    chat = "@stickers_to_image_bot"
    await event.edit("Conver to image..")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("unblock me (@stickers_to_image_bot) to work")
              return
          if response.text.startswith("I understand only stickers"):
              await event.edit("Sorry i cant't convert it check wheter is non animated sticker or not")
          else:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
              response = await response
              if response.text.startswith("..."):
                  response = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
                  response = await response
                  await event.delete()
                  await event.client.send_message(event.chat_id, response.message , reply_to = reply_message.id)
              else:
                  await event.edit("try again")
          await bot.send_read_acknowledge(conv.chat_id)
        
