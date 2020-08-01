""" Escribir un programa que tenga 2 listas y que a continuacion, cree las siguientes
listas (en las que no debe haber repeticiones) 

-> Lista de palabras que aparecen en las dos listas
-> Lista de palabras que aparecen en la primera lista, pero no en la segunda
-> Lista de palabras que aparecen en la segunda lista pero no en la primera.
-> Lista de palabras que aparecen en ambas listas"""

lista_1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista_2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminando los elements repetidos en ambas listas
a = set(lista_1)
b = set(lista_2)

union = list(a | b)
solo_A = list(a - b)
solo_B = list(b - a)
interseccion = list(a & b)

print(f"Lista de palabras que aparecen en las dos listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo_A}")
print(f"Lista de las palabras que aparecen en la segunda lista pero no en la primera: {solo_B}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")
