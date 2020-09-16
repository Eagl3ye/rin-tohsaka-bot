import discord
from discord.ext import commands
import random
import os

class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command(name="baog", aliases=['infertile', 'deadballs', 'deadeggs'])
	async def baog(self, ctx):
		msg = ctx.message
		await ctx.send(content='<a:baoggif:746755743809667193>')
		await msg.delete()

	@commands.command(name="treasure", aliases=['chest', 'coins', 'box'])
	async def treasure(self, ctx):
		msg = ctx.message
		await ctx.send(content='https://cdn.discordapp.com/emojis/677420843076288522.gif?v=1')
		await msg.delete()

def setup(client):
	client.add_cog(Misc(client))
