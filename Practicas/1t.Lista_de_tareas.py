#Lista de Tareas:
def lista_de_tareas():#!Esta funcion crea una lista de tareas.
    tareas = []
#?Creando las funciones: 1.Agregar tarea 2.Eliminar Tarea 3.Mostrar tareas 4.Salir
    #//Agregar una tarea:
    def agregar_tarea(tarea):
        tareas.append(tarea)
        print("Nueva Tarea Agregada.")
    #//Eliminar una tarea:
    def eliminar_tarea(indice):
        if indice < len(tareas):
            del tareas[indice]
            print("Tarea Eliminada.")
    #//Mostrar Tareas:
    def mostrar_tareas():
        if tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(tareas):
                print(f'{i}. {tarea}')
        else:
            print("No hay tareas en la lista.")

    #?Bucle principal:
    while True:
        print('\n1. Agregar tarea\n2. Eliminar Tarea\n3. Mostrar tareas\n4. Salir.')
        opcion = input("Seleccione una opcíon: ")
        if opcion == '1':
            tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(tarea)
        elif opcion == '2':
            indice = int(input("Ingrese el indice de la tarea a eliminar: "))
            eliminar_tarea(indice)
        elif opcion =='3':
            mostrar_tareas()
        elif opcion == '4':
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

print(lista_de_tareas())