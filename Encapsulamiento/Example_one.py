class encapsulamiento:

    """ Dos guiones bajos antes del name indican que es privado
    (Solo existe en la clase donde se encuentra) """

    __atri_private = "Atributo privado"
    
    def __function_private(self):
        print("Metodo privado")
    
    def public_atri(self):
        return self.__atri_private

    def public_met(self):
        return self.__function_private()

ob = encapsulamiento()
ob.public_atri()
