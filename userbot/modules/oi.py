from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Muka kalian Burik...`")
    sleep(3)
    await typew.edit("`Kayak Jemboot`")
    sleep(1)
    await typew.edit("`Muka Gw Gak Burik Kek Kalian`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Kamu...`")
    sleep(3)
    await typew.edit("`Tetap Semangat Ya`")
    sleep(1)
    await typew.edit("`Walau Sering Di Ghosting xixixi`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Ayang Ange😖`")
    sleep(3)
    await typew.edit("`Pap Memek Dulu Dong Ayang👉👈`")
    sleep(1)
    await typew.edit("`Please Yang Pap Memek Aku Lagi Ange Nih 😖`")
# Create by myself @localheart
