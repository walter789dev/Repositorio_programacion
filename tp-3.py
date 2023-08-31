# Exercise 1:

word = input("Introduzca una palabra: ")
for i in range(10):
   print(f"Tu palabra es: {word}")
   
#Exercise 2:

age = int(input("Introduzca su edad: "))
for i in range(1, age):
   print(f"Edad: {i}")

#Exercise 3:

numbers = []
number_post = int(input("Introduzca un número positivo: "))

for i in range(number_post):
   if i % 2 != 0:
      numbers.append(str(i))

t_numbers = ",".join(numbers)
print(t_numbers)

# Exercise 4:

numbers = []
number_post = int(input("Introduzca un número positivo: "))

i = number_post

while i >= 0:
   numbers.append(str(i))
   i -= 1

t_numbers = ",".join(numbers)
print(t_numbers)


#Exercise 5: 

amount_inv = int(input("Ingrese monto a invertir: "))
a_interest = int(input("Ingrese interes anual: "))
inv_age = int(input("Ingrese años a invertir: "))

total_inv = amount_inv
i = 1

while i <= inv_age:
   total_inv += a_interest * amount_inv / 100
   print(f"Año {i}: ${total_inv}")
   i += 1


#Exercise 6:

text = "*"
height = int(input("Introduzca un número: "))
i = 1

while i <= height:
   print(text.replace("*", "*" * i))
   i += 1

# Exercise 7: 

for i in range(1, 11):
   for j in range(1, 11):
      print(f"{i} x {j} = {i * j}")

# Exercise 8:

numbers = ["1"]
height = int(input("Introduzca un número: "))
i = 0

while i < height:
   print(" ".join(numbers))
   numb = int(numbers[0]) + 2
   numbers.insert(0, str(numb))
   i += 1

#Exercise 9:

password = "contraseña"
val = 1

while val != 0:
   v_password = input("Ingrese contraseña: ")
   if v_password == password:
      print("Contraseña correcta !!!")
      val = 0
   else:
      print("Intente nuevamente !!")
       
#Exercise 10:

v_number = int(input("Ingrese un numero: "))
cousin = 1

for i in range(2, v_number):
    if (v_number % i) == 0:
       cousin = 0

if cousin == 1:
   print("El número es primo")
else: 
   print("El número no es primo")

# Exercise 11:

word = input("Introduzca una palabra: ")
chars = list(word)
i = len(chars) - 1

while i >= 0: 
   print(f"Letra {i}: {chars[i]}")
   i -= 1

#Exercise 12:

phrase = input("Ingrese una frase: ")
c_char = input("Ingrese letra a buscar: ")
count = 0
chars = list(phrase)

for i in range(len(chars)):
   if phrase[i].lower() == c_char.lower():
      count += 1
else:
   print(f"La letra {c_char} se encuentra {count} vez/veces")

# Exercise 13:

val = 1
while val != 0:
   rep_text = input("Introduza una palabra: ")
   
   if rep_text.lower() != "salir":
      print(rep_text.replace(rep_text, f"{rep_text} " * 3))
   else:
      val = 0

# Exercise 14:

numb1 = int(input("Ingrese un número entero: "))
numb2 = int(input("Ingrese un otro número entero: "))
aux = 0

if numb2 > numb1:
   aux = numb1 
   numb1 = numb2
   numb2 = aux
   
while numb2 <= numb1:
   if (numb2 % 2) == 0:
      print(f"El numero {numb2} es par")
   else:
      print(f"El numero {numb2} es impar")
   numb2 += 1

# Exercise 15: 

dividers = []
numb = int(input("Ingrese un número entero: "))

for i in range(1, numb):
   if (numb % i) == 0:
      dividers.append(str(i))

print(f"Los divisores de {numb} son: {', '.join(dividers)}")

# Exercise 16: 

amount_numb = int(input("Ingrese cantidad de numeros a introducir: "))
count = 0

while amount_numb > 0:
   number = int(input("Ingrese un numero: "))
   if number < 0:
      count += 1
   amount_numb -= 1

print(f"La cantidad de números negativos: {count}")

# Exercise 17:

vowels = ["a", "e", "i", "o", "u"]
phrase = input("Ingrese una frase: ")
phrase = phrase.lower()
i = len(vowels) - 1

while i >= 0:
   val = phrase.find(vowels[i])
   if val == -1:
      vowels.pop(i)
   i -= 1
   
print(f"Las vocales encontradas son: {', '.join(vowels)}")


# Exercise 18:

counter = [0, 1]

for i in range(10):
   if i == 0 or i == 1:
      print(f"Numero {i + 1}: {i}")
   else: 
      aux = counter[0]
      counter[0] = counter[1]
      counter[1] = counter[1] + aux
      print(f"Numero {i + 1}: {counter[1]}")

# Exercise 19:

total = 0
amount_saving = int(input("Ingrese monto a conseguir: "))

while total <= amount_saving:
   save = int(input("Monto a ahorrar: "))
   if save < 0:
      print("Monto incorrecto, intente nuevamente")
   else:
      total += save
      
print(f"Ahorro conseguido: ${total}")

# Exercise 20:

add = 0
val = 1

while val != 0:
   numb = int(input("Introduzca un número: "))
   if numb != 0:
      add += numb
   else: 
      val = 0
else: 
   print(f"La sumatoria de valores es de: {add}")

# Exercise 21:

bigger = 0
val = 1

while val != 0:
   numb = int(input("Introduzca un número: "))
   if numb != 0:
      if numb > mayor:
         bigger = numb
   else: 
      val = 0
else: 
   print(f"El mayor valor es: {bigger}")

# Exercise 22:

add = 0
pair = 0
val = 1

while val != 0:
   number = int(input("Ingrese un número: "))
   if number != -1: 
      if number % 2 == 0:
         par += 1
      number = list(str(number))
      for i in range(len(number)):
         add += int(number[i])
         print(f"La suma de digitos es de: {add}")
         add = 0
   else:
      val = 0
else:
   print(f"Numeros pares: {pair}")

# Exercise 23 y 24:

total = 0
val = 1

while val != 0:
  amount = int(input("Ingrese monto de compra: "))
   if amount < 0:
      print("Monto invalido, intente nuevamente !!!")
   elif amount != 0:
      total += amount
   else: 
      val = 0
else: 
   if total > 1000:
      discount = total * .10
      print(f"Monto total: ${total - discount}")
   else:
      print(f"Monto total: ${total}")

# Exercise 25:

number = int(input("Ingrese un número: "))
total = 1

for i in range(1, number + 1):
   total *= i
else: 
   print(f"El factorial de {number} es de: {total}")
