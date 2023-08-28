import discord
import os
from msgs import slash_msg
# Load Variables from .env
from .env import loadEnv
loadEnv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    slash_msg()

        
client = MyClient()
client.run(os.getenv('TOKEN'))