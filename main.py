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
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(804569326296104961)
    await channel.send("blankbot has arrived")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('++introduce'):
        await message.channel.send('i am blank. well, at least a digital representation of him')

client.run(bot_token)
