# Copyright (C) 2020 TeamDerUntergang.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.

import logging

from telethon.errors.rpcerrorlist import BotInlineDisabledError

from userbot import BOT_TOKEN, BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    tgbotusername = BOT_USERNAME
    if tgbotusername and BOT_TOKEN:
        try:
            results = await event.client.inline_query(tgbotusername, "@ProjectAlf")
        except BotInlineDisabledError:
            return await event.edit(
                "`Bot tidak dapat digunakan dalam mode inline. \ Pastikan untuk mengaktifkan mode inline di @botfather!`"
            )
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        return await event.edit(
            "`Bot tidak berfungsi! Harap setel Token Bot dan Nama Pengguna dengan benar.`"
            "\n`Modul telah dihentikan.`"
        )
