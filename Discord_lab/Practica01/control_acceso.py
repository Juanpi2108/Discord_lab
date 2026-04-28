def main():
    print("--- MÓDULO DE SENSORES (VECTORES) ---")
    
    sensores_distancia = []
    
    for i in range(5):
        while True:
            try:
                distancia = float(input(f"Ingrese distancia sensor {i+1}: "))
                if distancia < 0:
                    print("Error: la distancia no puede ser negativa.")
                else:
                    sensores_distancia.append(distancia)
                    break
            except ValueError:
                print("Error: ingrese un número válido.")
    
    promedio = sum(sensores_distancia) / len(sensores_distancia)
    
    if promedio < 2.0:
        estado = "Aviso: Reduciendo velocidad global"
    else:
        estado = "Estado: Seguro"
    
    print(f"\nPromedio de proximidad: {promedio:.2f}m. {estado}")
    
    
    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
    
    camara_ia = []
    
    print("Llenando matriz de cámara 3x3:")
    
    for fila in range(3):
        fila_actual = []
        for col in range(3):
            while True:
                try:
                    valor = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
                    
                    if valor > 255:
                        valor = 255
                    elif valor < 0:
                        valor = 0
                    
                    fila_actual.append(valor)
                    break
                except ValueError:
                    print("Error: ingrese un número entero válido.")
        
        camara_ia.append(fila_actual)
    
    print("\nVisualización de la imagen capturada:")
    for fila in camara_ia:
        print("[", end=" ")
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print("]")
    
    contador_brillo = 0
    for fila in camara_ia:
        for valor in fila:
            if valor > 200:
                contador_brillo += 1
    
    print("\nResultado de Análisis IA:")
    print(f"Se detectaron {contador_brillo} píxeles de alta intensidad.")


if __name__ == "__main__":
    main()