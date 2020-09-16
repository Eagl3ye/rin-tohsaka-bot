import discord
from discord.ext import commands
import random
import os

class Utility(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="rules")
	@commands.has_guild_permissions(administrator=True)
	async def rules(self, ctx):
		msg = ctx.message
		rules = [
			'**1** ►   Same rules as any righteous groups or servers.',
			'**2** ►   Please be respectful towards everyone. This means __**NO HATE**__ and whatever variant of this rule applies.',
			'**3** ►   No self-promotion without admin permission.',
			'**4** ►   Yeah have fun.'
		]
		flatrules = ''
		for rule in rules:
			flatrules += rule + '\n\n'
		embed = discord.Embed(
			title=':round_pushpin: **SERVER RULES** :round_pushpin:\n',
			description=flatrules,
			colour=discord.Colour.from_rgb(102, 255, 153)
			)
		await ctx.send(embed=embed)
		await msg.delete()

	@commands.command(name="campus")
	@commands.has_guild_permissions(administrator=True)
	async def campus(self, ctx):
		msg = ctx.message
		description = '► Assign yourself a role by reacting to the specified emoji based on your campus.\n\n'
		reacts = [
			':white_circle:',':black_circle:',':red_circle:',
			':blue_circle:',':brown_circle:',':purple_circle:',
			':green_circle:',':yellow_circle:',':orange_circle:',
			':white_large_square:',':black_large_square:',':orange_square:',
			':blue_square:',':red_square:',':brown_square:',
			'\u200b',':purple_square:','\u200b'
		]
		roles = [
			'IRC','CLC','EVC',
			'CVisC','CVC','WVC',
			'MRC','MC','CBZRC',
			'ZPRC','CARC','CMC',
			'CRC','SMC','BRC',
			'\u200b','SRC','\u200b'
		]
		embed = discord.Embed(
			title=':round_pushpin: **ROLE MENU: Campus** :round_pushpin:\n',
			description=description,
			colour=discord.Colour.from_rgb(102, 255, 153)
			)
		for react, role in zip(reacts, roles):
			embed.add_field(name=react+' **'+role+'**', value='\u200b', inline=True)
		await ctx.send(embed=embed)
		await msg.delete()


	@commands.command(name="announce")
	@commands.has_guild_permissions(administrator=True)
	async def announce(self, ctx, color_r=0, color_g=0, color_b=0, *, content:str):
		msg = ctx.message
		embed = discord.Embed(
			title=':round_pushpin: **ANNOUNCEMENT** :round_pushpin:\n',
			description=content,
			colour=discord.Colour.from_rgb(color_r, color_g, color_b)
			)
		await ctx.send(embed=embed)
		await msg.delete()
'''
	@commands.command(name="setagree", aliases=['agreezone', 'uni', 'u'])
	@commands.has_guild_permissions(administrator=True)
	async def setagree(self, ctx, color_r=0, color_g=0, color_b=0, *, content:str):
		msg = ctx.message
		content = content.split("|")
		title = (content[0]).strip()
		embed = discord.Embed(
			title=(content[0]).strip(),
			description=(content[1]).strip(),
			colour=discord.Colour.from_rgb(color_r, color_g, color_b)
			)
		await ctx.send(embed=embed)
		await msg.delete()

	def compareChannelID(self, channelid):
		ret_value = False
		if int(os.environ['AGREEMENT_CHID']) == 0:
			print("Command: Aggreement | AGREEMENT_CHID is empty")
			ret_value = False
		else:
			ret_value = channelid == os.environ['AGREEMENT_CHID']
			print("Command: Aggreement | AGREEMENT_CHID and the target channel is " + str(ret_value))
		return ret_value

	@commands.Cog.listener()
	async def on_message(self, message):
		msg = message
		if (message.content).lower() in ["i accept","accept"] and self.compareChannelID(message.channel.id):
			print("ACCEPTED!")
			print(message.content)
		await msg.delete()
'''

def setup(client):
	client.add_cog(Utility(client))
