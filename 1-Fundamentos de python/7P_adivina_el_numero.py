import random

numero_aleatorio = random.randint(1,10)
#ciclo while true: Se repite hasta que la condicion sea verdadera y se finaliza con un break debajo de la condicion verdadera
while True:
    numero = int(input("Adivina el numero: "))
    if numero == numero_aleatorio:
        print("adivinaste el numero", numero_aleatorio)
        break
    elif numero<numero_aleatorio:
        print("el numero es mayor")
    else:
        print("el numero es menor")