""" Escriba un programa que pida dos números enteros y que calcule 
su división, escribiendo si la división es exacta o no. """

dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

if dividendo % divisor == 0:
    print("La division es exacta")
else:
    print("Division inexacta")
