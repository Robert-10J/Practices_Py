""" Realiza una función separar(lista) que tome una lista de números enteros y devuelva 
dos listas ordenadas. La primera con los números pares y la segunda con los números impares."""

list = []
number_elements = int(input("Total elementos >> "))
for lista in range(number_elements):
    elementos = int(input("Ingrese los elementos >> "))
    list.append(elementos)

list_pares = []
list_impares = []

def separar(lista):
    for recorrer in list:
        if list %2 == 0:
            list_pares.append(list)
        else:
            list_impares.append(list)
separar(list)