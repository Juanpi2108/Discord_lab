def promedio(n1, n2, n3):
    resultado = (n1 + n2 + n3) / 3
    return f"El promedio es: {resultado:.2f}"

def convertir_metros(metros):
    centimetros = metros * 100
    return f"{metros} metros equivalen a {centimetros} centímetros."

def datos_materia():
    return (
        "Materia: Programación\n"
        "Horario: Lunes y Miércoles\n"
        "Salón: A-203"
    )