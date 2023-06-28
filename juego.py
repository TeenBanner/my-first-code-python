import os
os.system("cls")

import random

numero = random.randint(1, 100)
intentos = 15

while(intentos > 0):
    eleccion = int(input("elige un numero "))
    if eleccion > numero:
        print("el numero es mas pequeño ")
        intentos = intentos - 1
    elif eleccion < numero:
        print("el numero es mas grande")
        intentos = intentos - 1
    else:
        print("ganaste")
        break

    if intentos < 0:
        print("se acabaron los intentos")