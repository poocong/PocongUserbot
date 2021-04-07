# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Memeriksa Koneksi Server...__")
    end = datetime.now()
    duration = (end - start).microseconds / 100000
    await pong.edit(f"☤ **𓆩Pong𓆪**\n"
                    f"➦ __%sms__ \n"
                    f"➥ __**User {ALIVE_NAME}**__\n" % (duration))


@register(outgoing=True, pattern="^.speedtest$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "❖ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   "❖ **Download:** "
                   f"`{speed_convert(result['download'] * 8)}` \n"
                   "❖ **Upload:** "
                   f"`{speed_convert(result['upload'] * 8)}` \n"
                   "❖ **Ping:** "
                   f"`{result['ping']}` \n"
                   "❖ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "❖ **USER:** "
                   f"`{ALIVE_NAME}`\n")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

CMD_HELP.update(
    {"ngewe": "`.ping`\
    \nPemakaian: Untuk menunjukkan ping bot.\
    \n\n`.speedtest`\
    \nPemakaian: Untuk menunjukkan kecepatan koneksi."
     })
