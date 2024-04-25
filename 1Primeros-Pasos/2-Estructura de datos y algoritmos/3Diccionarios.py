"""
Un diccionario es una estructura de datos que permiten almacenar 
pares clave-valor. Cada elemento en un diccionario esta representado
pro un par clave-valor, donde la clave es unica y se utiliza para acceder 
al valor correspondiente. Los diccionarios son una forma eficiente de
almacenar y recuperar datos cuando se conoce la clave asociada
"""
"""
Para crear un diccionario en python, se utilizan llaves '{}' y los
elementos se separan por comas.
Cada elemento esta formado por una clave seguida de dos puntos ':'
y el valor correspondiente.
"""
#Por ejemplo:
mi_diccionario = {"nombre": "Jean", "edad": 22, "ciudad": "san rafael"}
"""
En este caso "nombre", "edad", "ciudad", son las claves y
"jean", "22" y "san rafael" son los valores correspondientes
"""

#Puedes acceder a los valores en un diccionario utilizando las claves
nombre = mi_diccionario["nombre"]
print(nombre)#Devuelve Jean

"""
Si intentas acceder a una clave que no existe en el diccionario, python
generara un error. Para evitar este error puedes utilizar el metodo 'get()', que 
devuelve 'none' si la clave no esta presente en el diccionario
"""
apellido = mi_diccionario.get("apellido")
print(apellido)#Devuelve NONE

"""
Los diccionarios en python son mutables, lo que significa que puedes cambir, agregar o eliminar
elementos despues de crear el diccionario.
"""
#Por Ejemplo: Para cambiar el valor asociado con la clave "edad"

mi_diccionario["edad"] = 23
print(mi_diccionario["edad"])#Devuelve el nuevo valor asignado

#Para agregar un nuevo elemento al diccionario, simplemente asigna el nuevo par clave-valor
mi_diccionario["cuenta bancaria"] = "multi millonario"
print(mi_diccionario["cuenta bancaria"])

#Para elminar un elemento del diccionario, puedes utilizar la palabra 'del' seguida de la clave
del mi_diccionario["ciudad"]
print(mi_diccionario)

"""
Los diccionarios en Python son muy versatiles y se utilizan en una amplia variedad de 
situaciones donde se necesita almacenar y recuperar datos de forma eficiente utilizando una
clave asosciada
"""