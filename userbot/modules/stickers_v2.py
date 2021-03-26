from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import io
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Pak ini bukan pesan gambar balas pesan gambar")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("Pak, ini bukan gambar ")
        return
    chat = "@buildstickerbot"
    await event.edit("Membuat Sticker..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=164977173))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("buka blokir saya @buildstickerbot dan coba lagi")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Bisakah Anda dengan ramah menonaktifkan pengaturan privasi Anda untuk selamanya?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(conv.chat_id, [msg.id, response.id])


@register(outgoing=True, pattern="^.get$")
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
    await event.edit("Convert to image..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("buka blokir saya @stickers_to_image_bot agar bekerja")
            return
        if response.text.startswith("Saya hanya mengerti stiker"):
            await event.edit("Maaf saya tidak bisa mengubahnya, periksa apakah stiker inj beranimasi atau tidak")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            response = await response
            if response.text.startswith("..."):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=611085086))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_messages(conv.chat_id,
                                                   [msg.id, response.id])
            else:
                await event.edit("try again")
        await bot.send_read_acknowledge(conv.chat_id)


@register(outgoing=True, pattern="^.stoi$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("`NULL information to feftch...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("Ini Bukan sticker Goblok!!!...`")
        return False

    await sticker.edit("`Stiker Berhasil Di Colong!`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return


CMD_HELP.update(
    {
        "stickers_v2": ">`.itos`"
        "\nUsage: Reply .itos ke stiker atau gambar untuk di-kang ke userbot no pack Anda "
        "\n\n>`.get`"
        "\nUsage: membalas stiker untuk mendapatkan file 'PNG' stiker."
        "\n\n>`.stoi`"
        "\nUsage: membalas stiker untuk mendapatkan file 'PNG' stiker."})
