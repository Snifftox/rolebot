import os
import discord
import bot

# Janik's Command Spaß Box

@bot.slash_command(name = "Yeet", description = "Yeet a friend!")
async def yeet(ctx):
    await ctx.respond("") # Name yeets @name