#Eliminar elementos repetidos de una lista

lista = {1, 2, 3, "Robert", 2, 2, 3, "Robert", 4}

#Se transforma la lista a un conjunto, luego de esto el conjunto se vuelve a transformar en una lista.
lista = list(set(lista))
print(lista)