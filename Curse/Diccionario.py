""" Coleccion --> Diccionarios
colores = {"blue": "azul", "red": "rojo"}

colores["yellow"] = "amarillo"

del(colores["blue"])
print(colores) """

equipo = {10: "Messi", 7: "Cristiano", 11: "Neymar"}

#print(equipo.get(15, "No existe"))
#print(10 in equipo)

#print(equipo.keys())

#print(equipo.values())

#print(equipo.items())

print(len(equipo))

equipo.clear()
print(equipo)