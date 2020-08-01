""" Haver un programa para ingresar el radio de un circulo y se reporta su area
y la longitud de la circunferencia
area = pi * r^2
lonngitud = 2 * pi * r
"""
import math
radio = float(input("Ingrese el radio del circulo: "))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"EL area del circulo es: {area}")
print(f"La longitud del circulo es: {longitud}")