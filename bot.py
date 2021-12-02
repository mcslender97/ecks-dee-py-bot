import os
import discord
import re
import pattern as p
from dotenv import load_dotenv
# load ./.env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
# Regex pattern for xd
# Look for regex pattern in message 

pattern = p.pattern

# pattern match: XD (case insensitive) 

@client.event
async def on_ready():
    for guild in client.guilds:

        if guild.name == GUILD: 
            break
# show guild name and id that is registered for the bot
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
# Read message, find xd and reply with ECKS DEE
@client.event
async def on_message(message):
    # don't reply to self
    if message.author == client.user:
        return
    # if message contains xd, reply with ECKS DEE
    if re.search(pattern, message.content, re.IGNORECASE): #(case insensitive)
        await message.channel.send('XD? You mean ECKS DEE right?')
        
 

client.run(TOKEN)