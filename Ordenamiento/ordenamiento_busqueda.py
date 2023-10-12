from funciones_orden import *

def ordering():
   numb_list = []
   
   while True:
      number = input("Ingrese un número o 0 para salir: ")
      
      if number.isnumeric() and number != "0": numb_list.append(int(number))
      elif number == "0": break
      else: print("Dato invalido, intente nuevamente")
   
   while True:
      option = input("¿Con que método desea ordenarlos?: \n1.Burbuja, 2. Selección, 3. Inserción, 4. Mezcla \n: ")
      
      if option.isnumeric():
         option = int(option)
         if option <= 4 and option >= 1:
            if option == 1: ord_buble(numb_list)
            elif option == 2: ord_selection(numb_list)
            elif option == 3: ord_insert(numb_list)
            elif option == 4: merge_sort(numb_list)
            break
         else: print("Opcion invalida, intente nuevamente")
      else: print("Dato invalido, intente nuevamente")
      
   print(f"Números ordenados: {numb_list}")
      
   