import os
from discord import message
from discord.ext import commands
import random
import asyncio
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
    question_list = [["test question","choice 1","choice 2","choice 3(correct choice)", "choice 4", 2]]
    question_index = random.choice(question_list)
    user = ctx.author
    choice1 = question_index[1] 
    choice2 = question_index[2] 
    choice3 = question_index[3] 
    choice4 = question_index[4] 
    answer = question_index[5] 
    question = question_index[0]
    await ctx.send(f"""```{question} \n{choice1}\n{choice2}\n{choice3}\n{choice4}```""")
    try:
        msg = await client.wait_for(
           "message",
           timeout=10,
           check = lambda message: message.author == ctx.author
        )
        if msg:
            if int(msg.content) == answer:
                await ctx.send("Congrats you got it right, why not try another one!")
            else:
                await ctx.send(f"Better luck next time! The correct answer was {question_index[answer]}")
    except asyncio.TimeoutError:
        await ctx.send("bot timed out for your answer")
    
@client.command()
async def music(ctx):
    questions = [["test question","choice 1","choice 3(correct choice)", "choice 4", "3"]]
    await ctx.send(random.choice(questions)) 

client.run(os.getenv('TOKEN'))