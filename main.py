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
from nickname import nickn
from barney import Barney
from chandler import Chandler
from animequote import Animequote
from gif import Gif
import discord,asyncio,youtube_dl
import os
from dotenv import load_dotenv
from creepy import story
from dictionary import Dictionary

cg = CoinGeckoAPI()

client  = commands.Bot(command_prefix = 'kb$')

@client.event
async def on_ready():
    print("Bot is ready")


from dotenv import load_dotenv

load_dotenv()

exts=['music'] 


@client.event
async def on_ready():
    song_name='with All For One' 
    activity_type=discord.ActivityType.playing
    await client.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(client.user.name)

for i in exts:
    client.load_extension(i)



@client.event
async def on_member_join(member: discord.Member):
    def get_name():
        n_name = nickn()
        name_list = []
        name_list.append(n_name)
        return name_list
    x = get_name()
    a_set = set(x)
    contains_duplicates = len(x) != len(x)
    if (contains_duplicates == True):
        x.pop((-1))
        x = get_name()

    await member.edit(nick=x[-1])
    

@client.command()
async def words(ctx):
    embed = discord.Embed(title = 'WORDS OF WISDOM', color = discord.Colour.magenta())
    p = np.random.randint(3,size=1)
    q = p[0]

    if q==0:
        name = " - Barney Stinson"
        z = str(Barney()+name)
    elif q==1:
        name = " - chandler Bing"
        z = str(Chandler()+name)
    elif q==2:
        z = Animequote()

    embed.add_field(name = "Quote", value = z , inline=True)
    await ctx.send(embed = embed)

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
    # g = crypto_g(crypto,z)

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
async def wiki(ctx,*, subject):
    subject = subject.upper()
    em = discord.Embed(title = subject , color = discord.Colour.red())
    subject = subject.lower()
    await ctx.send(embed = em)

    y = wiki_info(subject)

    str_count = 0
    end_count=1999
    for i in range(int((len(y)/1999)+1)):
        if end_count > len(y):
            await ctx.send(y[str_count :])
            break
        await ctx.send(y[str_count : end_count]+'-')
        if end_count == len(y):
            break
        str_count +=1999
        end_count += 1999

    embed = discord.Embed(title = " " , color = discord.Colour.red())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

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
async def g(ctx, x, r = None):
    
    x = x.upper()
    embed = discord.Embed(title = x, color = discord.Colour.teal())
    x= x.lower()

    y = ctx.author.mention
    c = Gif(y, x)
    # file = discord.File(y+'.gif')
    # b = 'attachment://'+y+'.gif'
    # embed.set_image(url = b)
    if r == None:
        embed.add_field(name = "\u200b", value = y+" "+x, inline=True)
    else:
        embed.add_field(name = "\u200b", value = y+" "+x+" "+r, inline = True)
        

    embed.set_image(url = c)
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
async def creepy(ctx):
    s = story()
    story_title = str(s[0])
    story_content = str(s[1])
    embed = discord.Embed(title  = story_title, color = discord.Colour.dark_red())
    await ctx.send(embed = embed)
    
    str_count = 0
    end_count=1999
    for i in range(int((len(story_content)/1999)+1)):
        if end_count > len(story_content):
            await ctx.send(story_content[str_count :])
            break
        await ctx.send(story_content[str_count : end_count]+'-')
        if end_count == len(story_content):
            break
        str_count +=1999
        end_count += 1999


@client.command()
async def meaning(ctx, word):
    try:
        word = word.upper()
        embed = discord.Embed(title = word, color = discord.Colour.gold())
        word = word.lower()

        val = Dictionary(word)
        definition = val['list'][0]['definition']
        example = val['list'][0]['example']
        embed.add_field(name = "Meaning", value = definition, inline= False)
        embed.add_field(name = "Example", value = example, inline = True)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(title = "Error 404", color = discord.Colour.gold())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")        

        await ctx.send(embed=embed)

@client.command()
async def roll(ctx):
    p = np.random.randint(low = 1, high = 6,size=1)
    embed = discord.Embed(title = " ", color = discord.Colour.gold())
    embed.add_field(name = "Dice",
                    value = f"The number is **{p}**")
    
    await ctx.send(embed = embed)



@client.command()
async def delete(ctx,amount=2):
    await ctx.channel.purge(limit = amount)



client.run(<API-KEY> )
