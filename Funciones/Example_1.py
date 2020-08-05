# Funcion que muestra la tabla del 7
num = int(input("Numero a multiplicar >> "))

def tabla_multiplicar():
    for x in range(1, 11):
        print(f"{num} x {x} = {num * x}")

tabla_multiplicar() 

def students():
    print(f"Hi students {num}")

students()