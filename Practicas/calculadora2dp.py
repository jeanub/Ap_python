#Calculadora
#//Solictar datos:
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

#?Funcion de la primera calculadora:
def calculadora1(valor1, valor2):
    #*funciones lambda de la calculadora:
    seleccionar_operacion = int(input("Selecciona una: 1.porsentaje, 2.Raiz 3.Exponente 4.Elevado a 10: "))
    porsentaje = lambda a,b: a%b 
    raiz = lambda a,b: (a**0.5, b**0.5)
    exponente = lambda a,b: (a**2, b**2)
    elevado_a_10 = lambda a,b: (a**10, b**10)
    #!Seleccion de operacion:
    if seleccionar_operacion ==1:
        print(f'El porsentaje entre esos numeros es:{porsentaje(valor1,valor2)}')
    elif seleccionar_operacion ==2:
        print(f'La raiz de los numeros es: {raiz(valor1,valor2)}')
    elif seleccionar_operacion ==3:
        print(f'el exponente de ambos numero es: {exponente(valor1,valor2)}')
    else:
        print(f"Elevado a 10 los valores son{elevado_a_10(valor1,valor2)}")

#?Funcion de la segunda calculadora:
def calculadora2(valor1,valor2):
    #*Funciones lambda de la calculadora
    suma = lambda a,b: a+b
    resta = lambda a,b: a-b
    multiplicacion = lambda a,b: a*b
    division = lambda a,b: a/b
    #!Seleccion de operaciones
    seleccionar_operacion = int(input("Seleccione una de las operaciones: 1.suma, 2.Resta, 3.Multiplicacion, 4.Division"))
    if seleccionar_operacion == 1:
        print(f'La suma de los numeros es: {suma(valor1,valor2)}')
    elif seleccionar_operacion== 2:
        print(f'La resta de los numeros es: {resta(valor1,valor2)}')
    elif seleccionar_operacion== 3:
        print(f'la multiplicacion de los numeros es: {multiplicacion(valor1,valor2)}')
    else:
        print(f"La division de los numeros es: {division(valor1,valor2)}")

seleccionar = int(input("Seleccione: 1= Calculadora compleja, 2=Calculadora Simple: "))

if seleccionar == 1:
    print(calculadora1(valor1, valor2))
else:
    print(calculadora2(valor1, valor2))

