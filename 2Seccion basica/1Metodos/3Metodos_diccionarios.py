"""
Los diccionarios son una estructura de datos muy util que permiten almacenar
pares de clave-valor.
"""

#?Key(): Devuelve una vista de las claves del diccionario.
diccionario = {
    "nombre": "Jean", 
    "edad":22}
claves = diccionario.keys()
print(claves)

#?Get(): Devuelve el valor asociado a una clave. Si la clave no existe, devuelve un valor predeterminado
diccionario = {
    "nombre": "Jean", 
    "edad":22}
nombre = diccionario.get("nombre")
print(nombre)#Output "Jean"

#?Clear(): Elimina todos los elementos del diccionario.
diccionario = {
    "nombre": "Jean",
    "edad":22}
diccionario.clear()
print(diccionario)#Output {}

#?Pop(): Elimina la clave especificada y devuelve el valor asociado.
diccionario = {
    "nombre": "Jean", 
    "edad":22}
nombre = diccionario.pop("nombre")
print(diccionario)#Output {"edad": 22}

#?Items():Devuelve una vista de los pares clave-valor del diccionario.
diccionario = {
    "nombre": "Jean", 
    "edad":22}
items = diccionario.items()
print(items)