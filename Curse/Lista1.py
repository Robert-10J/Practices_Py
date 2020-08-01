#Colecciones --> Listas (Arrays)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for lista in list:
    print(lista, end=" ")

""" 
Una lista puede contener diferentes tipos de datos:
--> Strings
--> int, double
--> Otra lista
--> Booleanos
"""
#Ejemplo
print("\n")
list_2 = ["Python", 5, 10.5, [1, True, 3.89, "Martes"], False]
for lista_2 in list_2:
    print(lista_2, end=" ")