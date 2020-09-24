import discord
from discord.ext import commands
import requests
import numpy as np
from news import everything_news
import datetime
from graph import *
from pycoingecko import CoinGeckoAPI
from wiki import wiki_info
from toss import coinFlip, method
from weather import weather_res
from score_scrapper import score

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
async def weather(ctx, city, country):
    embed = discord.Embed(title = "WEATHER", color = discord.Colour.dark_green())
    city = str(city)
    country = str(country)
    json_data_2 = weather_res(city, country)
    weather_type = str(json_data_2['weather'][0]['main'])
    temperature = str(json_data_2['main']['temp']) + '°C'
    feel_like = str(json_data_2['main']['feels_like']) + '°C'
    min_temp = str(json_data_2['main']['temp_min']) + '°C'
    max_temp = str(json_data_2['main']['temp_max']) + ' °C'
    embed.add_field(name = "CATEGORY", value = weather_type, inline = False )
    embed.add_field(name = "TEMP", value = temperature, inline = True)
    embed.add_field(name = "FEELS LIKE", value = feel_like, inline = True)
    embed.add_field(name = "MIN_TEMP", value = min_temp, inline = True)
    embed.add_field(name = "MAX_TEMP", value = max_temp, inline = True)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)


@client.command()
async def fb(ctx, team_a, team_b):
    embed = discord.Embed(title = 'INFO', color = discord.Colour.from_rgb(0, 255, 255))
    team_a = str(team_a)
    team_b = str(team_b)
    result = score(team_a, team_b)
    embed.add_field(name = "status", value = result, inline = True)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)
 
@client.command()
async def delete(ctx,amount=2):
    await ctx.channel.purge(limit = amount)



client.run("NzUzOTgyNDk3ODQyMzk3MTk1.X1uG6w.4YZkwoz744yvNDlu1A2a1ZtEiqc")
