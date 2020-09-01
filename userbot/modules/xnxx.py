from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot


@register(outgoing=True, pattern=r"^\.o(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    wall = f"wall"
    await event.edit("```Processing```")
    async with bot.conversation("@xbotgroup_xbot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1281618755))
            await conv.send_message(f'/{wall} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @xbotgroup_xbot plox```")
            return
        if response.text.startswith("Hi"):
            await walpe.edit("`Please do /start` @xbotgroup_xbot`...`")
        else:
            downloaded_file_name = await event.client.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            try:
                msg_query
            except NameError:
                await event.client.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_query.id]
                )
    await event.delete()
    return os.remove(downloaded_file_name)
