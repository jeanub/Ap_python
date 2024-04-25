"""
!Una lista es una coleccion ordenada y mutable de elementos
Esto significa que puede almacenar una secuencia de elementos
en una lista y modificarlas segun sea necesario.
Las listas son una de las estructuras de datos mas 
utilizadas en python debido a su versatilidad y facil uso
"""

#Para crear una lista en python, simplemente encierra los elementos entre '[]',separado por coma','
mi_lista = [0,1,2,3,4,5,6,7,8,9]
print(mi_lista) #Esto mostrara los valores de la lista
"""
Se puede accerder a los elementos de una lista utilizando la indexacion. en Python,los
indices comienzan en 0, por lo que el primer elemento de la lista tiene un indice de 0.
por ejemplo, para acceder al primer elemento de "mi lista"
"""
primer_elemento = mi_lista[0]
print(primer_elemento)#Esto mostrara el primer elemento de la lista

"""
Las listas tambien admiten rebanadas (SLICES) para acceder a subconjuntos de elementos
de la lista. Puedes especififar un rango de indices separados por dos puntos ':' para 
obtener una parte de la lista.
"""
#Por ejemplo, para obtener elementos desde el segundo hasta el cuarto
segundo_y_cuarto = mi_lista[1:4]
print(segundo_y_cuarto)#Esto mostrara el elemento [2,3,4]

"""
Una caracteristica importante de las listas en Python es que son mutables, lo que 
significa que puedes cambiar, agregar o eliminar elementos de una lista despues de crearla.
"""
#Por ejemplos, para cambiar el segundo elemento de "mi lista":
mi_lista[1] = 10
print(mi_lista[1])#Esto mostrara 10

#Para agregar un elemento al final de la lista, puedes utilizar el metodo 'appedn()'
mi_lista.append(10)
print(mi_lista)# Esto mostrara la lista con el valor nuevo al final de la lista

#Para eliminar un elemento de la lista, puedes utilizar la declaracion 'del' o el metodo 'remove()' si conoces el valor del elemento a eliminar
del mi_lista[1]#Eliminara el segundo elemento de la lista
print(mi_lista)

mi_lista.remove(3) #Elimina el valor 3 de la lista
print(mi_lista)

"""
Tambien puedes utilizar el operador '+' para concatenar listas y el operador '*' para repetir
una lista
"""
#Por ejemplo:
otra_lista = [7,8,9]
lista_concatenada = mi_lista + otra_lista #Concatena las dos listas
lista_repetida = mi_lista*2 #Repite la lista dos veces
print(lista_concatenada, lista_repetida)

"""
En resumen, las listas en Python son colecciones ordenadas y mutables de elementos. 
Son versátiles y se utilizan ampliamente en Python debido a su flexibilidad y facilidad de uso.
"""