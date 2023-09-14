# I store main dishes and drinks in a list
dishs = ["Ravioles", "Ñoquis", "Capeletis", "Spaguettis", "Sorretinos"]
drinks = ["Vino", "Agua", "Cerveza", "Soda"]

order = "" # I save the main dish and the drink selected by the person

print("¡¡ Bienvenidos al restaurante de pastas !!")
count_person = int(input("Ingrese cantidad de personas a ingresar: "))

for i in range(count_person):
    print(f"\nPersona {i + 1}: ¿Que desea comer hoy?")

    while True: # verified that the user enters a valid number
        option = int(input(f"1. {dishs[0]}, 2. {dishs[1]}, 3. {dishs[2]}, 4. {dishs[3]}, 5. {dishs[4]}: "))

        if option <= 0 or option >= 6: 
            print("\nOpciòn invalida, por favor seleccione un platillo valido \n")
        else: 
            order += "Plato Principal: " + dishs[option - 1] # I insert the chosen option
            break

    print("\n¿Desea acompañarlo con una bebida?")
    drink = input("S. Si, N. No: ").lower()
    
    while drink == "s": # verified that the user enters a valid number
        option = int(input(f"\n1. {drinks[0]}, 2. {drinks[1]}, 3. {drinks[2]}, 4. {drinks[3]}: "))

        if option <= 0 or option >= 5: print("\nOpciòn invalida, por favor seleccione una bebida valida \n")
        else: 
            order+= ", Bebida: " + drinks[option - 1] # I insert the chosen option
            break
    
    print(f"\nSu pedido: {order}")
    order = ""
