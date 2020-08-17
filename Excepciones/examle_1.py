""" Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún 
elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo 
ValueError que debes capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego 
muestra su contenido. """

lis = []
n_elementos = int(input("Ingrese el total de elementos >> "))

def agregar_una_vez(lista, el):
    
    for x in range(n_elementos):
        element = input("Elemento >> ")
        lis.append(element)
    
    return lis

result = agregar_una_vez(lis, n_elementos)
print(result)