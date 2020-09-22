import discord
from discord.ext import commands
import requests
import numpy as np
from news import everything_news
import datetime
from crypto_graph import *
from pycoingecko import CoinGeckoAPI
from wiki import wiki_info
from Toss import coinFlip, method

cg = CoinGeckoAPI()

client  = commands.Bot(command_prefix = 'kb$')

@client.event
async def on_ready():
    print("Bot is ready")

    
@client.command()
async def news(ctx,arg):
    embed = discord.Embed(title = "HEADLINES" , color = discord.Colour.green())
    arg = str(arg)
    x = everything_news(arg)
    upper_case = arg.upper()
    embed.add_field(name = upper_case, value = x, inline = True )
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

    
@client.command()
async def cprice(ctx, crypto):
    crypto = crypto.upper()
    embed = discord.Embed(title = crypto , color = discord.Colour.dark_blue())
    crypto = crypto.lower()
    x = cg.get_price(ids= crypto, vs_currencies='usd,eur,inr', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    usd = str(x[crypto]['usd'])+' USD'
    eur = str(x[crypto]['eur'])+' EUR'
    inr = str(x[crypto]['inr'])+' INR'

    usd_market_cap = str(x[crypto]['usd_market_cap'])+' USD'
    usd_24h_vol = str(x[crypto]['usd_24h_vol'])+' USD'
    usd_24h_change = str(x[crypto]['usd_24h_change'])+' USD'
    z = ctx.author.name
    g = crypto_g(crypto,z)

    embed.add_field(name = "USD", value = usd, inline = True )
    embed.add_field(name = "EUR", value= eur, inline = True)
    embed.add_field(name = "INR", value= inr, inline = True)
    embed.add_field(name = "MARKET CAP", value= usd_market_cap, inline = True)
    embed.add_field(name = "24H VOL", value= usd_24h_vol, inline = True)
    embed.add_field(name = "24H CHANGE", value= usd_24h_change, inline = True)
    embed.set_image(url=g)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

    
@client.command()
async def wiki(ctx, subject):
    embed = discord.Embed(title = " " , color = discord.Colour.red())
    y = wiki_info(subject)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(x)
    await ctx.send(embed = embed)
    
    
@client.command()
async def toss(ctx, member: discord.Member):
    d = {}
    probability = .5
    side = np.random.binomial(1,probability)
    if (side == 1):
        x = 0
    else:
        x = 1

    d.update({ctx.author.name:1,member.name:0})
    t =coinFlip()
    w = method(d,t)
    res = f"{w} is the winner"
    embed = discord.Embed(title = "TOSS" , color = discord.Colour.dark_orange())
    embed.add_field(name = 'RESULT' , value = res , inline = False)
    await ctx.send(embed=embed)

    
@client.command()
async def delete(ctx,amount=2):
    await ctx.channel.purge(limit = amount)



client.run(<ID>)
