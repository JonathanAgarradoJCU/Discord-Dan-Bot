import discord
import random

file = open('TOKEN.txt', 'r')
read = file.readline()

TOKEN = read

GREETING = ["hello", "hey", "hi", "whats up",
            "what's up", "kamusta", "heyo",
            "heyoo", "good day", "gday", "g'day",
            "hello!", "hey!", "hi!", "whats up!",
            "what's up!", "kamusta!", "heyo!",
            "heyoo!", "good day!", "gday!", "g'day!"]
FAREWELL = ["bye", "goodbye", "farewell",
            "auf weidersehen", "seeya", "see you"
            "bye!", "goodbye!", "farewell!",
            "auf weidersehen!", "seeya!", "see you!"]

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
        if user_message.lower() in GREETING:
            greeting_response = [f"What's up, {username}!",
                                 f"Hello, {username}!",
                                 f"{username}, hi there!",
                                 "What's cookin'!"]
            await message.channel.send(random.choice(greeting_response))
            return

        elif user_message.lower() in FAREWELL:
            farewell_response = [f'Going so soon, {username}? See you another time!',
                                 f'Aww, going already? Take care, {username}.',
                                 f'Hey {username}, have a good day!']
            await message.channel.send(random.choice(farewell_response))
            return

        elif user_message.lower() == '!random':
            response = f"This is your random number (0-100): {random.randrange(100)}"
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return


client.run(TOKEN)
