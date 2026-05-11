import datetime

def agregar_tarea(lista_tareas, descripcion):
    '''
    Agrega una tarea a la lista si cumple con los requisitos
    '''

    if len(descripcion) < 3:
        return "Error: Longitud no válida"
    
    #crear formato para la tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con éxito"