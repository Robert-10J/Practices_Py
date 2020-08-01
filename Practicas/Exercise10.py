#Solicitar una letra e indicar si es una vocal o no

letra = input("Ingrese una letra: ").lower() 
#Con lower se transforma la letra inresada a una minuscula en caso de que se digite una mayuscula

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"La letra {letra} ingresada es vocal")
else:
    print("No es vocal")