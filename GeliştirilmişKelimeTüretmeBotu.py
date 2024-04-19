from kelimetüretme import kelimetüret
import discord
from discord.ext import commands
ma=0

kullanıcılar={"o":9999,
       "noob":0}

def finduserscore(u):
    if u in kullanıcılar.keys():
        return kullanıcılar[u]
    else:
        return "Böyle bir kullanıcı yok"
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def t(ctx):
    message=ctx.message
    if message.author not in kullanıcılar.keys():
        kullanıcılar.update({message.author : 0})


    kel=message.content.replace("/t ", "")
    ml=kelimetüret(message.author,kel,finduserscore(message.author))
    kullanıcılar.update({message.author:ml[1]})
    print(kel)
    print(ml[1])
    await ctx.send(f'{ml[0]}')

@bot.command()
async def score(ctx):
    message=ctx.message
    if message.author not in kullanıcılar.keys():
        kullanıcılar.update({message.author : 0})
    aranan=message.content.replace("/score ", "")
    await ctx.send(f"{aranan}'ın Skoru: {kullanıcılar[aranan]}")
@bot.command()
async def myscore(ctx):
    message=ctx.message
    if message.author not in kullanıcılar.keys():
        kullanıcılar.update({message.author : 0})
    await ctx.send(f"Skorunuz: {kullanıcılar[message.author]}")
@bot.command()
async def globalscore(ctx):
    message=ctx.message
    if message.author not in kullanıcılar.keys():
        kullanıcılar.update({message.author : 0})
    scorelist=[]
    scoredict={}
    for u, score in kullanıcılar.items():
        while score in scoredict:
            score+=0.00000000000000000000000000001
            print(kullanıcılar.items())
        scorelist.append(score)
        scoredict.update({score:u})
    print(scorelist)
    sortedusers=[]
    sortedscores = sorted(scorelist, reverse=True)

    for i in range(10):
        if i < len(sortedscores):
            sortedusers.append(scoredict[(sortedscores[i])])

    print(sortedusers)
    print(sortedscores)
    leaderboard=""
    for a in range(len(sortedusers)):
        leaderboard+=f"\n{a+1}.  -  {sortedusers[a]}  :  {round(sortedscores[a])}"
    await ctx.send(leaderboard)

bot.run(TOKEN")
