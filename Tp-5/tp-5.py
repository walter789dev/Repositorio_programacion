from funcionesTp5 import *

# Exercise 3: 
while val == 0:
   while True: 
      name_partner = input("# Si tiene más de un nombre, debe colocarlos seguidos de comas y solo un apellido \n# Para terminar presione Enter\n\nIngrese su nombre completo: ")

      # verify that you have not entered any characters
      if len(name_partner) == 0: 
         val = 1
         break
      else:
         #verified that the information entered matches the required format
         if name_partner.count(" ") == 0 and name_partner.count(",") == 0:
            print("Formato invalido, intente nuevamente \n")
         else: break
         
   while val == 0 and True:
      dni_partner = input("Ingrese su dni: ")
      if dni_partner.isnumeric():
         if len(dni_partner) == 7 or len(dni_partner) == 8: break
         else: print("El dni debe poseer 7 u 8 digitos, intente nuevamente \n")
      else: print("Valor invalido, intente nuevamente \n")  
   
   print(f"Tu identicador es: {identify(name_partner, dni_partner)}")

# Exercise 4:
number_1 = int(input("Ingrese un número: "))
number_2 = int(input("Ingrese un otro número: "))
aux = 0

if number_2 > number_1:
   aux = number_1
   number_1 = number_2
   number_2 = aux

multiple(number_1, number_2)

# Exercise 5: 
days = int(input("Ingrese la cantidad de dias a consultar: "))

for i in range(days):
   temp_max = int(input(f"Dia {i + 1}, ingrese la temperatura maxima: "))
   temp_min = int(input(f"Dia {i + 1}, ingrese la temperatura minima: "))
   print(f"Temperatura media: {medium_temp(temp_max, temp_min)}° grados")
   
# Exercise 6: 
text = input("Ingrese texto: ")
print(space_text(text))

# Exercise 7: 
numbers = []

while True:
   number = int(input("Ingrese un número o 0 para salir: "))
   if number == 0: break
   else: numbers.append(number)

if len(numbers) != 0:
   # I get the maximum and minimum values of the list to destructure them into two variables
   max, min = min_max(numbers)
   print(f"El mayor número ingresado es: {max} \nEl menor número ingresado es: {min}")

# Exercise 8: 
radio = int(input("Ingrese el radio de una circuferencia: "))
perimeter, area = perimeter_area(radio)
print(f"Area: {area} \nPerimetro: {perimeter}")

# Exercise 9: 
intent = 3
while intent > 0:
   name_user = input("Ingrese su nombre de usuario: ")
   passw_user = input("Ingrese su contraseña: ")
   
   #if user and password match, return true, else false. then I ask you to try again
   if login(name_user, passw_user): 
      break
   else: 
      intent -= 1
      print(f"Datos incorrectos, tiene {intent} intentos")
else: 
   print("Lo siento, ya no posee más intentos para logearse")
   
# Exercise 14:
number = int(input("Ingrese un número: "))
print(f"{number} es un número primo" if prime_number(number) else f"{number} no es un número primo")
   
# Exercise 15:
count = 0
while True:
   n_fact = int(input("Ingrese número que desee saber su factorial o 0 para terminar: "))
   
   if n_fact == 0: break
   if n_fact <= -1:
      print("No se puede obtener el factorial de un número negativo")
   elif n_fact == 1: print(f"El factorial de {n_fact}: {n_fact}")
   else:
      count += 1
      factorial(n_fact)

print(f"Ha ingresado {count} número/s")

# Exercise 16:
number_int = int(input("Ingrese un número entero: "))
digit = int(input("Ingrese un digito: "))

if digit >= 10:
   print("No ha ingresado un digito valido")
else:
   print(f"Se encuentra {count_digit(number_int, digit)} veces el digito {digit}")
   
# Exercise 17:
while True:
   prime = int(input("Ingrese un número primo: "))

   if prime_number(prime):
      digit = int(input("Ingrese un digito: "))
      
      print(f"Aparece {count_digit(prime, digit)} veces")
      print(f"Suma de digitos: {sum_digit(prime)}")
      print(f"El factorial de {prime}: {factorial(prime)}")
   else: break