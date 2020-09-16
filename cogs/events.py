import discord
from discord.ext import commands
import random
import os

class Events(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.mudae_events_list = {
			"a":["UNLUCKY EVENT","Server-wide Thanos Snap"],																																									# 1%
			"b":["UNLUCKY EVENT","Force-divorce all firstmarries"],																																								# 6%
			"c":["UNLUCKY EVENT","Limit your harem to 50 for a week"],																																							# 8%
			"d":["UNLUCKY EVENT","Remove kakera 300 (All)"], 
			"e":["NEUTRAL EVENT","Reroll mudae events"],																																											# 14%
			"f":["UNLUCKY EVENT","Right to choose from the top 4 of $tsv the one who will receive __**Force-divorce random character**__ (200<:kakera:748810456671453296> - 499<:kakera:748810456671453296>)"], 				# 15%
			"g":["UNLUCKY EVENT","Thanos Snap (2 random players)"],																																								# 7%
			"h":["LUCKY EVENT","Earn 1x Trading Power (Random player)"],
			"i":["LUCKY EVENT","Earn 1000 kakera (Two random players)"],		
			}																																				# 4%
	#def mudae_release():
	#	letters = ['a','b','c','d','e','f','g','h','i','j','k']
	#	return letters[random.randint(0,len(container)-1)]

	@commands.command(name="mudae_event", aliases=['mevent', 'mevnt', 'mev'])
	@commands.has_guild_permissions(administrator=True)	
	async def mudae_event(self, ctx, mode=None, number=1):
		msg = ctx.message
		if mode is None or mode == "spawn":
			embed = discord.Embed(
				title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
				colour=discord.Colour.red()
				)
			if number > 4:
				number = 4
			if number < 1:
				number = 1
			for _ in range(number):
				choice = self.mudae_randomize()
				embed.add_field(name='📍| '+self.mudae_events_list[choice][0], value=self.mudae_events_list[choice][1], inline=False)

			await ctx.send(embed=embed)
		elif mode == "release":
			embed = discord.Embed(
				title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
				description='► The following randomly-picked events will be __**removed**__ for this week\'s mudae event:',
				colour=discord.Colour.from_rgb(255, 230, 230)
				)
			if number > 4:
				number = 4
			if number < 1:
				number = 1
			for _ in range(number):
				choice = self.mudae_randomize()
				embed.add_field(name=':outbox_tray:| '+self.mudae_events_list[choice][0], value=self.mudae_events_list[choice][1], inline=False)
			embed.set_footer(text='New events will be added later... stay tuned!')
			await ctx.send(embed=embed)
		await msg.delete()

	@commands.command(name="mudae_announce", aliases=['mann', 'manc'])
	@commands.has_guild_permissions(administrator=True)	
	async def mudae_announce(self, ctx, *, content:str):
		msg = ctx.message
		embed = discord.Embed(
			title=':heart_exclamation: **Mudae Event** :heart_exclamation:',
			description=content,
			colour=discord.Colour.red()
			)
		await ctx.send(embed=embed)
		await msg.delete()

	@commands.command(name="arena_event", aliases=['aevent', 'aevnt', 'aev'])
	@commands.has_guild_permissions(administrator=True)	
	async def arena_event(self, ctx):
		embed = discord.Embed(
			title=':trophy: **Arena Event** :trophy:',
			description='Hosted by: <@336068309789310979>',
			colour=discord.Colour.gold()
			)
		first = '<@!273035462996918273>\n10,000 Tatsumaki Credits | 10,000 IdleRPG Credits | 1000 kakera'
		second = '<@!487935377219256343>\n5,000 Tatsumaki Credits | 5,000 IdleRPG Credits | 500 kakera'
		third = '<@!523701663937200134>\n1,000 Tatsumaki Credits | 1,000 IdleRPG Credits | 100 Kakera'
		embed.add_field(name='Eligible to:', value='Mudae and IdleRPG players', inline=False)
		embed.add_field(name='Rewards and Winners:', value='-', inline=False)
		embed.add_field(name=':first_place: ', value=first, inline=True)
		embed.add_field(name=':second_place: ', value=second, inline=True)
		embed.add_field(name=':third_place: ', value=third, inline=True)
		embed.add_field(name='Score Tally:', value='https://controlc.com/6b6f4fab', inline=False)
		join = 'Use `$skills` and set the skills for each of your 6 waifus/husbandos to the following divisions:' 
		embed.add_field(name='How to join:', value=join, inline=False)
		embed.add_field(name=':small_orange_diamond:| +10 :crossed_swords: stats', value='Yandere Division', inline=True)
		embed.add_field(name=':small_orange_diamond:| +5 :crossed_swords: +5 :shield: stats', value='Tsundere Division', inline=True)
		embed.add_field(name=':small_orange_diamond:| +10 :shield: stats', value='Kuudere Division', inline=True)
		embed.add_field(name=':small_orange_diamond:| +8 :notebook_with_decorative_cover: stats', value='Dandere Division', inline=True)
		embed.add_field(name=':small_orange_diamond:| +40% :heartpulse: stats', value='Deredere Division', inline=True)
		embed.add_field(name=':small_orange_diamond:| Any stats', value='Combo Division', inline=True)	
		embed.add_field(name='Where:', value='<#745137728793870366>', inline=True)
		embed.set_footer(text='When: COMPLETED ~~Friday, Aug-28-2020, 9:00 PM Local Time~~')
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Events(client))

'''
 1% - Server-wide Thanos Snap
 5% - Earn 1x Trading Power (Random player)
 6% - Next event immunity (random player)
 7% - Force-divorce all firstmarries
 8% - Thanos Snap (2 random players)
 9% - Limit your harem to 50 for a week
12% - Earn 1000 kakera (Two random players)
13% - Remove kakera 300 (All)
13% - Reroll mudae events
13% - Right to choose from the top 4 of $tsv the one who will receive __**Force-divorce random character**__ (200<:kakera:748810456671453296> - 499<:kakera:748810456671453296>)
13% - Earn 1x Two lock-in rights during Thanos/Reset (3 random players)
'''