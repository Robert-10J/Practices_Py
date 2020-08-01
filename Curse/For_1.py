#Tablas de multiplicar
numero = int(input("Ingrese un numero--> "))
mult = int(input("Limite a multiplicar --> "))
for i in range(1, mult + 1):
    print(f"{numero} x {i} = {numero * i}")