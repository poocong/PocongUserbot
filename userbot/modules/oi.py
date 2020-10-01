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


@register(outgoing=True, pattern='^.io(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Muka Gue Burik...`")
    sleep(3)
    await typew.edit("`Kayak Jemboot`")
    sleep(1)
    await typew.edit("`Muka Gw Burik Kek Jembott`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lucinta Luna Berbatang ...`")
    sleep(3)
    await typew.edit("`Tapi Gua sukaa`")
    sleep(1)
    await typew.edit("`I love memek Oplass`")
# Create by myself @localheart
