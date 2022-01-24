""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/poocong/Pocong-Userbot/pocong/varshelper.txt)")


CMD_HELP.update({
    "pmpermit": f"**Plugin : **`pmpermit`\
        \n\n  •  **Syntax :** `.vars`\
        \n  •  **Function : **Untuk melihat daftar vars Pocong - Userbot."
})
