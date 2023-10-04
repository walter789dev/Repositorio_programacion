# Exercise 2:

# I store the first invoice as a reference for subsequent invoices.
# If the address matches one of the addresses saved in the list, I add your expenses
# Otherwise, I save it in the list
def bills(bill):
   home = [list(bill[0][2:4])]
   for i in range(1, len(bill)):
      val = True
      
      for j in range(len(home)):
         if bill[i][-1] == home[j][-1]:
            home[j][0] += bill[i][2]
            val = False
            
      if val: home.append(list(bill[i][2:4]))
   return home

# Exercise 3:

# I ask the user to enter their full name, registration date and whether their fees are up to date. 
# I verify that the data is correct, if it is, I add it to the list of partners.
def set_partner():
   name_complete = input("\nIngrese su nombre completo: ").title()
   date = input("Ingrese fecha de ingreso en el siguiente formato 'DD/MM/AAA': ")
   dues = input("¿Lleva las cuotas al dia? S. si, N. no: ").lower()
   
   if len(date.split("/")) != 3:
      print("Formato de fecha incorrecta\n")
   elif dues != 's' and dues != 'n':
      print("No ha señalado si lleva sus cuentas al dia o no\n")
   else:
      dues = True if dues == "s" else False
      print("Se han ingresado los datos correctamente\n")
      return [name_complete, date, dues]
 
# I ask the user for their membership number, I verify that they are on the membership list. 
# I check that if its value is true, 
# I indicate that it does not owe, otherwise, I am informed that I paid correctly.
def set_dues(partners):
   number_partner = int(input("\nIngrese número de socio: "))
   partner = f"Socio N°{number_partner}"
   
   for item in partners:
      if partner == item:
         due = item[-1]
         
         if due:
            print("No tiene cuotas adeudadas")
         else:
            item[-1] = True
            print("Se ha pagado correctamente\n")
            break
   else:
      print("El socio ingresado no existe\n")

# I verify that users with the indicated date are updated to the correct date
def set_date(partners):
   val = False
   for item in partners.values():
      if item[1] == "13/03/2018":
         item[1] = "14/03/2018"
         val = True
   if val:
      print("Se han actualizado las fechas del 13/03/2018 al 14/03/2018")
   else:
      print("\nNo hay socios con la fecha 13/03/2018")
      
# I request the name of the partner, 
# if I find it I delete it, otherwise I indicate that it is not in the system.
def delete_partner(partners):
   name_complete = input("\nIngrese nombre de socio: ").title()
   for i in partners:
      if partners[i][0] == name_complete:
         partners.pop(i)
         print("Se ha eliminado correctamente\n")
         break
   else: 
      print("El usuario ingresado no existe en el sistema\n")

# I display all partners in a readable format for users
def show_partners(partners):
   print("\n")
   for key, value in partners.items():
      print(f"{key}, {value[0]}, ingresó: {value[1]}, cuota al dia: {'SI' if value[2] else 'NO'}")
   print("\n")