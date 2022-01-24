# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# ReCode by @PocongOnlen


from userbot import bot, CMD_HELP
from userbot.events import register


GCAST_BLACKLIST = [
    -1001267233272,    #PocongUserbot
    -1001294181499,    #UserbotIndonesia
]

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan aku teks`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Proses Mengirim Pesan Broadcast...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST
                 try:
                     done += 1
                     await bot.send_message(chat, msg)
                 except BaseException:
                     er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan aku teks`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Proses Mengirim Pesan Broadcast...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")

#XBot-Remix    

CMD_HELP.update({
    "gcast": 
"ㅤㅤㅤㅤ•**Syntax**: .gcast teks\
\n    •**Function**: Mengirim Pesan Broadcast Ke Seluruh Grup Yang Kmu Masuki.\
\n\nㅤㅤㅤㅤ•**Syntax**: .gucast teks\
\n    •**Function**: Mengirim Pesan Broadcast Ke Pengguna Telegram Yang Telah Kmu Chat." 
})

