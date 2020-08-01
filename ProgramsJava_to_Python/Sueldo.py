""" Dado como dato el tiempo de servicio de un trabajador considere el aumento del 15% si la 
categoria del trabajador es A, 12% en caso de que la categoria sea B, si la categoria es C un
10% y para la categoria D"""

categoria = input("Ingrese su categoria A, B, C: ").lower()
sueldo = float(input("Ingrese su sueldo: "))

if categoria == 'a':
    op = sueldo * 0.15
    aumento = sueldo + op
    print(f"Su sueldo con aumento es: {aumento:.2f}")
if categoria == 'b':
    op = sueldo * 0.12
    aumento = sueldo + op
    print(f"Su sueldo con aumento es: {aumento:.2f}")
if categoria == 'c' or categoria == 'd':
    op = sueldo * .10
    aumento = sueldo + op
    print(f"Su sueldo con aumento es de: {aumento}")