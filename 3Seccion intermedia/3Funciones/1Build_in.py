"""
Las funcion built-in de python son aquellas que estan integradas en el lenguaje y estan disponibles
para su uso sin necesidad de importar ningun modulo adicional. Estas funciones proporcionan
funcionalidades basicas  y fundamentales que son comunmente utilizadas en la programacion diaria
"""

#?1Print():La función print() se utiliza para imprimir mensajes en la consola. Puedes pasarle uno o más argumentos separados por comas y los imprimirá en la consola.
print("Hola, mundo!")


#?2Input():La función input() se utiliza para obtener una entrada del usuario desde la consola. Puedes mostrar un mensaje opcional para solicitar la entrada.
nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)

#?3Len()La función len() se utiliza para obtener la longitud de un objeto, como una cadena, lista, tupla, etc.
cadena = "Hola, Mundo!"
print(len(cadena))#Imprime 12

#?4Range(): La funcion range() se utiliza para generar una secuencia de nuemeros. Puedes proporcionar uno, dos o tres aguamentos para especificar el inicio y fin de la secuencia.
for i in range(5):
    print(i)#Output del 0 al 4

#?5Sum(): La función sum() se utiliza para sumar todos los elementos de una lista (o cualquier iterable).
numeros = [1,2,3,4,5]
print(sum(numeros))#Output 15

#?6 Max() y Min(): Estas funciones se utilizan para encontrar el valor máximo y mínimo en una lista (o cualquier iterable).
numeros = [1,2,3,4,5]
print(max(numeros))#Output 5
print(min(numeros))#Output 1

#?7Sorted(): se utiliza para ordenar una lista (o cualquier iterable). Puede tomar un argumento opcional reverse=True para ordenar en orden descendente
numeros = [5,2,8,1,3,4]
print(sorted(numeros))#Output [1,2,3,4,5,8]
print(sorted(numeros, reverse=True))#Output [8,5,4,3,2,1]

#?8Round(): Se utiliza para redondear un numero a una cantidad especifica de digitos decimales.
numero = 3.141659
resultado = round(numero, 2)#Se redondeara a 2 numeros despues de la coma
print(resultado)#Output 3.14

#?9Bool():Se utiliza para convertir un valor en su equivalente booleano. Los valores booleanos son 'True o False'
print(bool(0))#False
print(bool(1))#True
print(bool(-1))#True
print(bool([]))#False (una lista vacia)
print(bool([1,2]))#True (Una lista no vacia)
print(bool(""))#False (Una cadena vaci)
print(bool("Hola"))#True (Una cadena no vacia)
print(bool(None))#False (El valor None)

#?10All():  se utiliza para determinar si todos los elementos de un iterable son evaluados como verdaderos. Retorna True si todos los elementos son verdaderos.
print(all([True, True, True])) #True
print(all([True, False, True])) #False