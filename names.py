import os
import random

import discord

token = os.environ.get('DISCORD-TOKEN')
client = discord.Client()


def names():
    gender = random.choice(['boy', 'girl'])
    with open(f'txt_files/{gender}_title.txt') as title, open(f'txt_files/{gender}_first.txt') as first, open(
            f'txt_files/{gender}_last.txt') as last, open(
            f'txt_files/{gender}_last2.txt') \
            as last2:
        title = title.readlines()
        first = first.readlines()
        last = last.readlines()
        last2 = last2.readlines()

    t = random.choice(title).strip('\n')
    f = random.choice(first).strip('\n')
    l = random.choice(last).strip('\n')
    l2 = random.choice(last2).strip('\n')
    last = l + l2

    name = f'{t} {f} {last}'
    return name


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!name':
        response = f'{names()}'
        await message.channel.send(response)


client.run(token)
