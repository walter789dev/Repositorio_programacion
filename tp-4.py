x = 0

while x <= 30:
    if x == 4 or x == 6 or x == 10:
        print(f"The value {x} of x is skipped")
        x += 1
        continue
    elif x == 15:
        print(f"The execution of the loop was broken when x was {x}")
        break
    print(f"The value of the loop is: {x}")
    x += 1

# Exercise 1
words = []

while True:
   line = input("Ingrese una linea o deje una línea en blanco para terminar: ")
   if len(line) == 0: break
   else: words.append(line.upper())

print("\n".join(words))

# Exercise 2:
bank = 0

while True:
   print("Ingrese la letra operación que desea realizar, seguido de un espacio y el monto")
   answer = input("D para depositar o R para retirar: ").upper()
   if len(answer) == 0:
      break
   else:
      movement = answer[0]
      money = int(answer[2:len(answer)])
      if movement == "D":
         bank = bank + money
      elif movement == "R":
         if bank <= 0: 
            print("No posee el monto requerido.") 
         else:
            bank = bank - money
      else:
         print("Operación Incorrecta. Intente de nuevo.")
         
print(f"Monto: {bank}")

# Exercise 3:
count = 0

while True:
   number = int(input("Ingrese un numero mayor a 1 o 0 para terminar: "))
   if number == 0: break
   else:
      val = False
      for n in range(2, number):
        if number % n == 0:
            val = True
      if val : count += 1
      
print(f"Se han ingresado {count} numero/s primo/s")

# Exercise 4:
year_1 = int(input("Ingrese un año: "))
year_2 = int(input("Ingrese otro año: "))

if year_2 > year_1:
   aux = year_1
   year_1 = year_2
   year_2 = aux

while year_2 < year_1:
   if year_2 % 4 == 0 and (year_2 % 100 != 0 or year_2 % 400 == 0):
      print(f"Año Bisiesto: {year_2}")
   elif year_2 % 10 == 0:
      print(f"Año Multiplo de 10: {year_2}")
   year_2 += 1


# Exercise 5:
for i in range(21):
   if i%2 != 0:
      continue
   print(i)
   
# Exercise 6:
import random

n_jump = random.randint(0, 10)
n_limit = random.randint(0, 100)

numbers_list = [i for i in range(0, n_limit, n_jump)] 
search_number = int(input("Ingrese numero a buscar: "))
val = False

for i in range(len(numbers_list)):
    if numbers_list[i] == search_number:
        val = True
        break

if val: print(f"Numero encontrado: {search_number}")
else: print(f"El numero a buscar no se encuentra")

# Exercise 7:
while True:
   option = int(input("Ingrese una opcion: 1, 2, 3 o 0 para terminar: "))
   if option == 1: print("¡¡ Que agradable eleccíon !!")
   elif option == 2: print("¡¡ Un buen número par !!")
   elif option == 3: print("No hay dos sin tres")
   elif option == 0: break

