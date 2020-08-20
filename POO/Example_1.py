class Auto:

    Rojo = False

    def __init__(self, puertas = None, color = None):
        self.puertas = puertas
        self.color = color

        if puertas is not None and color is not None:
            print(f"Se creo un auto con {puertas} puertas y color {color}")

    def Fabricar(self):
        self.Rojo = True

    def confirmar_fabricacion(self):
        if (self.Rojo):
            print("Auto a sido coloreado")
        else:
            print("Aun no se a pintado")

autos = Auto("2", "Rojo")
autos.confirmar_fabricacion()
autos.Fabricar()
autos.confirmar_fabricacion()