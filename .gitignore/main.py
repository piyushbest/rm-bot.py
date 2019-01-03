import discord
from discord.ext import commands
import time

description = '''A Bot Made By Rudraksh Mehra'''

bot=commands.Bot(command_prefix="R")

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('~')

@bot.command()
async def ping():
	"""is the bot online?"""
	await bot.say('ping_pong')
	await bot.say('You pinged me haha')

@bot.command(pass_context=True)
async def kick(ctx, User:discord.Member):
	"""kick's a member"""
	await bot.kick(User)

@bot.command()
async def lol():
	"""says lol...."""
	await bot.say('lolololololololol')
	
@bot.command()
async def xD():
	"""says joy"""
	await bot.say(':joy:"')
	
@bot.command()
async def spam():
	"""Spam's WARNING!=use at your own risk"""
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')
	await bot.say('lol')

bot.run('Token')