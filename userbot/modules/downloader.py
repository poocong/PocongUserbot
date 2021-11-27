# All rights reserved.
# Keredit
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

# INSTAGRAM DOWNLOADER
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

# TIKTOK DOWNLOADER
@register(outgoing=True, pattern="^.tt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Link Nya Mana Anjg Ga Bisa Download Lah Gw Kalo Ga Pake Link Tt Nya Bngsd` **(._.)**")
    else:
        await event.edit("```Video Sedang Diproses.....```")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Kesalahan:** `Woy Kontol Buka Dulu Blokir` @ttsavebot `Dan Coba Lagi!`")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()

# Tiktok Downloader
CMD_HELP.update({
           "tiktok":
           "**Perintah**: .help tiktok\
           \n\nㅤㅤ•**Cmd**: .tt (link tiktok)\
           \n•**Function**: __Download video tiktok tanpa watermark__."
})
        

# Instagram Downloader
CMD_HELP.update({
           "instagram":
           "**Perintah**: .help instagram\
           \n\nㅤㅤ•**Cmd**: .ig (reply di link)\
           \n•**Function**: __Download video / foto dari Instagram__."
})
