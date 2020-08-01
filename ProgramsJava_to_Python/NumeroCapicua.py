#Saber si un numero es capicua o no.
num = int(input("Ingrese un numero de 4 cifras: "))

aux = num
um = aux / 1000
aux = aux % 1000
c = aux / 100
aux = aux % 100
d = aux / 10
u = aux % 10
aux = ((um * 1000) + (d * 100) + (c * 10) + u)

if num == aux:
    print("El numero es capicua")
else:
    print("EL numero no es capicua")