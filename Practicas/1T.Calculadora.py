#Calculadora simple de 4 operaciones.
#?Solicitar datos
seleccionar_operacion=int((input("Selecciones una operacion: 1.Suma, 2.Resta, 3.Multiplicacion, 4.Division: ")))
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

#?Crear las funciones: 
suma = lambda a,b: a+b
resta = lambda a,b: a-b
multi = lambda a,b: a*b
division = lambda a,b: a/b

if seleccionar_operacion ==1:
    print(f'La suma es:{suma(valor1,valor2)}')
elif seleccionar_operacion ==2:
    print(f'La resta es:{resta(valor1,valor2)}')
elif seleccionar_operacion == 3:
    print(f'La multiplicacion es:{multi(valor1,valor2)}')
else:
    print(f'La division es:{division(valor1,valor2)}')

