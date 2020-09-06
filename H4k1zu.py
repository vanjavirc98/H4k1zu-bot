#-----------------------------------------------------------------------------------------------------------
#SOURCE CODE

#https://github.com/Cryp70m4n/H4k1zu-bot-Code

#Made by Cryp70m4n


#FULL GUIDE ON HOW TO SETUP AND USE BOT IS IN 

#This bot is made for fun not damage so if you do any damage to anyone you take 100% responsibility
#-----------------------------------------------------------------------------------------------------------
#IMPORTS
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import time
import random
import requests
from termcolor import colored
from itertools import cycle
import os
#-----------------------------------------------------------------------------------------------------------
#INFO ABOUT BOT
banner_info = open("bot_info.txt", "r") #<------ Your path to bot_info.txt here with / instead of \
banner_info_open=(banner_info.read())
print(colored(banner_info_open, "red"))
time.sleep(5)
#clear console after loading bot info
#LINUX or MAC
#os.system("clear") #<------Uncomment this line if you using Linux or Mac


#WINDOWS
#os.system("cls") #<------Uncomment this line if you using Windows


#-----------------------------------------------------------------------------------------------------------
#BANNER LOAD
banner = open("banner.txt", "r") #<------ Your path to banner.txt here with / instead of \
banner_open=(banner.read())


#-----------------------------------------------------------------------------------------------------------
#INPUTS
print(colored(banner_open, "green"))
choosen_prefix=input(colored("Enter prefix:", "green"))
token=input(colored("Enter token:", "green"))
owner_id=int(input(colored("Enter your discord ID:", "green")))
time.sleep(1)


#clear console after loading banner, enetering prefix, token and ID.
#LINUX or MAC
#os.system("clear") #<------Uncomment this line if you using Linux or Mac


#WINDOWS
#os.system("cls") #<------Uncomment this line if you using Windows
#-----------------------------------------------------------------------------------------------------------
#SETUP STUFF

#print banner again
print(colored(banner_open, "green"))

#user is me
def user_is_me(ctx):
    return ctx.author.id == owner_id



#prefix
bot = commands.Bot(command_prefix = choosen_prefix)

#Errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":regional_indicator_x: You are missing an **required argument**. :regional_indicator_x:", delete_after=3)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":regional_indicator_x: You **can't** use that command. :regional_indicator_x:", delete_after=3)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(":regional_indicator_x: That command **doesn't** exist. :regional_indicator_x:", delete_after=3)
    if isinstance(error, commands.BadArgument):
        await ctx.send(":regional_indicator_x: Your argument is **not valid**. :regional_indicator_x:", delete_after=3)
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send(":regional_indicator_x: This command **doesn't** work in DMs. :regional_indicator_x:", delete_after=3)



#status change cycle
status = cycle([
       "H4k1zu.",
       "Cryp70m4n.",
       "Cryp70.",
       "Spamm."])
@tasks.loop(seconds=1)
async def change_presence():
    await bot.change_presence(activity=discord.Game(next(status)))



#bot start
@bot.event
async def on_ready():
    change_presence.start()
    print(colored("Bot is ready!", "yellow"))
    print(colored("Made by:Cryp70m4n", "green"))
    print(colored("Visit my github for source-code:https://github.com/Cryp70m4n/H4k1zu-bot-Code", "green"))
    print(colored("This bot is made for fun not damage so if you do any damage to anyone you take all of the responsibility", "red"))


#-----------------------------------------------------------------------------------------------------------
#COMMANDS

#spamming message "Spamm"
@bot.command()
@commands.check(user_is_me)
async def spam(ctx):
    while True:
        await ctx.send("Spam")



#spamm @everyone in channel
@bot.command()
@commands.check(user_is_me)
async def everyone_server_spam(ctx):
    while True:
        await ctx.send("@everyone")



#channel creating spamm
@bot.command()
@commands.check(user_is_me)
async def channel_spam(ctx):
  while True:
    guild = ctx.message.guild
    await guild.create_text_channel('Cry70m4n')
    await guild.create_voice_channel('H4k1zu channel')


#dm spamm mentioned user
@bot.command()
@commands.check(user_is_me)
async def dm_spam(ctx, user_id=None, *, args=None):
  while True:
      if user_id != None and args != None:
          try:
              target = await bot.fetch_user(user_id)
              await target.send(args)

              await ctx.send("'" + args + "' sent to: " + target.name)

          except:
              await ctx.send("Couldn't dm the given user.")


      else:
          await ctx.send("You didn't provide a user's id and/or a message.")




#dm spamm everyone from server
@bot.command()
@commands.check(user_is_me)
async def dm_all_spam(ctx, *, args=None):
    while True:
      if args != None:
          members = ctx.guild.members
          for member in members:
              try:
                  await member.send(args)
                  ctx.send("'" + args + "' sent to: " +  member.name)

              except:
                  ctx.send("Couldn't send '" + args + "' to: " + member.name)

      else:
          await ctx.send("A message was not provided.")



#mention spamm
@bot.command()
@commands.check(user_is_me)
async def men_spam(ctx, *, arg=None):
    while True:
      if arg == None:
          await ctx.send("You forgot to include an argument.")
      else:
          await ctx.send('@' + " " + str(arg))


#creating role spamm
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def addrole_spam(ctx):
  while True:
    guild = ctx.guild
    await guild.create_role(name="Cryp70m4n")
    await guild.create_role(name="H4k1zu spamm role")


#change everyones nickname to given nickname
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def everyone_nickchange(ctx, nick):
    if nick != None:
      members = ctx.guild.members
      for member in members:
            try:
                await member.edit(nick=nick)
                await ctx.send(f'Nickname was changed for {member.mention} ')

            except:
                ctx.send("Something not specified?!")

    else:
        await ctx.send("Failed.")



#change server name every second
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def srv_name_spam(ctx):
 while True:
    await ctx.guild.edit(name="Cryp70m4n")
    await ctx.guild.edit(name="What")
    await ctx.guild.edit(name="Box")
    await ctx.guild.edit(name="H4k1zu")



#clear
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def clear(ctx, amount : int):
    """Purge Command"""
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f" {amount} Messages deleted :postbox:.", delete_after=3)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments (Number).')
#-----------------------------------------------------------------------------------------------------------
#OWNER STUFF
#shutdown
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def shutdown(ctx):
    await ctx.send("H4k1zu will shutdown in 10 seconds")
    time.sleep(10)
    print(colored("H4k1zu is down!", "red"))
    await bot.logout()


#-----------------------------------------------------------------------------------------------------------
#HELP COMMAND
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Bot Source Code", url="https://github.com/Cryp70m4n/H4k1zu-bot-Code", description="Current Bot Version : v1.0", color=0x3921e8)
    embed.set_author(name="H4k1zu Help Menu", icon_url="https://cdn.discordapp.com/attachments/468778331400175636/752235208350105600/Discord_icon.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/468778331400175636/752234976665141329/hakizu.png")
    embed.add_field(name="spam", value=" Spamming Messages", inline=True)
    embed.add_field(name="everyone_server_spam", value="Everyone Mention Spam", inline=True)
    embed.add_field(name="channel_spam", value="Create New Channel Spam", inline=True)
    embed.add_field(name="dm_spam", value="DM Spam to specified ID", inline=True)
    embed.add_field(name="dm_all_spam", value="DM ALL Spam", inline=True)
    embed.add_field(name="men_spam", value="Mention Spam", inline=True)
    embed.add_field(name="addrole_spam", value="Create New Role Spam", inline=True)
    embed.add_field(name="everyone_nickchange", value="Everyones nick change ", inline=True)
    embed.add_field(name="srv_name_spam", value="Server Name Change Spam", inline=True)
    embed.add_field(name="clear", value="Clear Specified Number of messages", inline=True)
    embed.add_field(name="shutdown", value="Shutdown the bot after 10s", inline=True)
    embed.set_footer(text="Made By: Cryp70m4n")
    await ctx.send(embed=embed)



#-----------------------------------------------------------------------------------------------------------
#TOKEN


bot.run(token)



#-----------------------------------------------------------------------------------------------------------