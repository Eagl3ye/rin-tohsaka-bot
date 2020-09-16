import discord
from discord.ext import commands
import os
import random
import asyncio

client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game("with the Events | r!help"))
	print('Logged on as')
	print(client.user.name)
	print(client.user.id)

client.load_extension("cogs.tools")
client.load_extension("cogs.events")
client.load_extension("cogs.utility")
client.run(os.environ['TOKEN'])