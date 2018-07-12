import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
print ("hi bro")

prefix = "n!"
Client = discord.Client()
client = commands.Bot(command_prefix = "n!")

@client.event
async def on_ready():
    print("Bot is online!")
    await client.change_presence(game=discord.Game(name=prefix+"help | in {} servers!".format(len(client.servers))))
    print (client.servers)

@client.command()
async def servers():
    await client.send_message(message.channel, "I'm in ``{}`` servers!".format(len(Client.servers)))

@client.event
async def on_message(message): 
    if message.author.bot:
        return
    if not message.content.lower().startswith(prefix):
        return
    command = message.content.lower()[len(prefix)::]
    userID = message.author.id

    if (command == "help") or (command == ""):
        embed=discord.Embed(title="**__Sparky's information:__**", color=0x42f4eb)
        embed.add_field(name="prefix: " + prefix , value="**__Commands:__**\n**Help** - commands list\n**say** - make me say something\n**servers** - in how many servers i am?\n**ping** - pong\n**pizza**\n**cookie**", inline=False)
        embed.set_footer(text="Sparky's creator: Nir11s")
        embed.add_field(name="**--------------**", value="[invite me](https://discordapp.com/api/oauth2/authorize?client_id=460552217422856222&permissions=8&scope=bot)\n[Support server](https://discord.gg/Sk9pUny)")

        await client.send_message(message.channel, embed=embed)
    #commands:
    if command == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if command == "pizza":
        await client.send_message(message.channel, ":pizza:")
    if command == "ping":
        await client.send_message (message.channel, "<@%s> pong!" % (userID))
    if command.startswith("say"):
        args = message.content.split(" ")
        try:
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, "**Command:** "+prefix+"say [something]")
    if(command == "servers"):
       await client.send_message(message.channel, "I'm in ``{}`` servers!".format(len(client.servers)))
    #ADMIN commands:
    if ctx.message.author.server_permissions.administrator:
        pass


client.run(os.getenv("TOKEN"))
