""" Hacer un programa para intercambiar el valod de dos variables.
a = 10 --> a = 5, b = 5 --> b = 10 """
""" a = 10
b = 5

print("El valor inicial de a es: ", a)
print("El valor inicial de b es: ",b)
print(f"El valor de de a ahora es: {b}")
print(f"El valor de b ahora es: {a}") """


#Coreecta

a = input("a --> ")
b = input("b --> ")

a, b = b, a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")