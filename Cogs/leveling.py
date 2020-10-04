import discord
from discord.ext import commands
import json

class leveling(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open('users.json', 'r', encoding='utf8') as f:
            user = json.load(f)
            
        try:
            with open('users.json', 'w', encoding='utf8') as f:
                user[str(message.author.id)]['xp'] = user[str(message.author.id)]['xp'] + 1
                lvl_start = user[str(message.author.id)]['level']
                lvl_end = user[str(message.author.id)]['xp'] ** (1.5/4)
                if lvl_start < lvl_end:
                    user[str(message.author.id)]['level'] = user[str(message.author.id)]['level'] + 1
                    await message.channel.send(f"oh, {message.author.id} has level up to {lvl}")
                    json.dump(user, f, sort_keys= True, indent=4, ensure_ascii= False)
                    return
                json.dump(user, f, sort_keys= True, indent=4, ensure_ascii= False)    
        except:
            with open('users.json', 'w', encoding='utf8') as f:
                user = {}
                user[str(message.author.id)] = {}
                user[str(message.author.id)]['level'] = 0
                user[str(message.author.id)]['xp'] = 0
                json.dump(user,f, sort_keys=True, indent = 4, ensure_ascii=False)


def setup(client):
    client.add_cog(leveling(client))