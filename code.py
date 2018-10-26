import discord
from discord.ext import commands
import asyncio
from itertools import cycle 


TOKEN = 'NDc4NzcyMjIzMjk4MjQwNTE0.Dq564A.AMZ5hwfG80TI81BbDGcqLGap0qs'

status = ["Sleeping", "Eating", "Gaming", "Anime Time", "Eating"]
bot = commands.Bot(command_prefix = '.')
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name="Maintenance"))
    print("MyBot, ready for action")

async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game = discord.Game(name = current_status))
        await asyncio.sleep(200)  

@bot.event 
async def on_message(message):
    print ("A user has sent a message")
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Test Role")
    await bot.add_roles(member, role)

@bot.event
async def on_message(message):
    msgContent = message.content.lower()
    if "yeet" in msgContent:
        await bot.send_message(message.channel, "Yah!")
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    msgContent = message.content.lower()
    if "yah" in msgContent:
        await bot.send_message(message.channel, "Yeet!")
    await bot.process_commands(message)

@bot.command()
async def echo(*args):
    output = " "
    for words in args:
        output += words
        output += " "
    await bot.say(output)

@bot.command(pass_context=True)
async def clear(ctx, amount = 100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages deleted")

@bot.command()
async def displayembed():
    myEmbed = discord.Embed(
        title = "Title",
        description = "This is a description",
        colour = discord.Colour.red()
    )
    
    myEmbed.set_footer(text="This is a footer")
    myEmbed.set_image(url="https://discordapp.com/assets/94db9c3c1eba8a38a1fcf4f223294185.png")
    myEmbed.set_thumbnail(url="https://discordapp.com/assets/f72fbed55baa5642d5a0348bab7d7226.png")
    myEmbed.set_author(name="Prodigy",
    icon_url="https://discordapp.com/assets/e05ead6e6ebc08df9291738d0aa6986d.png")
    myEmbed.add_field(name="Field Name", value="Field Value", inline=False)
    myEmbed.add_field(name="Field Name", value="Field Value", inline=True)
    myEmbed.add_field(name="Field Name", value="Field Value", inline=True)
    await bot.say(embed=myEmbed)  

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    helpEmbed = discord.Embed(
        colour = discord.Colour.orange()
    )

    helpEmbed.set_author(name="help")
    helpEmbed.set_field(
        name=".yeet", value= "Returns Yah!", inline=False
    )

    await bot.send_message(author, embed=helpEmbed)

bot.loop.create_task(change_status())
bot.run(TOKEN)

