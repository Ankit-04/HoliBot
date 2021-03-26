import os
from discord.ext import commands
import random
from dotenv import load_dotenv


load_dotenv()
client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print(f'{client.user} is connected')

@client.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author}, im holi bot, i have three commands; triva, music, color")

@client.command(aliases = ['t','Triva'])
async def triva(ctx):
    questions = [["test question","choice 1","choice 3(correct choice)", "choice 4", "3"]]
    await ctx.send(random.choice(questions)) 

@client.command(aliases = ['t','Triva'])
async def triva(ctx):
    questions = [["test question","choice 1","choice 3(correct choice)", "choice 4", "3"]]
    await ctx.send(random.choice(questions)) 
    
@client.command(aliases = ['t','Triva'])
async def triva(ctx):
    questions = [["test question","choice 1","choice 3(correct choice)", "choice 4", "3"]]
    await ctx.send(random.choice(questions)) 

client.run(os.getenv('TOKEN'))