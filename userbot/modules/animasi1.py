from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Hai ,  Assalamualaikum**")
    sleep(1)
    await typew.edit("Kalian Nungguin aku gak??")
    sleep(1)
    await typew.edit("Ih ga mau🤢")
    sleep(1)
    await typew.edit("gasukaa😫")
    sleep(1)
    await typew.edit("__GELAYY__🤮")
    
   
@register(outgoing=True, pattern='^.kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Tau kh kalian wahai tuan-tuan??")
    sleep(1)
    await typew.edit("se**KONT0L** **K0NTOL** nya si **K0NTOL**")
    sleep(1)
    await typew.edit("lebih **KONTOL** lagi")              
    sleep(1)
    await typew.edit("kalian **KONTOL**")


@register(outgoing=True, pattern='^.alay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("eh kamu, iya kamu")
    sleep(1)
    await typew.edit("**ALAY** bnget sih")
    sleep(1)
    await typew.edit("spam bot mulu")
    sleep(1)
    await typew.edit("baru jadi userbot ya?? xixixi")
    sleep(1)
    await typew.edit("pantes **NORAK**")

    
@register(outgoing=True, pattern='^.repobot(?: |$)(.*)') 
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("👻")
    sleep(1)
    await typew.edit("**𝚃𝚎𝚛𝚒𝚖𝚊𝚔𝚊𝚜𝚒𝚑 𝚃𝚎𝚕𝚊𝚑 𝙼𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗**")
    sleep(1)
    await.typew.edit("[REPO](https://github.com/poocong/Pocong-Userbot")

CMD_HELP.update({
    "animasi1":
    "`.hai` ; `.kntl` ; `.alay`\
    \nUsage: lu liat sendiri lah anjg"
})
