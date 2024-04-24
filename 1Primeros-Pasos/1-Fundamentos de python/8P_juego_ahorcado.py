import random

tupla = ("gato", "perro","jamster","pez","gallina","boca", "luna","escorpio")
palabra_aleatoria = random.choice(tupla)

while palabra:
    palabra = input("Adivina la palabra")
    if palabra == palabra_aleatoria:
        print("adivinaste la palabra")
        break
    else:
        print("Sigue intentado")
