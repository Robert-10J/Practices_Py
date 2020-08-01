#Calcular area de un triangulo dada una formula
import math

base = float(input("Ingrese la base del triangulo: "))
lado = float(input("Ingrese el lado 1: "))
lado_2 = float(input("Ingrese el lado 2: "))

s = (base + lado + lado_2) / 2
area = math.sqrt(s * (s - base) * (s-lado) * (s - lado_2))

print(f"El area del triangulo es: {area:.2f}")