try:
    a = float(input("Numero >> "))
    r = 10/a
    print(r) 
except TypeError:
    print("Debe ser numero no letra")
except ValueError:
    print("Ingreso una letra no numero")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except Exception as x:
    print(type(x).__name__)