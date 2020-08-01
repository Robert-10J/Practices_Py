#Solicitar 3 letras e indicar si se repiten al menos dos

let_1 = input("Ingrese la primer letra: ")
let_2 = input("Ingrese la segunda letra: ")
let_3 = input("Ingrese una tercer letra: ")

if let_1 == let_2:
    print(f"La letra uno '{let_1}' y dos '{let_2}' son iguales")
if let_1 == let_3:
    print(f"La letra uno '{let_1}' y tres '{let_3}' son iguales")
if let_2 == let_3:
    print(f"La letra dos '{let_2}' y tres '{let_3}' son iguales")
