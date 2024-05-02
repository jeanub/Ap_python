"""
Los metodos de cadenas en python son funciones integradas que se utilizan para
realizar operaciones y manipulaciones en cadenas de texto.
"""


#?Upper(): Devuelve una copia de la cadena con todas las letras en mayusculas.
texto = "hola mundo"
print(texto.upper())#Output "HOLA MUNDO"

#?Lower(): Devuelve una copia de la cadena con todas las en minuscula.
texto = "HOLA MUNDO"
print(texto.lower())#Output "hola mundo"

#?Capitalize(): Este metodo devuelve una copia de la cadena con la primera letra en mayuscula y el resto en minuscula.
texto = "hola mundo"
print(texto.capitalize())#Output "Hola mundo"

#?Find(): Se utiliza para buscar la primera ocurrencia de una subcadena dentro de una cadena
texto = "Hola mundo"
posicion = texto.find("m")
print(posicion)#Muestra el indice donde se encuentra la letra m. "5"

#?Index() Se utiliza para encontrar la primera ocurrencia de una subcadena dentro de una cadena y devuelve el indice de inicio de esa ocurrencia
texto = "Hola mundo"
posicion = texto.index("mundo")
print(posicion)#Output 5

#?Isnumeric(): Se usa para verificar si TODOS los caracteres de una cadena son numericos.
cadena = "12345"
es_numerico = cadena.isnumeric()
print(es_numerico)

#?Isalpha(): Se usa para verificar si todos los carecateres de una cadena son alfabeticas.
cadena = "Hola"
es_alfabetico = cadena.isalpha()
print(es_alfabetico)

#?Count(): Se usa para contar cauntas veces aparece una subcadena en una cadena principal
texto = "hola hola hola"
contador = texto.count("la")
print(contador)#Output 3

#?Len(): Cuenta los caracteres de una cadena, lista, tupla, diccionario, etc.
texto = "hola mundo"
longitud = len(texto)
print(longitud)#Output 10

#?Endswhith(): Verifica si una cadena termina con una subcadena especifica. Retorna True
texto = "Hola mundo"
termina_con = texto.endswith("mundo")
print(termina_con)

#?Startwith(): Verifica si una cadena empieza con una subcadema especifica. Retorna True
texto = "Hola mundo"
empieza_con = texto.startswith("Hola")
print(empieza_con)

#?Replace(): Devuelve una copia de la cadena remplazando todas las ocurrencias de una subcadena con otra subcadena.
texto = "hola mundo"
nuevo_texto = texto.replace("mundo", "amigo")
print(nuevo_texto)#Output "hola amigo"

#?Split(): Divide la cadena en una lista de subcadenas utilizando un separador espeficicado(Por defecto, el espacio en blanco)
texto = "hola,mundo"
palabras = texto.split(",")
print(palabras)#Output ["hola", "mundo"]

#?Title(): Devuelve una copia de la cadena con la primera letra de cada palabra en mayusculas.
texto = "hola mundo"
print(texto.title())#Output "Hola Mundo"

#?Join(): Une una lista de cadenas en una sola cadena utilizando la cadena que llama al metodo como separador.
palabras = ["hola", "mundo"]
texto = ",".join(palabras)
print(texto)#Output "hola,mundo"

