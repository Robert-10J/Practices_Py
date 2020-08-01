""" Programa que solicite 2 numeros y revise cual de ellos es par oh si ambos lo son"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 % 2==0 and num2 % 2==0:
    print("Ambos numeros son pares")
if num1 % 2==0 and num2 % 2!= 0:
    print(f"{num1} es par")
if num1 % 2!=0 and num2 % 2==0:
    print(f"{num2} es par")
else:
    print("Ambos numeros son impares")