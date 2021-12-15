from time import sleep

from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.dana?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**PAYMENT ?\n\n Dana & Gopay\n\n ❏085372922123 **")
    sleep(9999)
    await typew.edit(".")

@register(outgoing=True, pattern='^.via(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Untuk Metode Pembayaran.\n\n ❏Dana\n ❏Gopay\n  ❏Pulsa ? + 5k**")
    sleep(9999)
    await typew.edit(".")
   
@register(outgoing=True, pattern='^.thnks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Done yaa kak🙏🏻\n TerimaKasih...\n\n [PocongOnlenStore?](https://t.me/Poocongonlen)\n [Testi](https://t.me/TestimoniPocong)")
    sleep(9999)
    await typew.edit(".")
