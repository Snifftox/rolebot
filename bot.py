import discord
import os
from slash-msg import slash
# Load Variables from .env
from .env import loadEnv
loadEnv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    

        
client = MyClient()
client.run('TOKEN')