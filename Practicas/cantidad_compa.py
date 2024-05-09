#Falto el profe y los pibes van a armar la clase

#Pedir el nombre y la edad de los compañeros que vinieron.

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del almuno: ")
        Edad = (input("Ingrese la edad del almuno: "))
        compañero = (nombre, Edad)
        
        #?Agrengando la informacion a la lista
        compañeros.append(compañero)
    #?Ordenandolos de menor a mayor segun su edad   
    compañeros.sort(key=lambda x:x[1])
    #Compañero[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #Para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    #Retornamos una tupla
    return asistente, profesor

#?Desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(int(input("Ingresa la cantidad de alumnos: ")))
print(f'El profesor es: {profesor} y su asistente es: {asistente}')