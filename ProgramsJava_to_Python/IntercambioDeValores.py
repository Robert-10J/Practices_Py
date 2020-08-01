""" Programa que intercambie valores A, B y C, el valor de B se almacene en A,
B obtenga el valor de C y C obtenga el valor de A  """

a = input("Ingrese el valor para A: ")
b = input("Ingrese el valor para B: ")
c = input("Ingrese el valor para C: ")

aux = a
a, b = b, a
b, c = c, b
c = aux

print(f"El valor de A ahora es {a}")
print(f"El valor de B ahora es: {b}")
print(f"El valor de C ahora es: {c}")