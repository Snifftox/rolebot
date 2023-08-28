import discord
from bot import client

async def present_msg(message,command,commandout):
    if message.channel.send(str(command)):
        await message.channel.send(str(commandout))
        

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send("""
                                   $help Role
                                   $help Slash
                                   $help Reaction
                                   $help Automeme
                                   
                                   """)
    present_msg(message,"$Slash","With Slash")