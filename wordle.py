from discord.ext import commands
import discord
import datetime
import asyncio

time = datetime.datetime.now

bot = commands.Bot(command_prefix='!')

async def timer():
    await bot.wait_until_ready()
    channel = bot.get_channel(942552068269428816) 
    msg_sent = False

    while True:
        if time().hour == 00 and time().minute == 00:
         if not msg_sent:
          with open('words.txt', 'r') as f:
           read = f.readline()

           a_file = open("words.txt", "r")

           lines = a_file.readlines()
           a_file.close()

           del lines[0]

           new_file = open("words.txt", "w+")

           for line in lines:
            new_file.write(line)

           new_file.close()
           
           content = '@everyone'
           embed=discord.Embed(title='Todays Word Is (24/2/22)', color=0xfff700)
           embed.add_field(name='Word: ', value=read, inline=False)
           embed.set_footer(text='Made By NormalPerson#5421')
           await channel.send(content, embed=embed)
           msg_sent = True
      
        else:
                msg_sent = False

bot.loop.create_task(timer())
bot.run('')