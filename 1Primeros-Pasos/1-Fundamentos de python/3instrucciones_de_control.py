"""
!En Python, las instrucciones de control se utilizam para controlar el flujo de ejecucion de un programa.
Las Principales instrucciones de control son: 'if', 'else', 'elif', 'for' y 'while'.

?if: 
la instruccion 'if' se utiliza para ejecutar un bloque de codigo si una condicion es verdadera
la sintaxis es:
    edad = 18
    if edad >= 18:
        print("Eres mayor de edad")

?else: 
La instruccion 'else' se utiliza en conjunto con 'if' para ejecutar un bloque de codigo
si la condicion del 'if' no se cumple. 
la sintaxis es:
    edad= 15
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

?ELIF: 
la instruccion 'elif' se utiliza para evaluar multiples condiciones despues de un 'if'.
se lee como "else if"
La sintaxis es:
    nota = 85
    if not >= 90:
        print("A")
    elif nota >= 80:
        print("B")
    else:
    print("C")

?FOR: 
la instruccion 'for' se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena
o rango) y ejecutar un bloque de codigo para cadena de elementos de la secuencia.
La sintaxis es:
    colores = ["rojo", "verde", "azul"]
    for color in colores:
        print(color)

?WHILE: 
la instruccion 'while' se utiliza para repetir un bloque de codigo mientras se cumpla una condicion.
la condicion se evalua antes de ejecutar el bloque de codigo, por lo que el bloque puede no ejecutarse nunca
si la condicion ya es falsa al principio. 
La sintaxis es:
    contador = 0
    while contador < 5:
        print(contador)
        contador +=1

"""

"""
#!Ejemplos simple de codigo sobre if, elif y else:

! IF y ELSE:
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad, puedes entrar")  
else:
    print("Eres menor de edad, vuelve a casa") 
"""

"""
!IF, ELIF y ELSE:
edad = int(input("Ingrese su edad: "))

if edad >=19:
    print("Eres mayor, puedes entrar")
elif edad == 11:
    print("Eres un niño de la vip")
else:
    print("NO MORE") 
"""

#! Ejemplos sobre  "Ciclos" FOR y WHILE:

"""
!FOR:
genios = ["Jean", "Axel"]

for genio in genios:
    print("Es un genio -->", genio)
"""

"""
#!WHILE:
var = int(input("Ingrese un numero:"))

while var < 10:
    var += 1
    print("Se sumo '1' al valor anterior y el resultado es:",var)
"""

