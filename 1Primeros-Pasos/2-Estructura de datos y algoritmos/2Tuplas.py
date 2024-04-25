"""
!las tuplas son secuencias ordenadas e inmutables de elementos. 
Significa que:
una vez que se crea una tupla, no se pueden modificar sus elementos. Las tuplas
se utilizan para almacenar colecciones de datos que no deben cambiar, como
coordenadas, fechas, o datos que representan una entidad unica, como informacion
de una persona
"""

#Para crear una tupla se utulizan parentesis '()' y se separan los elementos con comas ','
tupla_1= (1,2,3,4,5)

#Para accerder a los elementos de una tupla, se utiliza la indexacion"[0,1,etc]".
tupla_2 = ("dato1","dato2")
print(tupla_2[0]) #Esto mostrara el valor "dato1" alojado en el indice 0

#Las tuplas tambien adminten rebanadas(Slices) para acceder a un subconjuntos de elentos

sub_tupla = (0,1,2,3,4,5,6,7,8,9)
print(sub_tupla[0:4]) #Muestra del indice 0 al 4. Es decir 

#Una vez que se crea una tupla, no se puede modificar su contenido.
# Esto genera un error
#!sub_tupla[2] = 3

#Tambien se pueden concatenar tuplas para crear una con el valor de ambas:
tupla_ayb = tupla_1 + tupla_2
print(tupla_ayb) #Esto mostrara la suma de la tupla "Tupla_1 y Tupla_2"

#Las tuplas tambien se pueden utilizar para asignar multiples valores en una sola instruccion:
a, b, c = (1,2,3)
print(a,b,c) #Esto mostra: a=1, b=2, c=3

"""En resumen, las tuplas en Python son colecciones ordenadas e inmutables de elementos.
Son utiles para almacenar datos que no deben cambiar."""