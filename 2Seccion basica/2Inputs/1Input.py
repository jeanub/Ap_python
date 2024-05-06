"""
La funcion 'input()' Se utiliza para obtener informacion ingresada por el 
usuario desde el teclado. Esta funcion detiene la ejecucion del programa y 
espera a que el usuario ingrese algun texto('STR') y puede ser almacenado en 
una variable para su posterior uso.
"""

#?Input(): Solicita un dato al usuario y lo almacena como 'STR(String)'
nombre = input("Ingrese su nombre: ")
print("Hola",nombre)

"""
Es importante recordad que todo lo ingresado por el usuario mediante un 'input()'
se trata como una cadena de texto ('STR'), Incluso si el usuario ingresa un numero.
Si necesitas que la entrada sea tratada como un numero, se debe convertir usando
?funciones de conversion de tipos de datos: ('int()', 'float()',etc)
"""
#!Usando las funciones de conversion de tipos de datos.
#?Int():Convierte los datos a valores enteros.
numero = input("Ingrese un numero:")#Se almacena un valor de tipo STR
conversion = int(numero)#Convierte el valor almacenado a tipo entero
print(type(conversion))#Output <class 'int'>

#?Float(): Convierte los valores a numeros con coma
numero = input("Ingrese un valor numerico con coma:")
conversion =float(numero)
print(type(conversion))

