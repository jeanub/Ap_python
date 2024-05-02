"""
Los Datos compuestos en python, son tipos de datos que pueden almacenar collecciones
de valores. Estos tipos de datos compuestos incluyen -->Listas, tuplas, conjuntos y
diccionarios. 
"""
#!1.Listas('list'): Son colecciones ordenadas y mutables de elementos.
#?Se puede accerder a los elementos de una lista mediante indices, empezando desde el 0.
#?Se pueden modificar añadiendo, eliminando o cambiando elementos.
mi_lista = [1,2,3,4,5]
print(mi_lista[0])#Imprime 1
mi_lista.append(6)#Añade el valor 6 a la lista

#!2.Tuplas('tuple'): Son colecciones ordenadas e inmutables de elementos.
#?No se pueden modificar una vez creadas, no se pueden añadir, eliminar o cambiar elementos
mi_tupla = (1,2,3,4,5)
print(mi_tupla[2])#imprime 3

#!3.Conjuntos('set'):Los conjunto son colecciones desordenadas y mutables de elementos unicos.
#?No admiten elementos duplicados.
#?se pueden añadir o eliminar elementos, Pero no accerder mediante índices.
mi_conjunto = {1,2,3,4,5}
mi_conjunto.add(6)#Añade el valor 6 al conjunto
print(mi_conjunto)#No se puede acceder por indice porque es una coleccion no ordenada

#!4.Diccionarios('dict'): Son colecciones desordenadas y mutables de pares "Clave-Valor"
#?Se pueden acceder a los valores mediante claves en lugar de indices.
#?Las claves deben ser únicas e inmutables.
mi_diccionario = {"nombre": "Jean", "edad": 22, "ciudad": "San Rafael"}
print(mi_diccionario["nombre"])#Imprime "Jean"