while(True):
    try:
        var = float(input("Number >> "))
        a = 2
        print(f"Resultado {a*var}")
    except:
        print("No se ingreso un dato o el dato ingresado no es valido")
    else:
        print("Correcto")
        break