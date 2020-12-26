import discord
import os
import requests
import json

client = discord.Client()

def getquote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Bot has started as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prefix = '*'    
    msg = message.content
    quote = getquote()

    if msg.startswith(prefix + 'hello'):
        await message.channel.send('Ahhhhh')
    elif msg.startswith(prefix + 'flush'):
        await message.channel.send('All the snakes you produces are flushed down')
    elif msg.startswith(prefix + 'pressure'):
        await message.channel.send(quote)
    elif msg.startswith(prefix + 'help'):
        await message.channel.send('Hello there!, it is the international toilet bot for help:')

client.run('NzkxMTcxNDcwNTk5OTEzNDky.X-LR2Q.EzeECZbGiZah5iDr2G3bz1lWyXk')