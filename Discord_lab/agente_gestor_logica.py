import discord
from discord.ext import commands

from agente_logica import (
    obtener_hora,
    generar_numero,
    informacion
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
    print(f"{bot.user} se ha conectado correctamente.")

@bot.command()
async def hora(ctx):
    await ctx.send(obtener_hora())

@bot.command()
async def numero(ctx):
    await ctx.send(generar_numero())

@bot.command()
async def info(ctx):
    await ctx.send(informacion())

bot.run(TOKEN)