#Ingresar un numero entero de 3 cifras y obtener el inverso de dicho numero

numero = int(input("Ingrese un numero: "))

cent = numero / 100
rest = numero % 100
dec = numero / 10
uni = rest % 10

print(f"La unidad es {uni}")
print("El numero inverso es", uni, dec, cent)
