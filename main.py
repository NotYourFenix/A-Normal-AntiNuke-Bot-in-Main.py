import discord
import os
import sys
import requests
from time import strftime
import jishaku
from discord.utils import find
from discord_buttons_plugin import *
from discord_components import *
from typing import Union
import datetime
start_time = datetime.datetime.utcnow()

async def get_prefix(client, message):
    if message.author.id in [979967089542569994,]:
        return ""
    else:
        return "-"

prefix = "-"
token = "YOUR BOT TOKEN"
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.AutoShardedBot(shard_count=1,command_prefix=get_prefix, case_insensitive=True, intents=intents , help_command=None)
client.owner_ids = [979967089542569994]
client.add_cog(anti(client)) 
buttons = ButtonsClient(client)
headers = {"Authorization": f"{token}"}
ddb = DiscordComponents(client)

client.load_extension("jishaku")

@client.event
async def on_ready():
    print(f"Sucessfully logged in {client.user}")

def restart_client(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command(aliases=["reboot", "poweron"])
@commands.is_owner()
async def restart(ctx):
  await ctx.send(f"successfully restarted {client.user}")
  restart_client()

@client.event
async def on_ready():
    print(f"Bot is Ready")
    channel = client.get_channel(CHANNEL ID WHERE YOU WANT TO CONNECT YOUR BOT)
    activity = discord.Activity(type=discord.ActivityType.listening,
                                name="YOUR BOT CUSTOM STATUS!")
    await client.change_presence(status=discord.Status.idle,
                                 activity=activity)
    await channel.connect()

######## gg ###########

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.content.startswith(f'<@{client.user.id}>'):
    embed = discord.Embed(color=0x0052F9,
    title=f"connect", description = f"Hey My Prefix is `{prefix}`")
    await message.reply(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(color=0x0052F9, 
        title="",
        description=
        f"**`{int(client.latency * 1000)}ms`**")
    embed.set_thumbnail(
        url=
        'ENTER YOUR BOT PFP URL SKID'
    )
    await ctx.send(embed=embed)

@client.command(aliases=["mc"])
async def membercount(ctx):
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x0052F9)
    embed.add_field(name="**Members**",
                    value=ctx.guild.member_count,
                    inline=False)
    await ctx.send(embed=embed)

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(color=0x0052F9, 
        title="Bot Stats",
        description=
        f"**__Bot Info__**\n~ Name: {client.user}\n~ Developer: NotYourFenix#5465\n~ Language: Python\n~ Library: Discord.py\n~ Host: Replit (Temp)\n~ prefix: {prefix}\n\n**__Bot Stats__**\n~ Guilds: {len(client.guilds)}\n~ Users: {len(client.users)}\n~ Latency: {int(client.latency * 1000)}ms")
    embed.set_thumbnail(
        url=
        'ENTER YOUR BOT PFP URL SKID'
    )
    await ctx.send(embed=embed)

############### ANTINUKE ##################

@client.event
async def on_member_join(member):
    guild = member.guild
    reason = "NotYourFenix#5465 | Anti-Bot-Add"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
    logs = logs[0]
    if logs.user.id == guild.owner.id or logs.user.top_role >= guild.me.top_role:
        return
    if member.bot:
      await member.ban(reason=f"{reason}")
      await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_kick(member):
    guild = member.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
    logs = logs[0]
    reason = "NotYourFenix#5465| Kicking Members"
    await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_remove(member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "NotYourFenix#5465| Anti Prune"
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_ban(guild, member : discord.Member):
    if member == guild.me: return
    reason = "NotYourFenix#5465 | Anti-Ban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")
    await guild.unban(user=member, reason="Anti Ban")




@client.event
async def on_member_unban(guild, member : discord.Member):
    reason = "NotYourFenix#5465 | Anti-Unban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_channel_delete(channel):
  reason = "NotYourFenix#5465 | Anti Channel Delete"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  if isinstance(channel, discord.TextChannel):
      await guild.create_text_channel(channel.name, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
  if isinstance(channel, discord.VoiceChannel):
      await guild.create_voice_channel(f"{channel}")

  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  if logs.user == after.owner: return
  await logs.user.ban(reason="NotYourFenix#5465 | Guild Update")
  await after.edit(name=f"{before.name}")
 
@client.event
async def on_guild_channel_create(ch):
    try:
        async for entry in ch.guild.audit_logs(limit = 1 , action = discord.AuditLogAction.channel_create):
            await ch.guild.ban(entry.user , reason = "NotYourFenix#5465 | Anti Channel")
            await ch.delete()
    except Exception as e:
        print(e)



@client.event
async def on_message(message):
  await client.process_commands(message)
  member = message.author
  guild = message.guild
  if message.mention_everyone:
    idk = message.guild.get_member(client.user.id)
    if message.author.top_role.position >= idk.top_role.position:
        pass
    else:
        await message.author.ban(reason="NotYourFenix#5465 | Mentioning everyone/here")

 
 
@client.event
async def on_guild_role_create(role):
    reason = "NotYourFenix#5465 | Anti Role Create"
    guild = role.guild
    logs = await guild.audit_logs(
        limit=1, action=discord.AuditLogAction.role_create).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")
    await role.delete()

@client.event
async def on_guild_role_delete(role):
    guild = role.guild
    logs = await guild.audit_logs(
        limit=1, action=discord.AuditLogAction.role_delete).flatten()
    reason = "NotYourFenix#5465 | Anti Role Delete"
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")
    await guild.create_role(name=role.name,
                            color=role.color,
                            permissions=role.permissions,
                            hoist=role.hoist,
                            mentionable=role.mentionable)

@client.event
async def on_guild_channel_update(before, after):
  reason = "NotYourFenix#5465 | Anti Channel Update"
  guild = after.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

####### CHEAP ERRORS LOG #######

@client.event
async def on_command_error(ctx, error: commands.CommandError):
  embed1 = discord.Embed(description=f"You Need Permission To Run This Command", color=0x0052F9)
  embed2 = discord.Embed(description=f"You Are Missing An Arguments To Run This Command", color=0x0052F9)
  embed3 = discord.Embed(description=f"The Selected Member could not be found", color=0x0052F9)
  embed4 = discord.Embed(description=f"I Am Running Out of Permissions To Run This Command", color=0x0052F9)
  embed5 = discord.Embed(description=f"Command is On CoolDown Pls Try Again Later!", color=0x0052F9)
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(embed=embed1)
  elif isinstance(error, commands.MissingRequiredArgument):
     await ctx.send(embed=embed2)
  elif isinstance(error, commands.MemberNotFound):
    await ctx.send(embed=embed3)
  elif isinstance(error, commands.BotMissingPermissions):
    await ctx.send(embed=embed4)
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send(embed=embed5)
  else:
    raise error

client.run(token)
