"""
Las listas son un tipo de datos muy versatil y poderoso que te permite almacenar
una coleccion ordenada de elemento.
"""

#?Append():Agrega un elemento al final de la lista.
lista = [1,2,3]
lista.append(4)
print(lista)

#?Extend(): Extiende la lista agregando todos los elementos de otra lista al final.
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)
print(lista1)#Output [1,2,3,4,5,6]

#?Insert():Inserta un elemento en una posicion especifica.
lista = [1,2,3]
lista.insert(1,1.5)
print(list)#Output [1,1.5,2,3]

#?Remove(): Elimina la primera aparicion de un elemento en la lista.
lista = [1,2,3,2]
lista.remove(2)
print(lista)#Output [1,3,2]

#?Pop(): Elimina y devuelve el elemento en la posicion dada (O el ultimo elemento si no se especifica) (Con -1 se elimina el ultimo, con -2 el ante ultimo, etc)
lista = [1,2,3]
elemento = lista.pop(1)
print(elemento)#Output 2
print(lista)#Output [1,3]

#?Clear(): Elimina todos los elementos de la lista.
lista = [1,2,3]
lista.clear()
print(lista)#Output []

#?Len(): devuelve la cantidad de elementos de una lista.
lista = ["a",1,"b",3,4]
cantidad_elementos = len(lista)
print(cantidad_elementos) #Output 5

#?sort(): Ordena los elementos de una lista de menor a mayor
lista = [4,2,1,3]
lista.sort()
print(lista)#Output 1,2,3,4 (Con sort(reverse=True --> 4,3,2,1))

#?Reverse(): Invierte los elementos de una lista
lista = [5,4,3,2,1]
lista.reverse()
print(lista)