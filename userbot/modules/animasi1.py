from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Hai ,  Assalamualaikum**")
    sleep(2)
    await typew.edit("Kalian Nungguin aku gak??")
    sleep(2)
    await typew.edit("Ih ga mau🤢")
    sleep(2)
    await typew.edit("gasukaa😫")
    sleep(2)
    await typew.edit("__GELAYY__🤮")
    
CMD_HELP.update(
    {"animasi1": "`hai`\
    \nPemakaian: lihat sendiri lah anj."
     })
