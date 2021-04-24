# Bismillah
# Apa Lu Ga Terima?
# Suka Suka Gw Dong
# Kok Ngatur
# Pap TT kak 👻
# All rights reserved.
# Keredit
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# King Userbot - From King To King
# Yang Gbs Basa Enggres bisa Terjemahkan di atas
# Ngefork Doang Gak Bintang Anjg
# Kalo Clone Ini Jangan dihapus ya anjg nanti Ocong Ngamuk, Ok Mksh Sma Sma

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

# Anjing lu pada
# Kontol bapak kau pecah


@register(outgoing=True, pattern="^.ig ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Balas Ke Link Instagram`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Link Media Instagram Untuk Download`")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Memproses....`")
        return
    await event.edit("`Memproses.....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("`Mohon Buka Blokir` @SaveAsbot `Lalu Coba Lagi`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Creator @Pocongonlen**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


# By Pocong - Userbot
# Hmm
# Dah lah Cape 
CMD_HELP.update({"instagram": "**Modules:** __Instagram__\n\n𝘾𝙈𝘿: `.ig`"
                 "\n**Penjelasan:** Download Media di Postingan Instagram, Balas ke link instagram ketik `.ig`"})
