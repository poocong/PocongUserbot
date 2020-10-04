from pyrogram import Client, filters

goblok = Client("my_account")


@goblok.on_message(filters.private)
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")


goblok.run()
