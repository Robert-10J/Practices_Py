""" Metodos especiales y objetos embebidos"""
class Fabrica:
    
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
    
        print("Se creo el auto ", self.nombre) 
        
    def __del__(self):
        print("Se elimino el auto ", self.nombre)

    def __str__(self):
        return "{} ({})".format(self.nombre, self.tiempo)

class listado:
    autos = []

    def __init__(self, autos = []):
        self.autos = autos

    def fabricar(self, x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)

ob = Fabrica(10, "yo", 4)

l = listado([ob])
l.visualizar()
l.fabricar(Fabrica(15, "Otro yo", 2))
l.visualizar()