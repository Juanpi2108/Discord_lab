import discord
from discord.ext import commands
from tareas_agente import (
    reglas_servidor,
    enlaces_utiles,
    estado_servidor
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
    print(f"{bot.user} conectado exitosamente.")

@bot.command()
async def reglas(ctx):
    await ctx.send(reglas_servidor())

@bot.command()
async def recursos(ctx):
    await ctx.send(enlaces_utiles())

@bot.command()
async def estado(ctx):
    await ctx.send(estado_servidor())

bot.run(TOKEN)