#Recibir por posicion
""" def argu(*tu):
    for tus in tu:
        print(tus)
argu("Python", 'Hi', 10) """

#Por nombre
def ejemplo(*tu, **lo):
    b = 0 
    for tus in tu:
        b += tus
    print(b)
    for x in lo:
        print(x, " ", lo[x])

ejemplo(1, 2, 3, 4, pyton = "Student", calificacion = [9, 8, 7])