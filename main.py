import os
import discord
from discord.ext import commands
import random
import asyncio
from dotenv import load_dotenv
from PIL import Image
import numpy as np


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
    question_list = [
        [
            "What is the holi festival otherwise known as?",
            "Festival of doves",
            "Festival of colors",
            "Festival of victory",
            "Festival of love",
            2
        ],
        [
            "The holi festival marks the beginning of which season?",
            "Summer",
            "Spring",
            "Winter",
            "Autumn",
            2
        ],
        [
            "Besides India, what other country **primarily** celebrates Holi?",
            "Australia",
            "Canada",
            "Nepal",
            "Switzerland",
            3
        ],
        [
            "What Hindu month is holi celebrated within?",
            "Magha",
            "Baisakh",
            "Phalguna",
            "Pausa",
            3
        ],
        [
            "In sikhism what is holi known as?",
            "Baisakhi",
            "Hola Mohalla",
            "Bandi Chor Diwas",
            "Maghi",
            2
        ],
        [
            "What significance is there for the Holi festival in jainism?",
            "Cultural significance",
            "Religious significance",
            "No major significance",
            "None of the above",
            3
        ],
        [
            "What day is “choti holi”?",
            "Before the day of Holi",
            "After the day of Holi",
            "Same day as Holi",
            "None of the above",
            1
        ],
        [
            "What hindu demon was burnt which lead to the celebration of Holi?",
            "Malika",
            "Jarika",
            "Holika",
            "Heelika",
            3
        ],
        [
            "Holika is the sister of which demon king in hindu lore?",
            "Ravansura",
            "Vibhishana",
            "Kumbhakarna",
            "Hiranyakashyapa",
            2
        ],
        [
            "What is religious music referred to in Sikhism?",
            "Kirtan ",
            "Pooja",
            "Sangeet",
            "None of the above",
            1
        ],
        [
            "The story behind the festival in hindu culture is related to….?",
            "Demon holika and prahlad",
            "Shiv and parvati",
            "Radha and Krishna",
            "Ram and Sita",
            1
        ],
        [
            "Which of the following is NOT  a common holi color",
            "Black",
            "Red",
            "Green",
            "Pink",
            1
        ],
        [
            "Lathmaar holi, which is a pre-holi celebration, is often celebrated in which of the following cities?",
            "Chennai",
            "Jaipur",
            "Mathura",
            "Delhi",
            1
        ],
        [
            "Why did Prahlad’s father, the evil king Hiranyakashipu plan to kill his son?",
            "Because he worshipped someone else instead of him",
            "Because he betrayed his father",
            "Because he was an illegitimate son",
            "None of the above",
            1
        ],
        [
            "Who did Prahald worship instead of his father?",
            "Lord Vishnu",
            "Lord Shiva",
            "Lord Krishna",
            "Lord Brahma",
            1
        ],
        [
            "Why do hindu, sikhs, jains, and other cultures light fire on holi?",
            "To signify the triumph of good over evil",
            "To indicate that holi starts a new year",
            "As a method of worshipping their god",
            "To eliminate any bad omens",
            1
        ],
        [
            "What is NOT an eco-friendly way of celebrating holi?",
            "Using natural, homemade colors",
            "Using balloons and plastic bags",
            "Using eco-friendly disposables for sweets and food",
            "Reducing the usage of water colors",
            2
        ],
        [
            "What flowers are NOT primarily used to make traditional, holi colors?",
            "Turmeric",
            "Indigo",
            "Bilva",
            "None of the above",
            4
        ],
        [
            "Gulaal, which is classified as the various holi colors, is also known as?",
            "Abir",
            "Dharir",
            "Vihir",
            "Sihir",
            1
        ],
        [
            "What desert is popular during the time of holi?",
            "Kulfi",
            "Gulab Jamun",
            "Ice Cream",
            "Gajar Halwa",
            1
        ]
    ]
    question_index = random.choice(question_list)
    user = ctx.author
    choice1 = question_index[1] 
    choice2 = question_index[2] 
    choice3 = question_index[3] 
    choice4 = question_index[4] 
    answer = question_index[5]
    question = question_index[0]
    await ctx.send(f"""```{question} \n\t1. {choice1}\n\t2. {choice2}\n\t3. {choice3}\n\t4. {choice4}```""")
    
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
async def color(ctx):
    filename = "tempavatar.png"
    await ctx.author.avatar_url.save(filename)
    
    forground = Image.open("For.png").convert("RGBA")

    avatar = Image.open("tempavatar.png").convert("RGBA")
    avatar.paste(forground, (0,0), forground)
    avatar.save('final.png',"PNG")
    
    file = discord.File(fp="final.png")
    await ctx.send(file=file)


client.run(os.getenv('TOKEN'))