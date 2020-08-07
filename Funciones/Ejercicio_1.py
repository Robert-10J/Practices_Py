""" Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo 
de 15 de base y 10 de altura: """

area_rect = float(input("Area del rectangulo >> "))
base_rect = float(input("Base del rectangulo >> "))

def area_rectangulo(base, altura):
    return base * altura

resultado = area_rectangulo(area_rect, base_rect)
print(f"El area es {resultado}")