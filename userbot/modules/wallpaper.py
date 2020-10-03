import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import TEMP_DOWNLOAD_DIRECTORY, CMD_HELP, bot
import os


@register(outgoing=True, pattern=r"^\.wall(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@LyndaRobot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1281618755))
            await conv.send_message(f'/{wall} {link}')
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LyndaRobot dulu Goblok!!```")
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
