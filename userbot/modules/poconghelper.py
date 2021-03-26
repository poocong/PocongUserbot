""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.poconghelp$")
async def usit(e):
    await e.edit(
        f"**Hai tuan {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/bismillahselaluadaa)"
        "\n[Repo](https://github.com/ilham77mansiz/tuan-Userbotilham)"
        "\n[Instagram](Instagram.com/imansiezz_)")


@register(outgoing=True, pattern="^.pocongvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ilham77mansiz/Lord-Userbot/Lord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "poconghelper":
    "`.poconghelp`\
\nUsage: Bantuan Untuk tuan-Userbot.\
\n`.pocongvar`\
\nUsage: Melihat Daftar Vars."
})
