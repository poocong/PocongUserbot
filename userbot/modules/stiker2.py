from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import io
import os
from userbot import CMD_HELP , bot
from userbot.events import register
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from PIL import Image

@register(outgoing=True, pattern="^.itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("sir this is not a image message reply to image message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("sir, This is not a image ")
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
            await event.reply("unblock me (@buildstickerbot) and try again")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Can you kindly disable your forward privacy settings for good?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


@register(outgoing=True, pattern="^.get$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Balas Ke Sticker Tuan`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Mohon Balas Ke Sticker Tuan`")
        return
    chat = "@stickers_to_image_bot"
    await event.edit("`Mengubah Menjadi Gambar....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Buka Blokir @stickers_to_image_bot Lalu Coba Lagi")
            return
        if response.text.startswith("I understand only stickers"):
            await event.edit("`Maaf Tuan, Saya Tidak Bisa Mengubah Ini Menjadi Gambar, Periksa Kembali Apakah Itu Sticker Animasi?`")
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
                await event.client.delete_message(event.chat_id, [msg.id, response.id])
            else:
                await event.edit("`Coba Lagi`")
        await bot.send_read_acknowledge(conv.chat_id)


@register(outgoing=True, pattern="^.stoi$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("`NULL information to feftch...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("`Maaf Tuan, Ini Bukan Sticker`")
        return False

    await sticker.edit("`Berhasil Mengambil Sticker!`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return

# Tiny From Ultroid

@register(outgoing=True, pattern=r"^\.tiny(?: |$)(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await event.edit("`Mohon Balas Ke Sticker`")
        return
    await event.edit("`Memproses...`")
    ik = await bot.download_media(reply)
    im1 = Image.open("userbot/poconguserbot.png")
    if ik.endswith(".tgs"):
        await event.client.download_media(reply, "ult.tgs")
        os.system("lottie_convert.py ult.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = jsn.replace("512", "2000")
        open("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await event.delete()
    os.remove(file)
    os.remove(ik)


@register(outgoing=True, pattern=r"^\.frog (.*)")
async def honkasays(event):
    await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Beri Aku Bebeberapa Teks, Contoh .frog test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Maaf Saya tidak bisa menggunakan hal-hal sebaris di sini...`")
    except ChatSendStickersForbiddenError:
        await event.edit("Maaf saya tidak bisa mengirim stiker ke sini !!")


CMD_HELP.update({
        "stiker2":
        "**Perintah**: .help stickers2\
        \n**Total Command: 5**\
        \n\nㅤㅤ•**Cmd**: .itos\
        \n•**Function**: __Reply di stiker , untuk mengambil gambar__.\
        \n\nㅤㅤ•**Cmd**: .get\
        \n•**Function**: __Reply di stiker untuk mengambil file 'PNG' stiker__.\
        \n\nㅤㅤ•**Cmd**: .stoi\
        \n•**Function**: __Reply di stiker untuk mengambil file 'PNG' stiker__.\
        \n\nㅤㅤ•**Cmd**: .tiny\
        \n•**Function**: __Reply di stiker untuk memperkecil ukuran stiker__.\
        \n\nㅤㅤ•**Cmd**: .frog <kata - kata>\
        \n•**Function**: __Membuat animasi stiker__."
        
})
