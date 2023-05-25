import discord
from discord.ext import commands
import random
import os
print(os.listdir('animal'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def animals(ctx):
    
    images = os.listdir('animal') 
    img_name = random.choice(images)
    
    with open(f'animal/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTEwNDY3MzcxOTI2MTA3MzUwOA.G97sVE.77S6vKgLQl53plIC6ktxdju8ns9jjHYD7OYp58")
