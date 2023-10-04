from funct_ejercicio2_3 import *

# Exercise 2:
monthly_purchases = [
   ("Ernesto Sabato", 10, 25000, "Calle 12 - 456"),
   ("Roberto Bolaños", 10, 27050, "Calle 10 - 410"),
   ("Ernesto Sabato", 19, 55000, "Calle 12 - 456"),
   ("Jorge Russo", 20, 15000, "Calle 12 - 450"),
   ("Ernesto Sabato", 28, 25000, "Calle 12 - 456"),
   ("Nuria Costao", 1, 40000, "Calle 1 - 416"),
   ("Roberto Bolaños", 10, 25000, "Calle 10 - 410")
]
print(bills(monthly_purchases))

# Exercise 3:
partners = {
   "Socio N°1": ["Amanda Nuñez", "17/03/2009", True],
   "Socio N°2": ["Barbara Molina", "17/03/2009", True],
   "Socio N°3": ["Lautaro Campos", "17/03/2009", True]
}
count = 3

while True:
   print("\n¿Que operación desea realizar?")
   print("1. Cargar socios \n2. Cantidad de usuarios \n3. Pagar Cuotas Adeudadas")
   print("4. Dar de Baja \n5. Mostrar Socios \n6. Modificar fecha erronea \n7. Terminar")
   option = int(input(": "))

   if option == 1: 
      partner = set_partner()
      count += 1
      partners[f"Socio N°{count}"] = partner
   elif option == 2: 
      print(f"Cantidad de socios: {len(partners)}")
   elif option == 3: 
      set_dues(partners)
   elif option == 4: 
      delete_partner(partners)
   elif option == 5:
      show_partners(partners)
   elif option == 6: 
      set_date(partners)
   elif option == 7: 
      break
   else:
      print("Opcion invalida, intente nuevamente")
