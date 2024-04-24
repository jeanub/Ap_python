temp = int(input("Ingrese un valor que quiera convertir:"))
#Funcion 1 de celcius a farenheit
def dc_af(v1):
    resultado = (v1* 9/5) +32
    return resultado
caf = dc_af(temp)
#funcion 2 de farenheit a celcius
def df_ac(v2):
    resultado = (v2-32)*5/9
    return resultado
fac = df_ac(temp)



selec = int(input("A que desea convertir? 'celcius a farenheit= 1 o farenheit a celcius= 2'"))

if selec == 1:
    print("La temperatura en farenheit es de:", caf)
elif selec == 2:
    print("La temperatura en celcius es de:",fac)
else:
    print("FIN")

