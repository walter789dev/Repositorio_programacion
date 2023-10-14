def validate(item):
   if item.isnumeric(): return True
   else: 
      print("No ha ingresado un número")
      return False

"""
# Exercise 1:
I validate that the value entered is numerical and I add it to the list
"""
def add_item_list(lists):
   while True:
      item_list = input("Ingrese un número o 0 para terminar: ")
   
      if validate(item_list):
         if item_list != 0:
            lists.append(int(item_list))
            print("Se ha almacenado correctamente")
         else: break

"""
# Exercise 2
I validate that the entered value is numerical, I verify that it is in the list and I delete it, if not I report that it is not found
"""
def remove_item_list(lists):
   while True:
      item_remove = input("Ingrese un número a eliminar de la lista o 0 para terminar:")

      if validate(item_remove):
         if item_remove in lists:
            lists.remove(int(item_remove))
            print(f"Se ha eliminado la primera aparicion de {item_remove}")
         elif item_remove != 0: 
            print(f"El número no se encuentra en la lista")
         else: break

"""
# Exercise 4:
I request a number from the user to later iterate the list, subtracting the number entered and returning a new list
"""  
def new_list(item, lists):
   new_list = []
   item_repl = int(item)
      
   for i in range(len(lists)): 
      element = lists[i] - item_repl if lists[i] > item_repl else lists[i]
      new_list.append(element)
   return new_list

"""
# Exercise 5:
I iterate the elements of the list, take the first one to compare with the following ones and add the ones that are different. In addition to counting his appearances
"""
def list_tuples(lists):
   list_tuple = []
   list_check = []

   for i in range(len(lists)):
      item = lists[i]
      if item not in list_check:
         list_check.append(item)
         item_count = lists.count(item)
         list_tuple.append((item, item_count))
   return list_tuple

"""
# Exercise 6:
I get the names of the students until I enter x
"""
def get_names(text):
   new_list = []
   
   while True:
      name = input(f"Ingrese nombre de alumno '{text}' o 'X' para terminar: ").title()
      if name != "X": 
         new_list.append(name)
      elif name.title() == "X" and len(new_list) == 0: 
         print("Debe ingresar al menos 1 alumno")
      else: break
   return new_list

"""
I report the names of all primary level students and secondary level students, without repetitions and another arrangement with repeated names
"""   
def repeat_names(list = [], list2 = []):
   names_no_repeat = []
   names_repeat = []
   lists = [list, list2]
   
   for i in range(2):
      for j in range(len(lists[i])): 
         item = lists[i][j]
         if item not in names_no_repeat:
            names_no_repeat.append(item)
         else:
            if item not in names_repeat:
               names_repeat.append(item)
   return [names_no_repeat, names_repeat]

"""
I report which primary level names are not repeated in secondary level names.
"""
def check_names(list, list2):
   new_list = []
   
   for p_name in list:
      val = True
      for s_name in list2:
         if p_name == s_name:
            val = False
            break
      if val and p_name not in new_list: 
         new_list.append(p_name)
   return new_list

"""
# Exercise 7:
I verify that the entered character is in the dictionary, if not I add it. I also count his appearances
"""
def checks_characters(words, dict):
   for i in range(len(words)):
      if words[i] != " ":
         letter = words[i]
         if letter in dict:
            dict[letter] += 1
         else:
            dict[letter] = 1
            
# Exercise 8: In Fixture.py
# Exercise 9: In Memotest.py

"""
# Exercise 10:
I obtain the main diagonal and the inverse diagonal of the matrix that receives as a parameter
"""
def diagonal(matriz):
   matriz_1 = []
   for i in range(len(matriz)):
      for j in range(len(matriz[0])):
         if i == j: matriz_1.append(matriz[i][j])
   return matriz_1
   
def reverse_diagonal(matriz):
   matriz_1 = []
   for i in range(len(matriz) - 1, -1, -1):
      for j in range(len(matriz[0])):
         if i == j: matriz_1.append(matriz[i][j])
   return matriz_1
   
"""
# Exercise 13:
I get the fruits that the user enters, if they already exist, I notify their existence
"""
def get_fruit(fruit):
   while True:
      add_fruit = input("Ingrese una fruta o 'x' para salir: ").title()
      
      if add_fruit != 'X': 
         if add_fruit in fruit:
            print("La fruta ingresada ya existe en el sistema")
         else:
            price_fruit = int(input("Ingrese precio kg de la fruta: "))
            fruit[add_fruit] = price_fruit
      else: break