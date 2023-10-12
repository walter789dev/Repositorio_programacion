from funciones_orden import *
from funciones_adicionales import *

numb_list = []
"""
# Exercise 1:
I receive the numbers entered by the user and store 
them in an array and then sort them using the bubble method.
"""
numb_list = get_numbers(ord_buble)
print(f"Numeros ordenados: {numb_list}") 

"""
# Exercise 2:
I receive the words entered by the user, 
store them in an array and then sort them using the select method
"""
words_list = []

while True:
   text = input("Ingrese un palabra o 'x' para salir: ").lower()
   if text != 'x': words_list.append(text)
   elif text == 'x': break
   
ord_selection(words_list)
print(f"Palabras ordenadas: {words_list}")

# Exercise 3:
books = {} # I store the books entered by the user
pre_search = [] # I store the values that are going to be sorted
field = "" # I store the field that will sort the books

while True:
   add_book = input("¿Desea ingresar un libro?: S. si, N. no: ").lower()
      
   #I verify that the data entered is valid
   if not(add_book.isnumeric()):
      # If they are valid, I send the data to the function and create a new book
      if add_book == 's': set_book(books)
      elif add_book == 'n': break
      else: print("Opcion invalida, intente nuevamente")
   else: print("Dato invalido, intente nuevamente")

while True: # I show the valid options to order the books
   option = input("¿Como desea ordenarlos?: \na.Por Titulo, b. Por Autor, c. Por año, d. Por editorial \n: ").lower()
   
   if not(option.isnumeric()):
      if option <= 'd' and option >= 'a':
         if option == 'a':
            # If the option is a, I only need to obtain the keys and assign the field that I will use to sort
            pre_search = list(books.keys())
            field = "title"
         elif option == 'b':
            # I get the authors entered by the user
            for book in books: pre_search.append(books[book]["author"])
            field = "author"
         elif option == 'c':
            # I get the years of publication entered by the user.
            for book in books: pre_search.append(books[book]["year"])
            field = "year"
         elif option == 'd':
            # I get the editorials
            for book in books: pre_search.append(books[book]["editorial"])
            field = "editorial"
         break   
      else: print("Opcion invalida, intente nuevamente")
   else: print("Dato invalido, intente nuevamente")

# Based on the values of the fields that are going to be sorted, I am going to use them as a basis to sort the books
ord_selection(pre_search)
books = sort_books(pre_search, field, books)
         
print("Libros ordenados: ")
for book in books:
      print(books[book])

# Exercise 4:
words_list = []
long_list = []

while True:
   text = input("Ingrese un palabra o 'x' para salir: ").lower()
   if text != 'x' and not(text.isnumeric()): 
      words_list.append(text)
      long_list.append(len(text))
   elif text != 'x' and text.isnumeric():
      print("El dato ingresado no es una palabra, intente nuevamente")
   elif text == 'x': 
      break
   
ord_selection(long_list)
new_list_words = []

for i in long_list:
   for j in words_list:
      if i == len(j) and (j not in new_list_words):
         new_list_words.append(j)

print(f"Palabras ordenadas: {new_list_words}")

# Exercise 5:
numb_list = get_numbers(ord_buble)
numb_list.reverse()
print(f"Numeros ordenados de forma descendente: {numb_list}") 

# Exercise 6:
numb_list = get_numbers(ord_count)
print(f"Numeros ordenados: {numb_list}") 

# Exercise 7:
list = []

while True:
   item = input("Ingrese un número o una palabra o 'x' para salir: ").lower()
   
   if item != 'x': list.append(item)
   elif item == 'x': break
   
numbers, words = separate(list)
ord_selection(numbers)
ord_selection(words)

numbers += words
print(f"Arreglo ordenado: {numbers}")
   
# Exercise 8:
numb_list = get_numbers(merge_sort)
print(f"Numeros ordenados: {numb_list}") 
