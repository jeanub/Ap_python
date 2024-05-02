#En Python, Los tipos de datos se dividen en varios grupos Principales:

#!1.Numeros: 
#?int(enteros): Representa numeros enteros positivos o negativos sin decimales.
x = 10
#?Float(flotantes): Representan numeros con decimales.
y = 3.14

#!2.Booleanos:
#?Bool: Representan valores booleanos True(verdadero) o False(falaso).
is_valid = True
is_not_valid = False

#!3.Secuencias:
#?Str(Cadenas de texto): Representan texto, encerrado entre comillas simples('') o dobles("")
menssage = "Hola,¿ya lograste tus metas?"#29/04/2024
#?Bytes: Representa una secuencia de bytes. Es inmutable y se usa a menudo para datos binarios.
data = b"01010110"
#?Bytearray: Similar a bytes, pero mutables.
mutable_data = bytearray(b"Hello")
#?List(Listas): Representan una secuencia mutable de elementos.
numbers = [1,2,3,4,5]
#?Tuple(tuplas): Representan una secuencia inmutable de elementos.
coordinates = (10,20)

#!4.Conjuntos:
#?Set(conjuntos): Representa una coleccion no ordernada de elementos únicos.
unique_numbers= (1,2,3,4,5)
#?Frozenset: Similar a set, pero inmutable.
inmutable_set = frozenset({1,2,3})

#!5.Diccionarios:
#?Dict(Diccionarios): Representa una colección de pares clave-valor.
person = {"Name": "Jean", "Age": 22, "City": "San Rafael"}
