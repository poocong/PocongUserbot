# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# This script wont run your bot, it just generates a session.

import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv


if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "XBOT",
            api_key=int(os.environ.get("API_KEY") or input("Enter Telegram API KEY: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: ")
    ) as userbot:
        print("\nprocessing...")
        await userbot.send_message(
            "me", f"#XBOT #HU_STRING_SESSION\n\n```{await userbot.export_session_string()}```")
        print("Done !, session string has been sent to saved messages!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
