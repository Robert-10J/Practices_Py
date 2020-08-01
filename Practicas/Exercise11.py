""" Construir un programa que simule el funcionamiento de una calculadora que puede
realizar las cuatro operaciones aritmeticas basicas(suma, resta, multiplicación y division)
El usuario debe especificar la operacion con el primer caracter del nombre de la operación
"""
    #######################################
    # S, s -> Suma
    #R, r -> Resta
    #P, p, M, m -> Multiplicacion
    #D, d -> Division
    #######################################

opcion = input("Ingrese la inicial del nombre de la operacion que desea realizar: ").lower()

if opcion == 's':
    num1 = float(input("Ingrese el primer numero a sumar: "))
    num2 = float(input("Ingrese el segundo numero a sumar: "))
    suma = num1 + num2
    print(f"El resultado de la suma es = {suma}")

if opcion == 'r':
    num1 = float(input("Ingrese el primer numero a restar: "))
    num2 = float(input("Ingrese el segundo numero a restar: "))
    resta = num1 - num2
    print(f"El resultado de la esta = {resta}")

if opcion == 'p' or opcion == 'm':
    num1 = float(input("Ingrese el primer numero para la multiplicacion:"))
    num2 = float(input("Ingrese el segundo numero a multiplicar: "))
    multi = num1 * num2
    print(f"El resultado de la multiplicacion es = {multi}")

if opcion == 'd':
    num1 = float(input("Igrese el primer numero para dividir: "))
    num2 = float(input("Ingrese el segundo numero a dividir: "))
    div = num1 / num2
    print(f"El resultado de la division es = {div}")