"""
El desempaquetado en python es una tecnica que permite asignar los elementos de 
una secuencia (Como una lista o una tupla) a multiples variables de forma rapida
y sencilla. Esta tecnia es muy util cuando se quieren extrar los elementos de una
secuencia y asiganarlos a variables individuales.
"""
#?Creando datos
datos_tupla = ("Jean", "Uribe", 111000)
datos_listas = ["Jean, Axel, Uribe", "Nueva Zelanda", "11Billones"]

#?Desempaquetado 
nombre, apellido, cuenta_bancaria = datos_tupla
nombre_completo, lugar_de_residencia, datos_bancarios = datos_listas

#?Mostrando resultados:
print(nombre, apellido,cuenta_bancaria)
print(nombre_completo, lugar_de_residencia, datos_bancarios)
