#Generador de contraseñas con operaciones matematicas:
"""
El generador de contraseñas solicitara dos datos, el primero sera el tamaño de la contraseña(debera ser mayor a 3).
El segundo dato sera un numero al azar que elija el usuario(de preferencia su numero favorito).
"""
#?Solitar datos:
numero_azar_o_favorito = int(input("Ingre un numero al azar(De preferencia su numero favorito): "))

#?Funcion que genera contraseñas:
def new_password():
    import random#//importando modulo
    import string
    while True:
        try:
            tamaño_de_contraseña = int(input("Ingrese el tamaño de su contraseña: "))
            if tamaño_de_contraseña <= 0:
                print("El tamaño de la contraseña debe ser mayor a cero. Intente nuevamente: ")
            elif tamaño_de_contraseña <3:
                print("El tamaño minimo debe ser mayor a 3.")
            elif tamaño_de_contraseña == 11:
                print("Exelente numero :)")
                break
            else:
                break
        except ValueError:
            print("Por favor, Ingrese un numero válido.")
    azar_de_datos = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(azar_de_datos) for _ in range(tamaño_de_contraseña))
    return password

print(f'Su nueva contraseña es: {new_password()}')

datos_para_indice = new_password



#?La calculadora debera leer los indices de las contraseñas generadas. Y usarlos para realizar operaciones matematicas:
