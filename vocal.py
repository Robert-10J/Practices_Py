""" Que indique si un caracter es vocal o no """
letra = input("Caracter --> ").lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"La letra {letra} es vocal")
else:
    print(f"La letra {letra} no es vocal")