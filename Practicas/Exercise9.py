#Pedir 3 numeros y determinar cual es el mayor

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1>= num2 and num1 >= num3:
    print(f"El numero {num1} es mayor a los demas")
if num2 >= num1 and num2 >= num3:
    print(f"El numero {num2} es mayor a los demas")
if num3 >= num1 and num3 >= num2:
    print(f"El numero {num3} es mayor a los demas")

