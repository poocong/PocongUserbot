# Copyright (C) 2020-2021 by poocong@Github, < https://github.com/poocong >.
#
# This file is part of < https://github.com/poocong/PyroUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/poocong/PyroUserbot/blob/master/LICENSE >
#
# All rights reserved.


from telethon import events
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio


@register(outgoing=True, pattern=r"^\.tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    await event.edit("`Sedang Memprosess...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await king.edit("`Mohon buka blokir` @TempMailBot `lalu coba lagi`")
            return
        await event.edit(f"**TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({PocongUserbot})")



CMD_HELP.update({"tempmail": "**Modules:** __Temp Mail__\n\n: `.tm`"
                 "\n**Penjelasan:** Mendapatkan Email Gratis Dari Temp Mail"})
