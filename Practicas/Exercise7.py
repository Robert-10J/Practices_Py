""" Una tienda ofrece un descuento del 15%  sobre el total de la compra y un cliente
desea saber cuánto deberá pagar finalmente por su compra"""

compra = float(input("Ingrese el total de su compra: "))

descuento = compra * 0.15
total_compra = compra - descuento

print(f"El total de la compra con descuento es: ${total_compra:.2f}")

