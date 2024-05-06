#Conjuntos:
#?Creando un conjunto con sett{}:+
conjunto = set(["dato de lista 1"])

#?Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2", "dato4",])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#?Teoria de conjuntos:
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#?Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)#True
resultado = conjunto1 <= conjunto2# False

#?Verificando si es un superconjunto
resultado= conjunto1.issuperset(conjunto2)#True
resultado = conjunto2 >= conjunto1#False

#?Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)#Esto es True cuando los valores que se comparan son

print(resultado)