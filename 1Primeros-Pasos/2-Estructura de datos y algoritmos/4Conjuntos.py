"""
Un conjunto es una coleccion desordenada y mutable de elementos unicos.
esto significa que un conjunto no contiene elementos duplicados y puedes modificar su
contenido despues de crearlo. Los conjuntos son utiles cuando necesitas almacenar una coleccion
de elementos unicos y no te importa el orden en que aparecen
"""

"""
Para crear un conjunto en python, puedes usar llaves '{}' o la funcion 'SET()' y enumerar
los elementos separados por comas
"""
#Por ejemplo:
mi_conjunto ={1,2,3,4,5}
print(mi_conjunto)

#Tambien se pueden crear un conjunto vacio de la siguiente manera:
conjunto_vacio = set()
print(conjunto_vacio)

"""
Para agregar elementos a un conjunto, puedes usar el metodo 'add()' o 'update()'
El metodo 'add()' agrega un unico elemento al conjunto, mientras que el metodo
'update()' puede agregar multiples elementos a la vez.
"""
#Por ejemplo:
mi_conjunto.add(6)#agrega el elemento 6 al conjunto
mi_conjunto.update([7,8])#Agrega los elementos 7 y 8 al conjunto
print(mi_conjunto)

"""
Para eliminar elementos de un conjunto, puedes usar el metodo 'remove()' o 'discard()'
remove(): Genera un error si el elemento no esta presente en el conjunto
discard(): No genera ningun error
"""
#Por ejemplo:
mi_conjunto.remove(6)#Elimina el elemento 6 del conjunto
mi_conjunto.discard(7)#Elimina el elemento 7 del conjunto
print(mi_conjunto)

"""
Puedes realizar operaciones comunes de conjuntos en python, como union, interseccion,
diferencia y diferencia simetrica. estas operaciones se realizan utilizando los operadores
'|'(union), '&'(inteseccion), '-'(diferencia) y '^'(diferencia simetrica)
"""
#Por ejemplo:
conjunto1= {1,2,3}
conjunto2= {3,4,5}

union = conjunto1 | conjunto2 #{1,2,3,4,5}
interseccion = conjunto1 & conjunto2 #{3}
diferencia = conjunto1 - conjunto2 #{1,2}
diferencia_simetrica = conjunto1 ^ conjunto2 #{1,2,4,5}
print(union, interseccion, diferencia, diferencia_simetrica)

"""
En resumen, los conjuntos en python son colecciones desordenadas y mutables de elementos
unicos. Son utiles cuando necesitas almacenar elementos unicos y realizar operaciones de 
conjuntos, como union, interseccion y diferencia.
"""