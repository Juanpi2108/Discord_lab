def solicitar_datos():
    print("--- TELEMETRÍA DE CLUSTER IA ---\n")

    temperatura = float(input("Temperatura actual (°C): "))
    memoria = int(input("Uso de Memoria VRAM (%): "))
    enfriamiento = input("¿Enfriamiento activo? (si/no): ").lower()

    return temperatura, memoria, enfriamiento

def validar_memoria(memoria):
    if memoria < 0 or memoria > 100:
        print("\nError: Lectura de memoria fuera de rango (0-100%).")
        return False
    return True

def diagnosticar_sistema(temperatura, memoria, enfriamiento):
    if temperatura > 90 or memoria == 100:
        print("\n> Diagnóstico: ¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")

    elif 75 <= temperatura <= 90:

        if enfriamiento == "no":
            print("\n> Diagnóstico: Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")

        elif enfriamiento == "si":
            print("\n> Diagnóstico: Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")

        else:
            print("\n> Diagnóstico: Estado de enfriamiento no válido.")

    elif temperatura < 75 and memoria < 80:
        print("\n> Diagnóstico: Sistema Estable: Entrenamiento en curso a máxima capacidad.")

        memoria_libre = 100 - memoria
        print(f"> VRAM disponible: {memoria_libre}%")

    else:
        print("\n> Diagnóstico: Sistema funcionando con carga moderada.")


def main():
    temperatura, memoria, enfriamiento = solicitar_datos()

    if validar_memoria(memoria):
        diagnosticar_sistema(temperatura, memoria, enfriamiento)

main()