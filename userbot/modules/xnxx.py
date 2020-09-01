from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.events import register
from asyncio.exceptions import TimeoutError
from PIL import Image
from io import BytesIO
from userbot.events import register


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
        except YouBlockedUserError:
            await event.reply("```Unblock @xbotgroup_xbot plox```")
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await bot.send_read_acknowledge(event.chat_id)
            await event.client.delete_messages(event.chat_id, [response.id])
   except TimeoutError:
            await event.edit()
