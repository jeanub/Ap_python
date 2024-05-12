#Creando una funciones propias:
#?Creando una funcion que genera contraseñas:
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

#?llamando a la funcion:
print(f'Su Nueva contraseña es: {new_password()}')
