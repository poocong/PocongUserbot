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

    
@register(outgoing=True, pattern='^.jawa(?: |$)(.*)') 
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("baik")
    sleep(1)
    await typew.edit("Tidak Sombong")
    sleep(1)
    await typew.edit("Ganteng")
    sleep(1)
    await typew.edit("Sopan")
    sleep(1)
    await typew.edit("Rajin")
    sleep(1)
    await typew.edit("Budiman")
    sleep(1)
    await typew.edit("Alim")
    sleep(1)
    await typew.edit("Berguna")
    sleep(1)
    await typew.edit("Nguli Juga")
    sleep(1)
    await typew.edit("Pemaaf")
    sleep(1)
    await typew.edit("Jujur")
    sleep(1)
    await typew.edit("Tidk Sombong")
    sleep(1)
    await typew.edit("Kaya")
    sleep(1)
    await typew.edit("Pokoknya Jawa Pro Dah")
    sleep(1)
    await typew.edit("Tidak Seperti Yang Lain")
    sleep(1)
    await typew.edit("Bersama Jawa Membangun Negri")
    
@register(outgoing=True, pattern='^.erpe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Hai, Kamu Anak Erpe Ya")
    sleep(1)
    await typew.edit("Kok Pake Muka Orang sih?")
    sleep(1)
    await typew.edit("Oh iya, Muka Anak Erpe Kan")
    sleep(1)
    await typew.edit("**BURIK- BURIK**")
    sleep(1)
    await typew.edit("Jadinya Pake Muka Orang")
    sleep(1)
    await typew.edit("Karena Muka Anak erpe")
    sleep(1)
    await typew.edit("**BURIK- BURIK**")
    sleep(1)
    await typew.edit("Canda **BURIK**")
    sleep(1)
    await typew.edit("Lari Ada Plastik KePanasan")
                     
    
@register(outgoing=True, pattern='^.repobot(?: |$)(.*)')  
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("👻")
    sleep(2)
    await typew.edit("**𝙋𝙤𝙘𝙤𝙣𝙜 - 𝙐𝙨𝙚𝙧𝙗𝙤𝙩🔥**\n\n [𝚂𝚎𝚗𝚝𝚞𝚑 𝙰𝚔𝚞 𝙱𝚎𝚋](https://github.com/poocong/Pocong-Userbot)\n 𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠👻")

CMD_HELP.update({
    "animasi1":
    "`.hai`\
    \nPenjelasan: Cosplay Nissa Sablon\
    \n\n`.kntl`\
    \nPenjelasan: Cek Aja dh\
    \n\n`.alay`\
    \nPenjelasan: Lumayanlah Buat Nyindir\
    \n\n`.jawa`\
    \nPenjelasan: Jawa Pride Ni Bos.\
    \n\n`.erpe`\
    \nPenjelasan: Buat Nyindir Nak Rp Yg Goblok."
    
    
})
