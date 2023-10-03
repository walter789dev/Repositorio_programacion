# Exercise 1:
def verify_dni(dni):
   v_dni = str(dni)
   return v_dni.isnumeric() and (len(v_dni) == 7 or len(v_dni) == 8)

# # Exercise 2: 
def long_last_word(word):
   word = word.strip()
   words = word.split()
   return len(words[-1])

# Exercise 3:
def identify(name, dni):
   info_name = ""
   if name.count(", ") == 0: info_name = name.split() 
   else: info_name = name.split(", ")
   return f"{info_name[0]}{len(info_name[-1])}{dni[0:3]}"

# Exercise 4:
multiple = lambda numb1, numb2: f"{numb1} es multiplo de {numb2}" if numb1 % numb2 == 0 else f"{numb1} no es multiplo de {numb2}"

# Exercise 5: 
medium_temp = lambda t_max, t_min: (t_max + t_min) / 2

# Exercise 6:
def space_text(text):
   new_text = ""
   for i in range(len(text)):
      if text[i] != " ": 
         new_text += f"{text[i]} "
      else: 
         new_text += text[i]
   return new_text

# Exercise 7:
def min_max(numbers):
   max, min = [0, 0]
   for i in range(len(numbers)):
      if i == 0:
         min = numbers[i]
      if numbers[i] > max: max = numbers[i]
      if numbers[i] < min: min = numbers[i]
   return [max, min]

# Exercise 8:
import math

def perimeter_area(r):
   p = round(2 * math.pi * r, 2)
   a = round(math.pi * math.pow(r, 2), 2)
   return [p, a]

# Exercise 9:
def login(name, passw):
  if name != "usuario1" and passw != "asdasd":
     return False
  print("Se ha logeado con exito")
  return True

# Exercise 10:
def discount(products):
   total = 0
   for item in products.values():
      total += item[0] - (item[1] * item[0] / 100)
   return total

# Exercise 11:
aplicate_func = lambda list, funct: funct(list)

def dobule_list(list):
   new_list = []
   for i in range(len(list)):
      new_list.append(list[i] * 2)
   return new_list

def multiple_next(list):
   new_list = []
   for i in range(len(list)):
      if (i + 1) == len(list):
         new_list.append(list[i] * list[0])
      else:
         new_list.append(list[i] * list[i + 1])
   return new_list

def multiple_previous(list):
   new_list = []
   for i in range(len(list)):
      if i == 0:
         new_list.append(list[i] * list[-1])
      else:
         new_list.append(list[i] * list[i - 1])
   return new_list

# Exercise 12: 
def info_words(phase):
   words = phase.split()
   long_words = []
   
   for i in range(len(words)):
      long_words.append(len(words[i]))
      
   return dict(zip(words, long_words))

# Exercise 13:
module_vector = lambda a, b: round(math.sqrt(math.pow(a, 2) + math.pow(b, 2)), 2)

# Exercise 14:
def prime_number(num):
   for n in range(2, num):
      if num % n == 0:
         return False
   return True
   
# Exercise 15:
def factorial(numb):
   fact = 1
   for i in range(numb, 1, -1):
      fact *= i
   return fact
      
# Exercise 16:
def count_digit(numb, digit):
   count = 0
   str_numb = str(numb)
   str_digit = str(digit)
   
   for i in range(len(str_numb)):
      if str_numb[i] == str_digit: count += 1
   return count

# Exercise 17:
def sum_digit(numb):
   total = 0
   str_numb = str(numb)
   for i in range(len(str_numb)):
      total += int(str_numb[i])
   return total
  

