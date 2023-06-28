import os
os.system("cls")

eleccion = input("ingresa la contraseña ")

if eleccion == "ponchito" or eleccion == "papa":
  print("acceso concedido")
else:
  print("acceso denegado")

if eleccion == "ponchito" or eleccion == "papa":
   
    print("!bienvenido al conversor de monedas definitivo¡")
print("elige una de las siguientes opciones de conversion: ")
print("1 - Dolares a peso argentino")
print("2 - Dolares a peso colombiano")
print("3 - Dolares a peso mexicano")

USD = 1
ARS = 290
COP = 4600
MXM =  20
opcion = input("¿cual es tu opcion: ")

opcion = int(opcion)

if opcion == 1:
    dolares = int(input("cuantos dolares tienes? "))
    pesos = dolares * ARS
    print(f"tienes{pesos} pesos ")
elif opcion ==2:
    dolares = int(input("cuantos dolares tienes? "))
    pesos = dolares * COP
    print(f"tienes{pesos} pesos ")
elif opcion == 3:
    dolares = int(input("cuantos dolares tienes? "))
    pesos = dolares * MXM
    print(f"tienes{pesos} pesos ")
else:
    print("¡escrtibe una opcion correcta!")

    