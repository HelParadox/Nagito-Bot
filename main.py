import discord, keep_alive, os, random, time
from discord.ext import commands, tasks
from asyncio import sleep
import urllib.parse
import urllib.request


bot = commands.Bot(command_prefix="n!", case_insensitive=True)

client = discord.Client()

@bot.event
async def on_ready():
    print("bot ready!")


@bot.command()
async def hello(ctx):
  await ctx.send(f"Hello")

@bot.command()
async def CommandHelp(ctx):
  embed = discord.Embed(
    title = 'Help',
    description = 'Help For Commands!',
    colour = 0x33F2FF

  )

  embed.set_footer(text="")
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='Misc', value='`n!misc` for misc commands')
  

  await ctx.send(embed=embed)
@bot.command()
async def misc(ctx):
  embed = discord.Embed(
    title = 'Misc',
    description = 'Misc Commands',
    colour = 0x33F2FF
  )

  embed.set_footer(text="Misc")
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='Youtube', value='`n!Youtube (video) this will search youtube for videos')
@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! - {round(bot.latency * 1000)}ms!")

@bot.command()
async def youtube(ctx, *, search):
  query_string = urllib.parse.urlencode({
    'search_query': search
  })
  htm_content = urllib.request.urlopen(
    'http://www.youtube.com/results?' + query_string
  )
  search_results = re.findall("href=\"\\/watch\\?v=(.{11})", htm_content.read().decode())
  await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def purge(ctx, amount):
  await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)


@bot.command()
async def neon(ctx):
  await ctx.send(f"Join NeonGDPS today! https://discord.gg/YYfyYjJuH6")

@bot.command()
async def embed(ctx):
  embed = discord.Embed(
    title = 'UselessEmbed',
    colour = 0x33F2FF

  )

  embed.set_footer(text="")
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='Why', value='Did u use this command?')
  embed.set_image(url='https://cdn.discordapp.com/avatars/582670290950291476/5723169a306c581dd6d0d9ae41fa6a3c.png?size=1024')
  
  await ctx.send(embed=embed)




@bot.command()
async def dm(ctx,member : discord.Member,*,message= ""):
  await member.send(f"{message}")
  await ctx.channel.purge(limit=1)
  person = await bot.fetch_user(member.id)
  await ctx.channel.send(f"The DM to **{person}** was sent!")

keep_alive.keep_alive()
token = os.environ.get("token")
bot.run(token, bot=True, reconnect=True)

@client.event
async def on_member_join(member):
    await member.send(f"Welcome To The discord!")
