""" Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite 
superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite. """

num_1 = int(input("Numero 1 >>"))
num_2 = int(input("Numero 2 >> "))
num_3 = int(input("Numeor 3 >> "))

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero 
resultado = recortar(num_1, num_2, num_3)
print(resultado)