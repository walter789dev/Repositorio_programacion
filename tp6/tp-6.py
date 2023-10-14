from funcionesTp6 import *
from memotest import memotest
from fixture import fixture, team_champion

lists = []
add_item_list(lists) # Exercise 1:
remove_item_list(lists) # Exercise 2:
      
# Exercise 3:
sum_total = 0
for i in lists: sum_total += i
print(f"La sumatoria de la lista es de: {sum_total}")

# Exercise 4:
while True:
   item_replace = input("Ingrese un número para modificar la lista: ")

   if validate(item_replace):
      lists_2 = new_list(item_replace, lists)
      for i in lists_2: print(i)
      break

print(list_tuples(lists)) # Exercise 5

# Exercise 6:
primary = get_names(text="primaria")
secondary = get_names(text="secundaria")
no_repeat, repeat = repeat_names(list=primary, list2=secondary)

print("Nombres de alumnos de primaria y secundaria sin repetir: ")
for i in no_repeat: print(i)

print("Nombres de alumnos repetidos: ")
for i in repeat: print(i)

print("Nombres de alumnos de primaria que no coinciden con los de secundaria: ")
list = check_names(primary, secondary)
for i in list: print(i)

# Exercise 7:
list_string = []
list_characters = {}
i = 0

while i < 50:
   text = input(f"Ingrese su palabra/texto número {i + 1}: ").lower()
   
   if text != "" or text != " ":
      list_string.append(text)
      i += 1
   else:
      print("No ha ingresado ningun caracter")

for i in range(len(list_string)): 
   checks_characters(list_string[i], list_characters)
   
for key, value in list_characters.items():
   print(f"'{key}': {value}")

"""
# Exercise 8:
Sabia que se hacia con listas pero me inspire y lo hice asi para que quedara más bonito y estructurado 
"""
teams = {}
count_team = 10
i = 0
# get soccer teams
while i < count_team:
   team = input("Ingrese nombre del equipo: ").title()
   if team not in teams:
      # I initialize the basic structure for each team
      teams[team] = {
         "points": 0,
         "victories": 0,
         "defeats": 0,
         "ties": 0,
         "goals in favor": 0,
         "goals against": 0
      }
      i += 1
   else:
      print("El equipo ya se encuentra registrado")
      
# the function that contains all the programming of the football match calendar
fixture(teams)

# I show information about the performance of all equipment
for team in teams:
   print(f"El equipo '{team}' ha obtenido: ")
   print(f"Puntos: {teams[team]['points']}")
   print(f"Victorias: {teams[team]['victories']}")
   print(f"Derrotas: {teams[team]['defeats']}")
   print(f"Empates: {teams[team]['ties']}")
   print(f"Diferencia de Gol: {teams[team]['goals in favor'] - teams[team]['goals against']}\n")

team_champion(teams)

# Exercise 9:
memory = [
   [12, 50, 70, 29],
   [25, 77, 10, 57],
   [50, 70, 77, 10],
   [29, 12, 57, 25]
]

memotest(memory, 8)

# Exercise 10:
matriz = []
row = int(input("Ingrese cantidad de filas: "))

for i in range(row):
   matriz_1 = []
   for j in range(row):
      number = int(input(f"Ingrese numero para fila {i + 1}, columna {j + 1}: "))
      matriz_1.append(number)
      
   matriz.append(matriz_1)

print(f"Su diagonal es: {diagonal(matriz)}")
print(f"Su diagonal inversa es: {reverse_diagonal(matriz)}")

# Exercise 11:
money = {
   'Euro': "€",
   'Dolar': "$",
   'Yen': "¥"
}

get_money = input("Ingrese una divisa: ").capitalize()
if get_money in money:
   print(f"El simbolo de su divisa es: {money[get_money]}")
else:
   print("La divisa ingresada no es valida")

# Exercise 12:
dict_info = {}

dict_info["name"] = input("Ingrese su nombre: ")
dict_info["age"] = int(input("Ingrese su edad: "))
dict_info["direction"] = input("Ingrese su dirección: ")
dict_info["phone"] = int(input("Ingrese su telefono: "))

print(f"{dict_info['name']} tiene {dict_info['age']} años, vive en {dict_info['direction']} y su número es {dict_info['phone']}")

# Exercise 13:
fruit = {}
get_fruit(fruit)

user_fruit = input("Ingrese una fruta: ")
if user_fruit in fruit:
   while True:
      kg = int(input("Ingrese cantidad de kg solicitados: "))
      
      if kg >= 1:
         print(f"{kg} kg de {user_fruit}: ${fruit[user_fruit] * kg}")
      else:
         print("Valor de kg invalido")
else:
   print("La fruta solicitada no se encuentra en nuestro catalogo")
