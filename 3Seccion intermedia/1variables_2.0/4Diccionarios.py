#Diccionarios
#?Creando diccionarios con dict()
diccionario = dict(nombre="Jean", apellido="Uribe")

#?Las listas no pueden ser claves  y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Jean","Uribe"]): "11B"}

#?Creando un diccionario con fromkeys() con dos parametros
diccionario = dict.fromkeys(["Nombre", "apellido"])

#?Creando diccionarios con fromkeys() cambiando el valor por defector a "Valor"
diccionario = dict.fromkeys(["Nombre", "apellido"], "Valor")
print(diccionario)