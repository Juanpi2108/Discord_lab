def inicializar_vector():
    return [0, 0, 0]

def leer_clasificaciones(vector):
    for i in range(5):
        clasificacion = int(
            input(f"Palabra {i + 1} - Clasificación (0: Positivo, 1: Neutral, 2: Negativo): ")
        )

        if clasificacion >= 0 and clasificacion <= 2:
            vector[clasificacion] += 1
        else:
            print("Clasificación inválida")

def buscar_mayor(vector):
    mayor = vector[0]
    indice_mayor = 0

    for i in range(1, len(vector)):
        if vector[i] > mayor:
            mayor = vector[i]
            indice_mayor = i

    return indice_mayor

def mostrar_resultado(vector, indice_mayor):
    print("\nEstado final del vector de características:", vector)

    if indice_mayor == 0:
        print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")
    elif indice_mayor == 1:
        print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")
    else:
        print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")

def main():
    print("--- ANALIZADOR DE SENTIMIENTOS IA ---\n")

    puntajes_sentimiento = inicializar_vector()

    leer_clasificaciones(puntajes_sentimiento)

    indice_mayor = buscar_mayor(puntajes_sentimiento)

    mostrar_resultado(puntajes_sentimiento, indice_mayor)

main()