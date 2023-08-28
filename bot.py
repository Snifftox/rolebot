import discord
import os

# Load Variables from .env
from .env import loadEnv
loadEnv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = TOKEN = os.getenv('DISORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    @client.event
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        
client = MyClient()
client.run('TOKEN')