#Creando las listas
diccionario = {
"nombre": "Jean",
"apellido": "Uribe",
"Cuenta del banco:": "11B"
}

cadena = "Hola Jean"
numeros = [2,5,8,10]
#?Recorriendo diccionarios para obtener las claves:
for key in diccionario:
    print(f'La clave es: {key}')

#?Recorriendo diccionarios con items() para obtener la clave y el valores:
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')


#?Mas iteraciones:
dias_de_la_semana = ["lunes,","Martes","Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for entrenar in dias_de_la_semana:
    if entrenar == "Miercoles":
        continue
    print(f'Voy a entrenar los dias: {entrenar}')

#?Recorrer una cadena de texto:
for letra in cadena:
    print(letra)

#?For en una sola linea de codigo(Duplicandos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)