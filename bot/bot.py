import discord
import configparser

config = configparser.ConfigParser()
config.read('keys.ini')

TOKEN = (f'{config["KEY"]["key"]}')
client = discord.Client()


@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'what is the price of bitcoin':
            await message.channel.send(f'I dunno {username}.')
            return
        elif user_message.lower() == 'what is the price of ethereum':
            await message.channel.send(f'I dunno {username}.')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Goodbye {username}.')
            return




client.run(TOKEN)
