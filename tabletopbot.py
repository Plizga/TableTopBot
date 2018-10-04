import discord
from random import randint
TOKEN = "meme"
client = discord.Client()

@client.event
async def on_message(message):
    """
    handles events involving messages.
    :param message: message submitted by user.
    """
    #Prevent bot from replying to itself
    if message.author == client.user:
        return
    #handles all !roll parameters
    if message.content.startswith('!roll'):
        strRoll = message.content.strip("!roll ")
        amount, die = strRoll.split("d", 1)
        rollSum = 0
        tupAddends = ()
        for i in range(int(amount)):
            newRoll = randint(1, int(die))
            tupAddends = tupAddends + (newRoll,)
            rollSum += newRoll

        strFinal = ""
        for i in range(len(tupAddends)):
            if i != len(tupAddends) - 1:
                strFinal += str(tupAddends[i]) + " + "
            else:
                strFinal += str(tupAddends[i]) + " "
        strFinal += "= {}"
        await client.send_message(message.channel, strFinal.format(rollSum))

@client.event
async def on_ready():
    """
    prints bot information to the console.
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)