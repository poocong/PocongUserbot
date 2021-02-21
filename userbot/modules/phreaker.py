import asyncio
import os
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    nmap = f"nmap"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{nmap} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    subdomain = f"subdomain"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{subdomain} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.cek(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    httpheader = f"httpheader"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{httpheader} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    try:
        query = event.pattern_match.group(1)
        await event.edit("`Processing..`")
        async with bot.conversation("@Carol5_bot") as conv:
            try:
                query1 = await conv.send_message(f"/bin {query}")
                asyncio.sleep(3)
                r1 = await conv.get_response()
                r2 = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await event.reply("Unblock @Carol5_bot plox")
            if r1.text.startswith("No"):
                return await event.edit(f"`No result found for` **{query}**")
            else:
                p = await event.client.send_messages(
                    event.chat_id,
                    r1, r2,
                    reply_to=event.reply_to_msg_id,
                )

                await event.client.delete_messages(
                    conv.chat_id, [r1.id, r2.id, query1.id]
                )


CMD_HELP.update({
    "phreaker":
    "`.nmap <bug hosts>`\
\nUsage: to get info bug/host.\
\n\n`.subd <bug hosts>`\
\nUsage: to get subdomain bug/host.\
\n\n`.cek <bug hosts>`\
\nUsage: to cek respons bug/host.\
    \n\n`.bin < bin number >`\
    \nUsage: to cek bin ip."
})
