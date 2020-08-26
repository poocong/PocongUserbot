from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gid(?: |$)(.*)")
async def firstname(uid):
    if uid.fwd_from:
        return 
    if not uid.reply_to_msg_id:
       await uid.edit("```Balas di Pesan Goblok!!.```")
       return
    message = await uid.get_reply_message() 
    chat = "@getidsbot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await uid.edit("```Balas di Pesan Goblok!!.```")
       return
    await uid.edit("```Membongkar ID..```")
    async with borg.conversation(chat) as conv:
          try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await uid.reply("`Bunuh @getidsbot dulu bos, biar botnya bisa jalan -_-`")
                return
          if response.text.startswith("Profil Buriq Tidak Punya ID,"):
             await uid.edit("```Profil Buriq Tidak Punya ID..```")
          await uid.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await uid.edit(f"{response.message}")
            await uid.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@getidsbot not responding!.`")


CMD_HELP.update({
    "get_uid":
    "`.gid`"
    "\nUsage: Reply in message to get user ID."
})
