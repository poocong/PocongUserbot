from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(3)
    await typew.edit("`Wie De Dong Tian...`")
    sleep(3)
    await typew.edit("`Shalom  Aleichem b'Shem Ha Mashiach...`")
    sleep(3)
    await typew.edit("`Om Swastyastu...`")
    sleep(3)
    await typew.edit("`Namo Buddhaya...`")
    sleep(3)
    await typew.edit("`Shalom...`")
    sleep(3)
    await typew.edit("`Assalamualaikum...`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(3)
    await typew.edit("`Wie De Dong Tian...`")
    sleep(3)
    await typew.edit("`Shalom  Aleichem b'Shem Ha Mashiach...`")
    sleep(3)
    await typew.edit("`Om Swastyastu...`")
    sleep(3)
    await typew.edit("`Namo Buddhaya...`")
    sleep(3)
    await typew.edit("`Shalom...`")
    sleep(3)
    await typew.edit("`Assalamualaikum...`")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bro! Jawab Salam Dong...`")
    sleep(3)
    await typew.edit("`Om Swastyastu Semeton......`")
    sleep(3)
    await typew.edit("`Damai Dihati......`")
    sleep(3)
    await typew.edit("`Waallaikumsalam......`")


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bro! Jawab Salam Dong...`")
    sleep(3)
    await typew.edit("`Om Swastyastu Semeton......`")
    sleep(3)
    await typew.edit("`Damai Dihati......`")
    sleep(3)
    await typew.edit("`Waallaikumsalam......`")


CMD_HELP.update({
    "salam":
    "`P` atau `p`\
\nUsage: Untuk Memberi salam.\
\n\n`L` atau `l`\
\nUsage: Untuk Menjawab Salam."
})
