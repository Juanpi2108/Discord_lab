# logica_bot.py

from datetime import datetime
import random

def obtener_hora():
    return f"La hora actual es: {datetime.now().strftime('%H:%M:%S')}"

def generar_numero():
    return f"Número aleatorio: {random.randint(1, 100)}"

def informacion():
    return (
        "Soy un agente de Discord desarrollado en Python.\n"
        "Comandos disponibles:\n"
        "!hora\n"
        "!numero\n"
        "!info"
    )