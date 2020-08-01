""" Hacer un programa que simule un cajero automático con un sueldo inicial de $1000 y tendra el 
siguiente menu de opciones:
1.- Ingresar dinero a la cuenta.
2.- Retirar dinero de la cuenta.
3.- Mostrar dinero disponible.
4.- Salir.
"""
saldo = 1000
print("""1.- Ingresar dinero a la cuenta.
2.- Retirar dinero de la cuenta."
3.- Mostrar dinero disponible."
4.- Salir.""")

opcion = int(input("\nIngrese la opcion que desea: "))
while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
    print("Opcion no valida")
    opcion = input("\nIngrese la opcion que desea: ")

if opcion == 1:
    ingreso = float(input("Ingrese el total que desea ingresar a la cuenta: $"))
    saldo += ingreso
    print(f"Su saldo de ahora es: ${saldo}")

elif opcion == 2:
    retiro = float(input("Ingrese el monto a retirar: $"))
    if retiro > saldo:
        print("La cantidad a retirar no esta disponible en su cuenta!")
    else:
        saldo -= retiro
        print(f"El saldo de su cuenta ahora es: ${saldo}")

elif opcion == 3:
    print(f"El saldo de su cuenta es: ${saldo}")

elif opcion == 4:
    print("Gracias por su preferencia! Hasta la proxima")