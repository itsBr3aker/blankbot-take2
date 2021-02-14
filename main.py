import discord
import os
import requests
import json
from decouple import config
import datetime

bot_token = config('TOKEN')
# 'bot_token' will be populated with bot token in the hidden .env file

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is armed and ready'.format(client))
    channel = client.get_channel(804569326296104961)
    await channel.send("blankbot has arrived")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('_about'):
        await message.channel.send('i am blank. well, at least a digital representation of him')
    
    if message.content.startswith('_license')
        await message.channel.send('the code used for me is open-source, and is protected with the gnu gpl v3 license. you can view this on my github page under the ***LICENSE*** file')

client.run(bot_token)
