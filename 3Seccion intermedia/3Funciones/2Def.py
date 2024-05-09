"""
Las funciones en python son bloques de codigo reutilizables que realizan una tarea
especifica. Pueden aceptar datos de entrada, llamados argumentos, realizan
operaciones en esos datos, y devolver un resultado.
"""

#!Definir una funcion:
"""
Para definir una funcion, utilizamos la palabra clave 'def', seguida del nombre
de la funcion y parentesis '()'. Despues de los parentesis, se coloca dos puntos ':'
Despues de los parentesis ':' Para indicar el inicio del bloque de codigo funcion.
El cuerpo de la funcion se indenta, y aqui es donde se escribe el codigo que realiza
la tarea deseada.
"""
def mi_funcion():
    #Codigo de la funcion
    print("Hola, soy una funcion!")


"""
!Llamar a una funcion: 
Para ejecutar una funcion y que realice su tarea, se llama a la funcion.
Esto se hace simplemente escribiendo el nombre de la funcion seguido de parentesis '()'

mi_funcion()#Output ¡Hola, soy una función!
"""

"""
!Argumentos de la funcion:
Las funciones pueden aceptar datos de entrada, llamados argumentos. se especifican
entre los parentesis al definir la funcion. Pueden ser variables, valores, u otros objetos.
"""
def saludar(nombre):
    print("¡Hola", nombre,"!")

"""
!Llamar a una funcion con Argumentos:
Cuando se llama a una funcion que acepta argumentos, se proporcionan los valores de esos
argumentos entre los parentesis.
"""
saludar("Jean")

"""
!Valor de Retorno:
Las funciones pueden devolver un resultado utilizando la palabra clave 'return'. Esto es util
cuando se desea utilizar el resultado de la funcion en otras partes del codigo.
"""
def suma (a, b):
    return a+b
resultado = suma(3, 5)
print(resultado)#Output

"""
!Argumentos por defecto:
Se puede establecer valores predeterminados para los argumentos de una funcion. estos valores
se utilizan si no se proporcionan argumentos al llamar a la funcion.
"""

def saludar(nombre="Amigo"):
    print("Hola,", nombre)

saludar()
saludar("Jean")

"""
!Funciones Recursivas:
una funcion puede llamarse a si misma, lo que se conoce como recursividad. esto es util
para resolver problemas que se puede descomponer en problemas mas pequeños del mismo tipo.
"""

def factorial(n):
    if n ==0:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))#Output 120(5*4*3*2*1)

"""
!Alcance de las variables:
Las variables definidas dentro de una funcion son locales a esa funcion y no pueden ser accedidas
desde fuera de ella. Sin embargo, las variables definidas fuera de una funcion pueden ser accedidas
y modificadas dentro de la funcion, a menos que sea declaradas como 'global'
"""
def mi_funcion():
    x = 10 #Variable local
    print("Dentro de la funcion:", x)#Dentro de la funcion: 10

x=20#Variable global
mi_funcion()
print("Fuera de la funcion", x)#Fuera de la funcion: 20

"""
!Argumentos Arbitrarios:
Python permite definir funciones que aceptan un numero arbitrario de argumentos. Para esto,
se utiliza '*args' para argumentos posicionales y '**kwargs' para argumentos de palabras clave.
"""
def mi_funcion(*args, **kwargs):
    for arg in args:
        print("Argumentos posicional:", arg)
    for clave, valor in kwargs.items():
        print("Argumentos de la palabra clave:", clave, "=", valor)
mi_funcion(1,2,3,nombre="Jean", edad=22)

"""
!Lambdas(Funciones Anónimas):
Las lambdas son funciones anonimas de una sola linea que pueden tener cualquier numero de
argumentos, pero solo pueden tener una expresion. se definen utilizando la palabra clave 'lambda'.
"""
suma = lambda a,b : a+b
print(suma(3,5))#Output 8