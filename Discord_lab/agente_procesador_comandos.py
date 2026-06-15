import discord
from discord.ext import commands
from procesador_comandos import (
    promedio,
    convertir_metros,
    datos_materia
)

TOKEN = "TU_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def prom(ctx, n1: float, n2: float, n3: float):
    await ctx.send(promedio(n1, n2, n3))

@bot.command()
async def metros(ctx, cantidad: float):
    await ctx.send(convertir_metros(cantidad))

@bot.command()
async def materia(ctx):
    await ctx.send(datos_materia())

bot.run(TOKEN)