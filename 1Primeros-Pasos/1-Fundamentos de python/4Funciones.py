"""
!Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.
las funciones pueden aceptar argumentos(valores de entrada), realizar operaciones
y devolver un resultado utilizando la palabra clave 'return'.

Una funcion se define utilizando la palabra clave 'def' seguida del nombre
de la funcion y los parentesis. la definicion de la funcion finaliza con dos 
puntos ':' y el codigo de la funcion se escribe con sangria.
"""
#Por ejemplo:

def saludar (nombre):
    print("Hola, " + nombre + "!")

#En este caso, 'saludar' es el nombre de la funcion y 'nombre' es el argumento que acepta.

#!Llamada a una funcion.
""" Para llamar a una funcion y ejecutar su codigo, simplemente se escribe el 
nombre de la funcion seguido de parentesis y los valores de los argumentos"""
#Por ejemplo:
saludar("Jean")
#Esta llamada imprimira "hola, Jean!"

#!Argumentos de una funcion:
""" Una funcion puede aceptar multiples argumentos separados por comas. los 
argumentos pueden tener valores predeterminados, lo que significa que si no se
proporciona un valor al llamar a la funcion, se usara el valor predeterminado"""
#Por ejemplo
def sumar (a, b=0):
    return a + b

print(sumar(3, 4)) #Resultado 7
print(sumar(3))    #Resultado 3

#En este ejemplo, 'sumar' es una funcion que acepta dos argumentos, 'a' y 'b',
#donde b tiene un valor predeterminado de '0'

#!Retorno de valores:
"""Una funcion puede devolver un valor utilizando la palabra clave 'return'.
Esto finaliza la ejecucion de la funcion y devuelve el valor espeficado"""
#Por ejemplo:
def sumar(a, b):
    return a + b
resultado = sumar(3,4)
print(resultado) #Resultado 7
#En este caso, la funcion 'sumar' devuelve la suma de 'a' y 'b', Que luego se asigna
# a la variable 'resultado'

#!Alcanse de las variables:
"""Las variables definidad dentro de una funcion tienen un alcance local, lo que
significa que solo son accesibles dentro de esa funcion. las variables definidas
fuera de una funcion tienen un alcance global y son accesibles desde cualquier parte
del codigo"""
#Por ejemplo:
x = 10
def imprimir_x():
    print(x) #Esto imprime el valor de x, que es 10
imprimir_x()
#En este ejemplo, la funcion 'imprimir_X' puede accerder a la variable 'x' definida
#fuera de la funcion porque 'x' tiene un alcance global.

#!Documentacion de funciones:
"""Es una buena practica documentar las funciones utilizando cadenas de documentacion
(docstrings). Estas son cadenas de texto que describen lo que hace la funcion"""
#Por ejemplo:
def sumar(a, b):
    """
    Esta funcion suma 2 numeros y devuelve el resultado.
    
    Args:
    a (int o float): el primer numero a sumar
    b (int o float): el segundo numero a sumar

    Returns:
    int o float: La suma de dos numeros.
    """
    return a + b
