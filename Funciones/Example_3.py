""" num_1 = int(input("Numero 1 >> "))
num_2 = int(input("Numero 2 >> ")) """

def nulos(x = None, y = None):
    if x == None or y == None:
        print("No hay datos")
        return
    return x + y

nulos()
