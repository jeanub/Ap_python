#CALCULADORA DE IMC(indice de masa corporal) --> Peso/altura**2

altura = int(input("Ingrese su altura:"))
peso = int(input("Ingrese su Peso:"))

def imc(v1,v2):
    resultado = v1 /v2 **2
    return resultado

idmc = imc(peso, altura)

if idmc < 0.00240:
    print("Estas bajo de peso", idmc)
elif idmc > 0.00243:
    print("Estas en sobre peso")
else:
    print("Estas bien de peso, bien ahi crack")

#Se logro 22/04/2024