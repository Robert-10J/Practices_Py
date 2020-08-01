""" Determinar la solucion para la siguiente operacion:
((3 + 5 x 8) < 3 and ((-6/3 x 4) + 2 < 2)) or (a > b)"""

a = float(input("a -> "))
b = float(input ("b -> "))

resultado = (( 3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)

print(f"El resultado es: {resultado}")