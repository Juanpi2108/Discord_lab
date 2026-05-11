patron_maestro = [1, 0, 1, 1, 0]

lectura_sensor = []

print("--- ESCÁNER BIOMÉTRICO DE IA ---\n")

for i in range(5):
    bit = int(input(f"Ingrese bit {i + 1}: "))
    lectura_sensor.append(bit)

coincidencias = 0

for i in range(5):
    if lectura_sensor[i] == patron_maestro[i]:
        coincidencias += 1

similitud = (coincidencias / 5) * 100

print("\n> Comparando lectura con base de datos...\n")
print(f"> Coincidencias encontradas: {coincidencias}")
print(f"> Porcentaje de Similitud: {similitud}%\n")

if similitud == 100:
    print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
elif similitud >= 60:
    print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
else:
    print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

print("\n--- DETALLE DE COMPARACIÓN ---")
print("Patrón Maestro :", patron_maestro)
print("Lectura Sensor :", lectura_sensor)