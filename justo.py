import os
os.system("cls")

import random



puntos = 0
intentos = 3

print("bienvenido al piedra papel o tijera")
print("escoge 1 para piedra")
print("escoge 2 para papel")
print("escoge 3 para tijera")

eleccion = int(input("escoge una opcion "))
eleccion_pc = random.randint(0, 3)

while(intentos > 0 ):
    if eleccion == 1 & eleccion_pc == 1:
        print("elegiste piedra pc elige piedra EMPATE")
        intentos = intentos - 1

    elif eleccion == 2 & eleccion_pc == 2:
        print("elegiste papel pc elige papel EMPATE")
        intentos = intentos - 1

    elif eleccion == 3 & eleccion_pc == 3:
        print("elegiste tijera pc elige tijera EMPATE")
        intentos = intentos - 1

    elif eleccion == 1 & eleccion_pc == 3:
        print("elegiste piedra pc elige tijera GANASTE")
        

    elif eleccion == 2 & eleccion_pc == 1:
        print("elegiste papel pc elige piedra GANASTE")
        

    elif eleccion == 3 & eleccion_pc == 2:
        print("elegiste tijera pc elige papel GANASTE")
        

    elif eleccion == 1 & eleccion_pc == 2:
        print("elegiste piedra pc elige papel PERDISTE")
        intentos = intentos - 1
    
    elif eleccion == 2 & eleccion_pc == 3:
        print("elegiste papel pc elige tijera PERDISTE")
        intentos = intentos - 1

    elif eleccion == 3 & eleccion_pc == 1:
        print("elegiste tijeras pc elige piedra PERDISTE")

        break

    if intentos < 0:
        print("Perdiste tus 3 oportunidades ¡BUENA SUERTE LA PROXIMA VEZ!")


    
