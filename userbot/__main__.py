# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# ReCode by @Pocongonlen

""" Userbot start point """

import sys
from importlib import import_module

import requests
from pytgcalls import idle
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import LOGS, bot, branch, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autopilot, autobot, checking

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklist = requests.get(
        "https://raw.githubusercontent.com/poocong/darkweeb/master/blacklist.json"
    ).json()
    if user.id in blacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJISS BET DIPAKE BOCIL KEK LU.\nCredits: @Pocongonlen"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/PocongUserbot"
)

LOGS.info(f"PocongUserbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")

if not BOTLOG_CHATID:
    LOGS.info(
        "Vars BOTLOG_CHATID tidak terisi, Proses Membuat Grup Otomatis."
    )
    bot.loop.run_until_complete(autopilot())

async def pocong_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🔥 **PocongUserbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{branch}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@PocongProject"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest("@Poconguserbot"))
    except BaseException:
        pass
    


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(pocong_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()