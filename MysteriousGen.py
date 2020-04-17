import random
import discord
from discord.ext import commands
from discord.ext.commands import bot

print("Getting ready to give some accounts to noobs")

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.command(name='minecraft')
@commands.has_role('Gen Access')
@commands.cooldown(1, 3600, commands.BucketType.user)
async def minecraft(ctx, content):
	with open('minecraft.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")
                print("1" + content + "has been sent")

@bot.command(name='spotify')
@commands.has_role('Gen Access')
@commands.cooldown(1, 3600, commands.BucketType.user)
async def spotify(ctx,content):
	with open('spotify.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")
                print("1" + content + "has been sent")

@bot.command(name='nord')
@commands.has_role('Gen Access')
@commands.cooldown(1, 3600, commands.BucketType.user)
async def nord(ctx, content):
	with open('nord.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")
                print("1" + content + "has been sent")

@bot.command(name='steam')
@commands.has_role('Gen Access')
@commands.cooldown(1, 3600, commands.BucketType.user)
async def steam(ctx, content):
	with open('steam.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")
                print("1" + content + "has been sent")


@bot.command(name="stock")
async def stock():
        embed = discord.Embed(title="Current stock:", color=0xeee657)
        embed.add_field(name="nord",value="nord",inline=False)
        embed.add_field(name="minecraft",value="minecraft",inline=False)
        embed.add_field(name="spotify",value="spotify",inline=False)
        embed.add_field(name="steam",value="steam",inline=False)
        embed.add_field(name="Prefix:",value="!",inline=False)
        print("A user has checked the stock")





bot.run('Njc3NjExNDQzMDYyOTY0Mjk2.XoImng.BAZMunA-2eu-Qcwdoq2hSGk-GXU')