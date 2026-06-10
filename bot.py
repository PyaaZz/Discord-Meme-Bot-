import discord
from discord import app_commands
import requests
import random

def get_meme():
    try:
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()
        return data["url"]
    except:
        return "Couldn't fetch a meme 😢"


def get_dog():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        return data["message"]
    except:
        return "Couldn't fetch a dog 😢"


def get_cat():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        return data[0]["url"]
    except:
        return "Couldn't fetch a cat 😢"


def get_fact():
    try:
        response = requests.get(
            "https://uselessfacts.jsph.pl/random.json?language=en"
        )
        data = response.json()
        return data["text"]
    except:
        return "Couldn't fetch a fact 😢"

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=1396492132520300645)
        self.tree.copy_global_to(guild=guild)
        synced = await self.tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s)")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())

        elif message.content.startswith("$dog"):
            await message.channel.send(get_dog())

        elif message.content.startswith("$cat"):
            await message.channel.send(get_cat())

        elif message.content.startswith("$fact"):
            await message.channel.send(get_fact())

        elif message.content.startswith("$coinflip"):
            await message.channel.send(
                random.choice(["🪙 Heads", "🪙 Tails"])
            )

        elif message.content.startswith("$ping"):
            await message.channel.send("🏓 Pong!")

        elif message.content.startswith("$help"):
            await message.channel.send(
                """
**Commands**

$meme - Random meme
$dog - Random dog image
$cat - Random cat image
$fact - Random fact
$coinflip - Flip a coin
$ping - Check if bot is online
$help - Show commands

Slash Commands:
/meme - Random meme
"""
            )

client = MyClient()

@client.tree.command(
    name="meme",
    description="Get a random meme"
)
async def meme(interaction: discord.Interaction):
    await interaction.response.send_message(get_meme())

client.run('YOUR_BOT_TOKEN_HERE') 
