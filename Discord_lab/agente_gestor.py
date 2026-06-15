import discord
from discord.ext import commands
from Discord_lab.gestor_comandos import saludar, despedir, ayuda

TOKEN = "TU_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    respuesta = saludar(ctx.author.name)
    await ctx.send(respuesta)

@bot.command()
async def adios(ctx):
    respuesta = despedir(ctx.author.name)
    await ctx.send(respuesta)

@bot.command()
async def ayuda_bot(ctx):
    respuesta = ayuda()
    await ctx.send(respuesta)

bot.run(TOKEN)