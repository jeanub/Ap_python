#Datos
#?Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#?Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#?Diferencia de duracion.
diferencia_con_min = 100 - dalto_curso /otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 //otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso /otros_cursos_promedio * 100

#?Calculando porsentaje de tiempo removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 //crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso *1000 //crudo_dalto / 10
print("-----------------------------")
print("El curso de dalto dura")
#?Mostrando diferencias de duracion (Ejercicio A)
print(f'- un {diferencia_con_min}% menos que el mas rapido')
print(f'- un {diferencia_con_max}% mas que el mas lento')
print(f'- un {diferencia_con_promedio}% menos que el promedio')
print("-----------------------------")

#?Mostrando la cantidad de espacios vacios que se remueven (Ejercicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio} de tiempo vacio")
print(f"Este curso elimino el  {tiempo_vacio_dalto} de tiempo vacio")
print("-----------------------------")


#?Mostrando diferencia si los cursos duraran 10 horas
print(f"ver 10 horas de otros cursos equivale a ver:  {dalto_curso*100//otros_cursos_promedio/10} horas de este curso\n"
      f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio*100 // dalto_curso/10}")

print("------------------------Ejercicio 2-----------------------------------")

frase = input("Decime alguna frase y calculo cuanto tardarias si tuvieras que decirlo: ")
plabras_separadas = frase.split(" ")
cantidad_de_palabras = len(plabras_separadas)
print(f"Dijiste: {cantidad_de_palabras} palabras, tardarias: {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en: {cantidad_de_palabras*100//2*1.3} Segundos")
if cantidad_de_palabras >120:
    print("no te pedi un testamento maquina")