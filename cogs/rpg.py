import discord
from discord.ext import commands
import random
import os

class RPG(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == 555955826880413696 and message.channel.id == 755450243281190994:
			print(message.type)
	
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
	client.add_cog(RPG(client))
