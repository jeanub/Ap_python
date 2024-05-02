"""
Los operadores aritmeticos se utilizan para realizar operaciones matematicas
basicas en numeros.
"""

#?Suma(+): El operador suma se utiliza para sumar dos numeros.
a = 5
b = 3
suma = a + b
print(suma)#Imprime la suma de a+b= 8

#?Resta(-) El operador de resta se utiliza para restar un numero de otro.
a = 5
b = 3
resta = a - b
print(resta)#Imprime la resta de a - b = 2

#?Multiplicacion(*): El operador multiplicacion se utiliza para multiplicar dos numeros.
a = 5
b = 3
multiplicacion = a * b
print(multiplicacion)#Imprime la multiplicacion de a * b = 15

#?Division(/): El operador de division se utiliza para dividir un numero por otro.(Siempre devuelve un resultado de tipo 'float').
a = 6
b = 3
division = a / b
print(division)#Imprime la division de a / b = 2.0

#?Division entera(//): Igual que la division anterior, con la diferencia que devuelve un valor entero.
a = 7
b = 3
division_entera = a // b 
print(division_entera)# Imprime 2, devuelve Int, redondeado hacia abajo

#?Modulo(%): El operador de modulo se utiliza para obtener el resto de la division entre dos numeros.
a = 7
b = 3
modulo = a % b
print(modulo)# Imprime 1

#?Potencia(**): El operador de potencia se utiliza para elevar un numero a una potencia.
a = 2
b = 3
potencia = a ** b
print(potencia)#Imprime 8