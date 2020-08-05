while True:
    print("""
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir""")

    opcion = int(input("Opcion >> "))

    if opcion >= 1 and opcion <= 4:
        print("Ingrese dos numeros >>  ")
        num_1 = float(input())
        num_2 = float(input())

        if opcion == 1:
            resultado = num_1 + num_2
            print(f"Resultado {resultado}") 
        
        elif opcion == 2:
            resultado = num_1 - num_2
            print(f"Resultado {resultado}") 
        
        elif opcion == 3:
            resultado = num_1 * num_2
            print(f"Resultado {resultado}") 
        
        elif opcion == 4:
            resultado = num_1 / num_2
            print(f"Resulado {resultado}")    

        elif opcion == 5:
            exit()
        #exit()

    else:
        print("Adios")