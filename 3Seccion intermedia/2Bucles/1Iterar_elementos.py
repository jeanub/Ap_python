animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10,20,30,40,]

#?Recorriendo lista de animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#?Recorriendo lista de numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero*10
    print(resultado)

#?Iterando 2 lista del mismo tamaño al mismo tiempo:
for numero, animal in zip(animales, numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

#!Forma no optima de recorrer una lista con su indice(No FUNCIONA EN CONJUNTOS)
for num in range(len(numeros)):
    print(numeros[num])

#?Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')


#?Usando el for/else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("EL bucle termino.")


#!Todo lo anterior funciona exactamente igual para tuplas y conjuntos