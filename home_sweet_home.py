import discord
import random
from discord.ext import commands
from credits import bot_token_hsh
import asyncio

client = discord.Client()
token = bot_token_hsh
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

flag = True
things = ['восхитительный', 'самый охуенный', 'любимый', 'прекрасный', 'сасный', 'ещё и самый гейский гей. Это']


@bot.command(name="start")
async def members(ctx):
    global flag
    if flag:
        await ctx.send('Привет. Теперь каждые 24 часа я буду определять главного пидора дня на этом сервере.')
        await ctx.send('Ещё со мной скоро можно будет поиграть в камень-ножницы-бумага')
        members = []
        guild = ctx.guild
        for m in guild.members:
            members.append(m)
        member = random.choice(members)
        print(type(member))
        await ctx.send(f'А сегодняшний пидор дня - это {random.choice(things)} {member.mention}')
        flag = False
        while True:
            await asyncio.sleep(86400)
            members = []
            guild = ctx.guild
            for m in guild.members:
                members.append(m)
            member = random.choice(members)
            print(type(member))
            await ctx.send(f'А сегодняшний пидор дня - это {random.choice(things)} {member.mention}')


bot.run(token)
