import os
os.system("cls")


eleccion = input("elige tu opcion: ")

if eleccion == "papel" or eleccion == "Papel":
     print("computadora elige tijeras.gana la computadora :)")   
elif eleccion == "piedra"or eleccion == "Piedra":
    print("computadora elge papel. gana la computadora:)")  
elif eleccion == "tijeras"or eleccion == "Tijeras":
    print("computadora elige piedra. gana la computadora")
else: 
    print("elige una opcion correcta")