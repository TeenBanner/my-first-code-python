import os 
os.system("cls")

def conversor(moneda):
    dolares = int(input("cuantos dolares tienes? "))
    pesos = dolares * moneda
    return pesos

USD = 1
ARS = 290
COP = 4600
MXM =  20

print("!bienvenido al conversor de monedas definitivo¡")
print("elige una de las siguientes opciones de conversion: ")
print("1 - Dolares a peso argentino")
print("2 - Dolares a peso colombiano")
print("3 - Dolares a peso mexicano")
opcion = input("¿cual es tu opcion: ")
opcion = int(opcion)

if opcion == 1:
    pesos_argentinos = conversor(ARS)
    print(f"tienes{pesos_argentinos} pesos ")
elif opcion ==2:
    pesos_colombianos = conversor(COP)
    print(f"tienes{pesos_colombianos} pesos ") 
elif opcion == 3:
   pesos_mexicanos = conversor(MXM)
   print(f"tienes{pesos_mexicanos} pesos ")
else:
    print("¡escrtibe una opcion correcta!")