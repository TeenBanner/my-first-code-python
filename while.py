import os
os.system("cls")

i = 0
# el ciclo de abajo imprime los numeros del 1 al 5

while(i < 5):
    if i == 3:
        i = i + 1
        continue   
    print(f"Hola en este momento  i vale {i}")
    i = i + 1 