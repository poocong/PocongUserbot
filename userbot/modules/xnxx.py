# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.o(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SaitamaRobot"
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@SaitamaRobot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=701937965))
            await conv.send_message(f'/{wall} ')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.client.send_file(event.chat_id)
