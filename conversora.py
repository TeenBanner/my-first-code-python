import os 
os.system("cls")

def conversor_pesos(moneda):
    pesos = int(input("cuantos pesos tienes "))
    dolares =  pesos * moneda
    return dolares

def conversor_euros(moneda):
    euros = int(input("cuantos euros tienes "))
    dolares = euros * moneda 
    return dolares

def conversor_real(moneda):
    real = int(input("cuanto reales tienes "))
    dolar = real * moneda
    return dolar

def conversor_yuanes(moneda):
    yuan = int(input("cuantos yuanes tienes "))
    dolar = yuan * moneda
    return dolar
    

MXN = 1/20
EUE = 1.0759
ARG = 1/290
BRS = 1/50468
CHX =1/71044

print("bienvenido al conversor de pesos a dolares")
print("tenemos conversion de euro a dolar y peso mexicano a dolar")
print("1 para peso mexicano a dolar")
print("2 para euro a dolar")
print("3 para peso argentino a dolar")
print("4 para real brasileño a dolar")
print("5 para yuan a dolar")

opcion = input("cual es tu opcion ")

opcion = int(opcion)





if opcion == 1:
    dolares = conversor_pesos(MXN)
    print(f"tienes {dolares} dolares")

elif opcion == 2:
    dolares = conversor_euros(EUE)
    print(f"tienes {dolares} dolares")

elif opcion == 3:
    dolares = conversor_pesos(ARG)
    print(f"tienes {dolares} pesos dolares")

elif opcion == 4:
    dolares = conversor_real(BRS)
    print(f"tienes {dolares} real")

elif opcion == 5:
    dolares = conversor_yuanes(CHX)
    print(f"tienes {dolares} dolares")

    
else:
    print("eligiste mal escoge 1 para empezar a convertir")
