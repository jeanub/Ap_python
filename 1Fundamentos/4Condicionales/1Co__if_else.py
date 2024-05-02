"""
Los condicionales en python se utilizan para ejecutar ciertos bloques de codigo 
solo si se cumple una condicion especifica. Los condicionales mas comunes son
'if', 'elif' y 'else'
"""

#?if: El bloque de código dentro de un if se ejecuta solo si la condición especificada es verdadera (evalúa a True).
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

#?elif: elif se utiliza para verificar múltiples condiciones después de un if. Si la condición en el if es falsa, se evalúa la siguiente condición en el elif.
nota = 85
if nota >= 90:
    print("Goood")
elif nota >= 80:
    print("Good")
elif nota >= 70:
    print("god")
else:
    print("no god")

#?else: El bloque de código dentro de else se ejecuta si ninguna de las condiciones anteriores es verdadera. Es opcional y solo puede usarse una vez al final.
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


#?Anidamiento de condicionales: Puedes anidar condicionales dentro de otros condicionales para realizar verificaciones más complejas.
num = 10
if num > 0:
    if num % 2 == 0:
        print("Es un número positivo y par")
    else:
        print("Es un número positivo e impar")
else:
    print("Es un número negativo")


#?Operadores lógicos: Puedes combinar múltiples condiciones utilizando los operadores lógicos and, or, y not.
edad = 25
if edad >= 18 and edad <= 65:
    print("Eres adulto")

