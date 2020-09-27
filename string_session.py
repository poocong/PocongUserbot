#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677 and SpEcHiDe
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check di Telegram Pesan Tersimpan untuk Melihat Kode STRING_SESSION""")
API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check di Telegram Pesan Tersimpan untuk Melihat Kode STRING_SESSION")
    session_string = client.session.save()
    saved_messages_template = """XBOT CHANNEL SUPPORT: @XBOT_SUPPORT

<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <i>Silahkan Klick Code String Untuk Mengcopy</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
