import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot

@register(outgoing=True, pattern=r"^\.o(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@xbotgroup_xbot"
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@xbotgroup_xbot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1281618755))
            await conv.send_message(f'/{wall} {link}')
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("`Unblock` @xbotgroup_xbot dulu Goblok!!`...`")
            return
        if response.text.startswith("You're"):
            await event.edit("`You're not listening to anything on Spotify at the moment`")
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
            return
        if response.text.startswith("Ads."):
            await event.edit("`You're listening to those annoying ads.`")
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
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
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
    await event.delete()
    return os.remove(downloaded_file_name)
