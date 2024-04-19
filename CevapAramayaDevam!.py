from math import *
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'@{member.name} ! Bu bir hesap makinası. İşlemler: topla-çıkar-böl-çarp-kökal-kuvvetal. İki sayı giriniz. Boşluk bırakınız. Başında "/" kullanınız.')
    
@bot.command()
async def topla(ctx, a: int, b: int):
    message=ctx.message
    işlem=(a+b)
    await ctx.send(işlem)

@bot.command()
async def çıkar(ctx, a: int, b: int):
    message=ctx.message
    işlem=(a-b)
    await ctx.send(işlem)

@bot.command()
async def böl(ctx, a: int, b: int):
    message=ctx.message
    işlem=(a/b)
    await ctx.send(işlem)

@bot.command()
async def çarp(ctx, a: int, b: int):
    message=ctx.message
    işlem=(a*b)
    await ctx.send(işlem)

@bot.command()
async def kökal(ctx, a: int, b: int):
    message=ctx.message
    işlem = pow(a,1/b)
    await ctx.send(işlem)

@bot.command()
async def kökal(ctx, a: int, b: int):
    message=ctx.message
    işlem = pow(a,1/b)
    await ctx.send(işlem)
    
@bot.command()
async def üsal(ctx, a: int, b: int):
    message=ctx.message
    işlem = (a**b)
    await ctx.send(işlem)
    

bot.run("TOKEN")
