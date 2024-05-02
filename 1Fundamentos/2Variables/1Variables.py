"""
Una variable es un nombre que se utiliza para hacer referencia a un valor en la
memoria. Cuando asignas un valor a una variable, Python reserva un espacio en la
memoria para almacenar ese valor y te permite accerder a él utilizando el nombre
de la variable.
"""
#!1.Declaracion de variables:Las variables se declaran y se definen. Tambien son modificables.
#?Definiendo una variable
nombre_completo = "Jean Uribe"

#?Concatener con +:
bienvenida_al_usuario = "Hola" + "¿Como estas?"

#?Concatener con f-strings:
bienvenida = f"Hola {nombre_completo} ¿Como estas"

#?Operadores de pertenencia (in / not in)
print("Jean" in bienvenida)#True
print("Jean" not in bienvenida)#False

