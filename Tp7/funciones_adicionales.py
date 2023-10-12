def get_numbers(method):
   numb_list = []

   while True:
      number = input("Ingrese un número o 0 para salir: ")

      if number.isnumeric() and number != "0": numb_list.append(int(number))
      elif number == "0": break
      else: print("Dato invalido, intente nuevamente")

   method(numb_list)
   return numb_list

# Exercise 3:
def sort_books(order, field, books):
   new_books = {}
   
   for key, values in books.items():
      for i in range(len(order) - 1, -1, -1):
         if order[i] == values[field]:
            new_books[key] = values
            break
   return new_books

# I get the basic data to create a book and add it to the arrangement
def set_book(books):
   while True:
      title = input("Ingrese nombre del libro: ").lower()
      author = input("Ingrese autor del libro: ").lower()
      year = input("Ingrese año de publicación: ")
      editorial = input("Ingrese nombre de la editorial: ").lower()

      if (len(title) + len(author) + len(editorial)) > 9 and year.isnumeric():
         books[title] = {
            "title": title,
            "author": author,
            "year": int(year),
            "editorial": editorial
         }
         break
      else:
         print("Datos no validos, intente nuevamente")
         
def separate(array):
   a = [] 
   b = []
   
   for item in array:
      if item.isnumeric(): a.append(int(item))
      else: b.append(item)
      
   return [a, b]
   