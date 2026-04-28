class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        # Validación de error negativo
        if valor_error < 0:
            raise ValueError("El error no puede ser negativo.")

        # Verificar convergencia
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")

        # Guardar en historial
        self.historial_errores.append(valor_error)
        print("> Registro exitoso.\n")


print("--- Iniciando Monitor de Red Neuronal ---\n")

monitor = MonitorEntrenamiento()

epocas = 5
contador = 0

while contador < epocas:
    try:
        entrada = input(f"Ingrese el error de la Época {contador + 1}: ")
        valor_error = float(entrada)

        monitor.registrar_epoca(valor_error)
        contador += 1

    except ValueError:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.\n")


print("\n--- Resumen de Entrenamiento ---")

if monitor.historial_errores:
    print("Historial:", monitor.historial_errores)

    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    print("Promedio de Error:", promedio)

    mejor_error = min(monitor.historial_errores)
    print("Mejor resultado obtenido:", mejor_error)
else:
    print("No se registraron datos válidos.")
