import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re



bot = commands.Bot(command_prefix='-', description="This is a Helper Bot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
   
@bot.command()
async def sum(ctx, num1:int, num2:int):
    await ctx.send(num1+num2)
    
@bot.command()
async def inf(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}", 
        description="Este server es el mas perro de todos ",
        timestamp = datetime.datetime.utcnow(),
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Server created at", 
        value=f"{ctx.guild.created_at}"
        )

    embed.add_field(
      name="Server Owner",
      value=f"{ctx.guild.owner}"
    )

    embed.add_field(
        name="Server region",
        value=f"{ctx.guild.region}"
    )
    embed.add_field(
        name="Server ID",
        value=f"{ctx.guild.id}"
    )

    embed.set_thumbnail(
        url="https://graffica.info/wp-content/uploads/2017/07/logotipo-nasa.jpg"
    )
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


#Evento
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tututorial", url="http://www.twitch.tv/accountname" ))
    print("el servidor de discord esta corriendo")

bot.run('token')
