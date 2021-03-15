# Authored by @Khrisna_Singhal & Sh1vam & @danish_00
# Ported from Userge by Alfiananda P.A & X-ImFine

import requests, os ,re
import PIL
import cv2
import random
import numpy as np
from colour import Color
from telegraph import upload_file
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image, ImageOps, ImageDraw, ImageFont
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

bground = "black"


@register(outgoing=True, pattern=r"^\.(ascii|asciis)$")
async def ascii(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to Any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker/video`")
        return
    await event.edit("`Downloading Media..`")
    if reply_message.photo:
        IMG = await bot.download_media(
            reply_message,
            "ascii.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "ASCII.tgs",
        )
        os.system("lottie_convert.py ASCII.tgs ascii.png")
        IMG = "ascii.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "ascii.mp4",
        )
        extractMetadata(createParser(video))
        os.system("ffmpeg -i ascii.mp4 -vframes 1 -an -s 480x360 -ss 1 ascii.png")
        IMG = "ascii.png"
    else:
        IMG = await bot.download_media(
            reply_message,
            "ascii.png",
        )
    try:
        await event.edit("`Processing..`")
        list = await random_color()
        color1 = list[0]
        color2 = list[1]
        bgcolor = bground
        await asciiart(IMG, color1, color2, bgcolor)
        cmd = event.pattern_match.group(1)
        if cmd == "asciis":
            os.system("cp ascii.png ascii.webp")
            ascii_file = "ascii.webp"
        else:
            ascii_file = "ascii.png"
        await event.client.send_file(
            event.chat_id,
            ascii_file,
            force_document=False,
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        os.system("rm *.png")
        os.system("rm *.webp")
        os.system("rm *.mp4")
        os.system("rm *.tgs")
    except BaseException as e:
        os.system("rm *.png")
        os.system("rm *.webp")
        os.system("rm *.mp4")
        os.system("rm *.tgs")
        return await event.edit(str(e))


async def asciiart(IMG, color1, color2, bgcolor):
    chars = np.asarray(list(" .,:irs?@9B&#"))
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height / letter_width
    img = Image.open(IMG)
    widthByLetter = round(img.size[0] * 0.15 * WCF)
    heightByLetter = round(img.size[1] * 0.15)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** 2.2 * (chars.size - 1)
    lines = ("\n".join(("".join(r)
                        for r in chars[img.astype(int)]))).split("\n")
    nbins = len(lines)
    colorRange = list(Color(color1).range_to(Color(color2), nbins))
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    leftpadding = 0
    y = 0
    lineIdx = 0
    for line in lines:
        color = colorRange[lineIdx]
        lineIdx += 1
        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height
    IMG = newImg.save("ascii.png")
    return IMG


# this is from userge
async def random_color():
    color = [
        "#" + "".join([random.choice("0123456789ABCDEF") for k in range(6)])
        for i in range(2)
    ]
    return color


@register(outgoing=True, pattern=r"^\.asciibg(?: |$)(.*)")
async def _(event):
    BG = event.pattern_match.group(1)
    if BG.isnumeric():
        return await event.edit("`Please input a color not a number!`")
    elif BG:
        global bground
        bground = BG
    else:
        return await event.edit("`please insert bg of ascii`")
    await event.edit(f"`Successfully set bg of ascii to` **{BG}**")


Converted = TEMP_DOWNLOAD_DIRECTORY + "sticker.webp"


@register(outgoing=True, pattern=r"^\.(mirror|flip|ghost|bw|poster)$")
async def transform(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to Any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    await event.edit("`Downloading Media..`")
    if reply_message.photo:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        os.system("lottie_convert.py transform.tgs transform.png")
        transform = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        os.system(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        transform = "transform.png"
    else:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        await event.edit("`Transforming this media..`")
        cmd = event.pattern_match.group(1)
        im = Image.open(transform).convert("RGB")
        if cmd == "mirror":
            IMG = ImageOps.mirror(im)
        elif cmd == "flip":
            IMG = ImageOps.flip(im)
        elif cmd == "ghost":
            IMG = ImageOps.invert(im)
        elif cmd == "bw":
            IMG = ImageOps.grayscale(im)
        elif cmd == "poster":
            IMG = ImageOps.posterize(im, 2)
        IMG.save(Converted, quality=95)
        await event.client.send_file(
            event.chat_id, Converted, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        os.system("rm -rf *.mp4")
        os.system("rm -rf *.tgs")
        os.remove(transform)
        os.remove(Converted)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.rotate(?: |$)(.*)")
async def rotate(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any media..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker`")
        return
    await event.edit("`Downloading Media..`")
    if reply_message.photo:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        os.system("lottie_convert.py transform.tgs transform.png")
        rotate = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        os.system(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        rotate = "transform.png"
    else:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        value = int(event.pattern_match.group(1))
        if value > 360:
            raise ValueError
    except ValueError:
        value = 90
    await event.edit("`Rotating your media..`")
    im = Image.open(rotate).convert("RGB")
    IMG = im.rotate(value, expand=1)
    IMG.save(Converted, quality=95)
    await event.client.send_file(
        event.chat_id, Converted, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.tgs")
    os.remove(rotate)
    os.remove(Converted)


path = "./downloads/"

@register(outgoing=True, pattern="^.wast$")
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.edit("`Reply to Any media..`")
        return
    reply = await event.get_reply_message()
    if not reply.media:
        await event.edit("`reply to a image/sticker`")
        return
    await event.edit("`Downloading Media..`")
    #os.system(f'wget https://telegra.ph/file/26d43e25cb2095a931ab1.jpg')
    os.system(f'wget https://telegra.ph/file/b3a6038bc825cc4edc4f0.png')
    img = await bot.download_media(reply.media, path)

    mon = "b3a6038bc825cc4edc4f0.png"
    foreground = Image.open(mon).convert("RGBA")
    img = cv2.VideoCapture(img) 
    tales, miraculous = img.read()
    cv2.imwrite("MiraculousLadybug.png",miraculous)
    shvm=PIL.Image.open("MiraculousLadybug.png")
    shi,vam = shvm.size
    img=shvm.resize((512,512))
    img.save("shivamgta.png", format="PNG", optimize=True)
    img = cv2.VideoCapture("shivamgta.png") 
    tales, miraculousladybug = img.read()
    gray = cv2.cvtColor(miraculousladybug, cv2.COLOR_BGR2GRAY) 
    #gray = cv2.medianBlur(gray, 5)
    bug = cv2.imwrite("shivamgtas.jpg", gray)
    image = cv2.imread("shivamgtas.jpg")
    overlay = image.copy()########################

    x, y, w, h = 0, 210, 800, 100
    overlay =cv2.rectangle(overlay, (x, y), (x+w, y+h), (0,0,0), -1) 

    alpha = 0.5  # Transparency factor.0.8

    # Following line overlays transparent rectangle over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    cv2.imwrite("shivamgta.jpg", image_new)######################################

    background = Image.open("shivamgta.jpg").convert("RGB")
    with Image.open("shivamgta.jpg") as imge:
        width, height = imge.size
    fg_resized = foreground.resize((width, int(height/5)))
    background.paste(fg_resized, box=(0,int(height/2)-50), mask=fg_resized)
    background.save("shivamwasted.png")
    miraculous=PIL.Image.open("shivamwasted.png")
    img=miraculous.resize((int(shi),int(vam)))
    img.save("shivamwastedgta.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "shivamwastedgta.png", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    os.system("rm -f .wget-hsts")
    os.system("rm -f MiraculousLadybug.png")
    os.system("rm -f shivamgta.jpg")
    os.system("rm -f shivamgta.png")
    os.system("rm -f shivamgtas.jpg")
    os.system("rm -f shivamwastedgta.png")
    os.system("rm -f shivamwasted.png")
    os.system("rm -f *.png")
    os.system("rm -f downloads/*.webp")
    os.system("rm -f downloads/*.jpg")


path = "./downloads/"
if not os.path.isdir(path):
    os.makedirs(path)


@register(outgoing=True, pattern=r"^\.icircle(?: |$)(.*)")
async def shiv(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    licence = event.text
    liscence = licence[8:]
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()

    download = await bot.download_media(reply.media, path)
    miraculous = cv2.VideoCapture(download)
    ladybug, catnoar = miraculous.read()
    cv2.imwrite("shivamcircular.png", catnoar)
    #image = PIL.Image.open(download)
    img = Image.open("shivamcircular.png").convert("RGB")
    npImage = np.array(img)
    h, w = img.size
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    npImage = np.dstack((npImage, npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('sirsle.png')
    # await event.edit(f"Dimensions Of Image are {shi} by {vam}")
    #img.save("sh1vam.png", format="PNG", optimize=True)
    await event.delete()
    await event.client.send_file(event.chat_id, "sirsle.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove(download)
    os.remove("sirsle.png")
    os.remove("shivamcircular.png")


@register(outgoing=True, pattern=r"^\.scircle(?: |$)(.*)")
async def shiv(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    licence = event.text
    liscence = licence[8:]
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    danish = cv2.VideoCapture(download)
    ret, frame = danish.read()
    cv2.imwrite("danish.jpg", frame)
    img = Image.open("danish.jpg").convert("RGB")
    npImage = np.array(img)
    h, w = img.size
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    npAlpha = np.array(alpha)
    npImage = np.dstack((npImage, npAlpha))
    Image.fromarray(npImage).save('shivam.webp')
    await event.delete()
    await event.client.send_file(event.chat_id, "shivam.webp", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove(download)
    os.remove("shivam.webp")
    os.remove("danish.jpg")


CMD_HELP.update(
    {
        "transform": ">`.ghost`"
        "\nUsage: Enchance your image to become a ghost!."
        "\n\n>`.ascii`"
        "\nUsage:create ascii art from media"
        "\n\n>`.asciis`"
        "\nUsage:same but upload result as sticker"
        "\n\n>`.asciibg <color>`"
        "\nUsage:Now to use ASCII module change first background color past"
        "\n\n>`.flip`"
        "\nUsage: To flip your image"
        "\n\n>`.mirror`"
        "\nUsage: To mirror your image"
        "\n\n>`.bw`"
        "\nUsage: To Change your colorized image to b/w image!"
        "\n\n>`.poster`"
        "\nUsage: To posterize your image!"
        "\n\n>`.icircle`"
        "\nUsage: To Convert image to Circle image!"
        "\n\n>`.scircle`"
        "\nUsage: same but upload result as sticker"
        "\n\n>`.rotate <value>`"
        "\nUsage: To rotate your image\n* The value is range 1-360 if not it'll give default value which is 90"
        "\n\n>`.wast`"
        "\nUsage: To wasted in image as GTA"
    }
)
