import discord
import os
from msgs import slash_msg
from discord.ext import commands
from playground import froehlich


from Rols import role
# Load Variables from .env
from .env import loadEnv
loadEnv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    slash_msg()

    # mit discord.ext kann man laut denen so die hinzufügen
    bot.add_command(froehlich) 

        
client = MyClient()
client.run(os.getenv('TOKEN'))