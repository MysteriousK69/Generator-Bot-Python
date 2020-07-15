import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
import string
from discord import Game


bot = commands.Bot(command_prefix='6!')

bot.remove_command('help')

blank = '** **'

_servers = [
    "432",
    "543",
    "439",
    "334",
    "392",
    "424",
    "923",
    "283",
    "932",
    "422",
    "522",
    "528",
    "342",
    "842"
]

servers = random.choice(_servers)

Game = [
    " 6!help for a list of commands",
    "Watching Aypro suck MKs dick while running  6!donate",
    "Consider donating 6! it encourages me and helps me keep the bot online, use the command  6!donate",
    f"Watching {servers} Servers do  6!help",
    "me is like  6!donate ;-;",
    "y u no donate ;-; use  6!donate or small pp",
    "6!donate or you are not floor gang",
    " 6!donate or micro pp"
]

gamePlaying = random.choice(Game)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(gamePlaying))

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def donate(ctx):
        embed = discord.Embed(title='Perks', description='Its great that you want to donate! it realy helps me to keep the bot running and also encourages me to add more accounts to the bot! by donating you can reduce your cooldown to 5 minutes or 5 seconds depending on how much you paid.')
        embed.add_field(name='Prices', value='For 5 minute cooldown donate $5, $10 for 5 second cooldown contact me @ MysteriousK#1476', inline=False)
        embed.add_field(name='How to donate', value='To donate you can use Bitcoin, USD Digital, Ethereum, Stellar, Bitcoin Cash', inline=False)
        embed.add_field(name='Just support', value='Even if you dont want cooldown reduced and just wanna help me out with any amount u can donate directly to my wallets :)', inline=False)
        embed.add_field(name='Wallets', value='the adresses for Bitcoin, USD Digital, Ethereum, Stellar, Bitcoin Cash are: 1E5dmmLA6t9hHokhEddPqsGhwWhsiRiVUA, 0xAeC46db4034D97ec511833A086E6a641dD931f17, 0xAeC46db4034D97ec511833A086E6a641dD931f17, GDCQAQ6B6QELDGO6RGFCTRQS6AXH5CVHXGXU4QL5D7JO5Y3QV24VA6TA, qqtze5gjqtuyuznhu5pfxw7qchvu6zacvuz03kcdvx respectively', inline=False)
        await ctx.send(embed=embed)
@bot.command(name='minecraft')
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def minecraft(ctx):
    with open('minecraft.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='spotify')
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def spotify(ctx):
    with open('spotify.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='nord')
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def nord(ctx):
    with open('nord.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='steam')
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def steam(ctx):
    with open('steam.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def blizzard(ctx):
        with open('blizzard.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def brazzers(ctx):
        with open('brazzers.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")


@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def crunchyroll(ctx):
        with open('crunchyroll.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")
@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def directtv(ctx):
        with open('direct.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command(name='disney+')
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def disney(ctx):
        with open('disney.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def express(ctx):
        with open('express.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def fortnite(ctx):
        with open('fortnite.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def hulu(ctx):
        with open('hulu.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def instagram(ctx):
        with open('instagram.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def onlyfans(ctx):
        with open('onlyfans.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def pornhub(ctx):
        with open('pornhub.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def rockstar(ctx):
        with open('rockstar.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def strong(ctx):
        with open('strong.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def surfeasy(ctx):
        with open('surfeasy.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def twitch(ctx):
        with open('twitch.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def valorant(ctx):
        with open('valorant.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def uplay(ctx):
        with open('uplay.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 21600, commands.BucketType.user)
async def xnxx(ctx):
        with open('xnxx.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                embed = discord.Embed(title='Your account', description=a)
                embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
                embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
                embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
                await ctx.author.send(embed=embed)
                await ctx.send("You account has been sent enjoy ^^")

@bot.command(name='nitro')
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def nitro(ctx):
    Ncode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    embed = discord.Embed(title='Your account', description=discord_url + Ncode)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
    await ctx.author.send(embed=embed)
    await ctx.send('Your nitro code has been sent, enjoy ^^')

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def amazon(ctx):
    Acode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    embed = discord.Embed(title='Your account', description=Acode)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
    await ctx.author.send(embed=embed)
    await ctx.send("You Amazon giftcard has been sent enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def mcwin10(ctx):
    Mcode = ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    embed = discord.Embed(title='Your account', description=Mcode)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
    await ctx.author.send(embed=embed)
    await ctx.send("Sent a win 10 minecraft code enjoy ^^")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def robux(ctx):
    Rcode = ('').join(random.choices(string.digits, k=10))
    embed = discord.Embed(title='Your account', description=Rcode)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
    await ctx.author.send(embed=embed)
    await ctx.send("Sent a robux code")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def steamkey(ctx):
    Scode = ('').join(random.choices(string.ascii_letters + string.digits, k=13))
    embed = discord.Embed(title='Your account', description=Scode)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
    await ctx.author.send(embed=embed)
    await ctx.send("A key has been sent")

@bot.command()
@commands.has_role('Free Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def gplay(ctx):
    try:
        Gcode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        embed = discord.Embed(title='Your account', description=Gcode)
        embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
        embed.add_field(name="**DM Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=False)
        embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128",)
        await ctx.author.send(embed=embed)
        await ctx.author.send(Gcode)
    except:
        print('Unknown error :(')


@bot.command(name='stock-vpn')
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock_vpn(ctx):
    embed = discord.Embed(title='All VPN Account That We Offer:', description=blank)
    embed.add_field(name="**Generate StrongVPN**", value="command:   6!strong" , inline=False)
    embed.add_field(name="**Generate SurfEasyVPN**", value="command:   6!surfeasy" , inline=False)
    embed.add_field(name='**Generate ExpressVPN**', value='command:   6!express', inline=False)
    embed.add_field(name="**Generate NordVPN**", value="command:   6!nord" , inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476 & Aypro's Hyper#2399", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)

@bot.command(name='stock-streaming')
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock_streaming(ctx):
    embed = discord.Embed(title='All Streaming Account That We Offer', description=blank)
    embed.add_field(name="**Generate PornHub**", value="command:   6!pornhub" , inline=False)
    embed.add_field(name="**Generate Spotify**", value="command:   6!spotify" , inline=False)
    embed.add_field(name="**Generate XNXX**", value="command:  6!xnxx" , inline=False)
    embed.add_field(name='**Generate Crunchyroll**', value='command:  6!crunchyroll', inline=False)
    embed.add_field(name='**Generate DirectTV**', value='command:  6!directtv', inline=False)
    embed.add_field(name='**Generate DisneyPlus**', value='command:  6!disney+', inline=False)
    embed.add_field(name='**Generate Brazzers**', value='command:  6!brazzers', inline=False)
    embed.add_field(name='**Generate Hulu**', value='command:  6!hulu', inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476 & Aypro's Hyper#2399", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)

@bot.command(name='stock-gaming')
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock_gaming(ctx):
    embed = discord.Embed(title='All Gaming Accounts That We Offer')
    embed.add_field(name='**Generate Blizzard**', value='command:  6!blizzard', inline=False)
    embed.add_field(name='**Generate Fortnite**', value='command:  6!fortnite', inline=False)
    embed.add_field(name="**Generate Minecraft**", value="command:  6!minecraft", inline=False)
    embed.add_field(name="**Generate uPlay**", value="command:  6!uplay" , inline=False)
    embed.add_field(name="**Generate Valorant**", value="command:  6!valorant" , inline=False)
    embed.add_field(name="**Generate Twitch**", value="command:  6!twitch" , inline=False)
    embed.add_field(name="**Generate Steam**", value="command:  6!steam", inline=False)
    embed.add_field(name="**Generate RockstarGames**", value="command:  6!rockstar" , inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476 & Aypro's Hyper#2399", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)

@bot.command(name='stock-other')
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock_others(ctx):
    embed= discord.Embed(title='Other Accounts That We Offer', descrpition=blank)
    embed.add_field(name='**Generate Instagram**', value='command:  6!instagram', inline=False)
    embed.add_field(name="**Generate OnlyFans**", value="command:  6!onlyfans" , inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476 & Aypro's Hyper#2399", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)

@bot.command(name='stock-giftcard')
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock_giftcard(ctx):
    embed = discord.Embed(title='All Giftcards That We Offer', description=blank)
    embed.add_field(name="**Generate Nitro(has a very less chance of getting a working one)**", value="command:  6!nitro", inline=False)
    embed.add_field(name="**Generate Amazon GiftCard(has a very less chance of getting a working one)**", value="command:  6!amazon", inline=False)
    embed.add_field(name="**Generate Minecraft Windows 10 Code(has a very less chance of getting a working one)**", value="command:  6!mcwin10", inline=False)
    embed.add_field(name="**Generate Steam Key(has a very less chance of getting a working one)**", value="command:  6!steamkey", inline=False)
    embed.add_field(name="**Generate Robux(has a very less chance of getting a working one)**", value="command:  6!robux", inline=False)
    embed.add_field(name="**Generate Google Play GiftCard(has a very less chance of getting a working one)**", value="command:  6!gplay", inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476 & Aypro's Hyper#2399", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title='All commands', description=blank)
    embed.add_field(name=' 6!stock', value=blank, inline=False)
    embed.add_field(name=' 6!stock-vpn', value=blank, inline=False)
    embed.add_field(name=' 6!stock-gaming', value=blank, inline=False)
    embed.add_field(name=' 6!stock-streaming', value=blank, inline=False)
    embed.add_field(name=' 6!stock-other', value=blank, inline=False)
    embed.add_field(name=' 6!stock-giftcard', value=blank, inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def stock(ctx):
    embed = discord.Embed(title="All stock for the bot 69420 Gen™", description=blank , color=0xff0000)
    embed.add_field(name='**Generate Blizzard**', value='command:  6!blizzard', inline=False)
    embed.add_field(name='**Generate Fortnite**', value='command:  6!fortnite', inline=False)
    embed.add_field(name="**Generate Minecraft**", value="command:  6!minecraft", inline=False)
    embed.add_field(name="**Generate uPlay**", value="command:  6!uplay" , inline=False)
    embed.add_field(name="**Generate Valorant**", value="command:  6!valorant" , inline=False)
    embed.add_field(name="**Generate Twitch**", value="command:  6!twitch" , inline=False)
    embed.add_field(name="**Generate Steam**", value="command:  6!steam", inline=False)
    embed.add_field(name="**Generate RockstarGames**", value="command:  6!rockstar" , inline=False)
    embed.add_field(name="**Generate StrongVPN**", value="command:  6!strong" , inline=False)
    embed.add_field(name="**Generate SurfEasyVPN**", value="command:  6!surfeasy" , inline=False)
    embed.add_field(name='**Generate ExpressVPN**', value='command:  6!express', inline=False)
    embed.add_field(name="**Generate NordVPN**", value="command:  6!nord" , inline=False)
    embed.add_field(name="**Generate PornHub**", value="command:  6!pornhub" , inline=False)
    embed.add_field(name="**Generate Spotify**", value="command:  6!spotify" , inline=False)
    embed.add_field(name="**Generate XNXX**", value="command:  6!xnxx" , inline=False)
    embed.add_field(name='**Generate Crunchyroll**', value='command:  6!crunchyroll', inline=False)
    embed.add_field(name='**Generate DirectTV**', value='command:  6!directtv', inline=False)
    embed.add_field(name='**Generate DisneyPlus**', value='command:  6!disney+', inline=False)
    embed.add_field(name='**Generate Brazzers**', value='command:  6!brazzers', inline=False)
    embed.add_field(name='**Generate Hulu**', value='command:  6!hulu', inline=False)
    embed.add_field(name="**Generate Nitro(has a very less chance of getting a working one)**", value="command:  6!nitro", inline=False)
    embed.add_field(name="**Generate Amazon GiftCard(has a very less chance of getting a working one)**", value="command:  6!amazon", inline=False)
    embed.add_field(name="**Generate Minecraft Windows 10 Code(has a very less chance of getting a working one)**", value="command:  6!mcwin10", inline=False)
    embed.add_field(name="**Generate Steam Key(has a very less chance of getting a working one)**", value="command:  6!steamkey", inline=False)
    embed.add_field(name="**Generate Robux(has a very less chance of getting a working one)**", value="command:  6!robux", inline=False)
    embed.add_field(name="**Generate Google Play GiftCard(has a very less chance of getting a working one)**", value="command:  6!gplay", inline=False)
    embed.add_field(name='**Generate Instagram**', value='command:  6!instagram', inline=False)
    embed.add_field(name="**Generate OnlyFans**", value="command:  6!onlyfans" , inline=False)
    embed.add_field(name='Join My Official Discord Server For Giveaways And More :)', value='https://discord.gg/j3exaAu', inline=False)
    embed.add_field(name="**DM The Dev To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/731554261783150682/62ca32edce8b70dd8b965eb42dd12658.png?size=128")
    await ctx.send(embed=embed)



bot.run('TOKEN')
