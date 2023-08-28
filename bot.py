# bot.py
#pip install python-decouple
#pip install discord
import os
from decouple import config
import discord

# Load Variables from .env
from .env import loadEnv
loadEnv()

bot = discord.Bot()

TOKEN = os.getenv('DISORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
