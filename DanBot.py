import discord
import random

TOKEN =  # TODO: Replace this text here with your Discord token.

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == '!hello':
            await message.channel.send(f"What's up, {username}!")
            return
        elif user_message.lower() == '!bye' and 'bye':
            await message.channel.send(f'Going so soon, {username}? See you another time!')
            return
        elif user_message.lower() == '!random':
            response = f"This is your random number: {random.randrange(100)}"
            await message.channel.send(response)
            return
        elif user_message.lower() == 'pow':
            await message.channel.send('who the hell is Pow? i bet he is handsome as fuck')
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return


client.run(TOKEN)
