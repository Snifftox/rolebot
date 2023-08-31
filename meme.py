import bot
from bot import client


@bot.slash_command(name = "meme", description = "post a meme")
async def image():
    NotImplemented