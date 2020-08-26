from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gid(?: |$)(.*)")
async def (event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Balas di Pesan Goblok!!.```")
       return
    message = await event.get_reply_message() 
    chat = "@getidsbot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Balas di Pesan Goblok!!.```")
       return
    await event.edit("```Membongkar ID..```")
    async with borg.conversation(chat) as conv:
          try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await event.reply("`Bunuh @getidsbot dulu bos, biar botnya bisa jalan -_-`")
                return
          if response.text.startswith("Profil Buriq Tidak Punya ID,"):
             await event.edit("```Profil Buriq Tidak Punya ID..```")
          await event.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await event.edit(f"{response.message}")
            await event.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@getidsbot not responding!.`")


CMD_HELP.update({
    "get_uid":
    "`.gid`"
    "\nUsage: Reply in message to get user ID."
})
