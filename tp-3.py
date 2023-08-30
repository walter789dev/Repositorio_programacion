# Ejercitación 1:

word = input("Introduzca una palabra: ")
for i in range(10):
   print(f"Tu palabra es: {word}")
   
#Ejercicio 2:

age = int(input("Introduzca su edad: "))
for i in range(1, age):
   print(f"Edad: {i}")

#Ejercicio 3:

numbers = []
number_post = int(input("Introduzca un número positivo: "))

for i in range(number_post):
   if i % 2 != 0:
      numbers.append(str(i))

t_numbers = ",".join(numbers)
print(t_numbers)

# Ejercicio 4:

numbers = []
number_post = int(input("Introduzca un número positivo: "))

i = number_post

while i >= 0:
   numbers.append(str(i))
   i -= 1

t_numbers = ",".join(numbers)
print(t_numbers)


#Ejercicio 5: 

cant_inv = int(input("Ingrese monto a invertir: "))
a_interes = int(input("Ingrese interes anual: "))
inv_age = int(input("Ingrese años a invertir: "))

total_inv = cant_inv
i = 1

while i <= inv_age:
   total_inv += a_interes * cant_inv / 100
   print(f"Año {i}: ${total_inv}")
   i += 1


#Ejercicio 6:

text = "*"
altura = int(input("Introduzca un número: "))
i = 1

while i <= altura:
   print(text.replace("*", "*" * i))
   i += 1

# Ejercicio 7: 

for i in range(1, 11):
   for j in range(1, 11):
      print(f"{i} x {j} = {i * j}")

# Ejercicio 8:

numeros = ["1"]
altura = int(input("Introduzca un número: "))
i = 0

while i < altura:
   print(" ".join(numeros))
   numb = int(numeros[0]) + 2
   numeros.insert(0, str(numb))
   i += 1

#Ejercicio 9:

password = "contraseña"
val = 1

while val != 0:
   v_password = input("Ingrese contraseña: ")
   if v_password == password:
      print("Contraseña correcta !!!")
      val = 0
   else:
      print("Intente nuevamente !!")
       
#Ejercicio 10:

v_number = int(input("Ingrese un numero: "))
primo = 1

for i in range(2, v_number):
    if (v_number % i) == 0:
       primo = 0

if primo == 1:
   print("El número es primo")
else: 
   print("El número no es primo")

# Ejercicio 11:

word = input("Introduzca una palabra: ")
chars = list(word)
i = len(chars) - 1

while i >= 0: 
   print(f"Letra {i}: {chars[i]}")
   i -= 1

#Ejercicio 12:

frase = input("Ingrese una frase: ")
c_letra = input("Ingrese letra a buscar: ")
count = 0
chars = list(frase)

for i in range(len(chars)):
   if frase[i].lower() == c_letra.lower():
      count += 1
else:
   print(f"La letra {c_letra} se encuentra {count} vez/veces")

# Ejercicio 13:

val = 1
while val != 0:
   rep_text = input("Introduza una palabra: ")
   
   if rep_text.lower() != "salir":
      print(rep_text.replace(rep_text, f"{rep_text} " * 3))
   else:
      val = 0

# Ejercico 14:

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

# Ejercicio 15: 

divisores = []
numb = int(input("Ingrese un número entero: "))

for i in range(1, numb):
   if (numb % i) == 0:
      divisores.append(str(i))

print(f"Los divisores de {numb} son: {', '.join(divisores)}")

# Ejercicio 16: 

cantidad_numb = int(input("Ingrese cantidad de numeros a introducir: "))
count = 0

while cantidad_numb > 0:
   number = int(input("Ingrese un numero: "))
   if number < 0:
      count += 1
   cantidad_numb -= 1

print(f"La cantidad de números negativos: {count}")

# Ejercicio 17:

vocales = ["a", "e", "i", "o", "u"]
frase = input("Ingrese una frase: ")
frase = frase.lower()
i = len(vocales) - 1

while i >= 0:
   val = frase.find(vocales[i])
   if val == -1:
      vocales.pop(i)
   i -= 1
   
print(f"Las vocales encontradas son: {', '.join(vocales)}")


# Ejercicio 18:

contador = [0, 1]

for i in range(10):
   if i == 0 or i == 1:
      print(f"Numero {i + 1}: {i}")
   else: 
      aux = contador[0]
      contador[0] = contador[1]
      contador[1] = contador[1] + aux
      print(f"Numero {i + 1}: {contador[1]}")

# Ejercicio 19:

total = 0
cantidad_ahorro = int(input("Ingrese monto a conseguir: "))

while total <= cantidad_ahorro:
   ahorro = int(input("Monto a ahorrar: "))
   if ahorro < 0:
      print("Monto incorrecto, intente nuevamente")
   else:
      total += ahorro
      
print(f"Ahorro conseguido: ${total}")

# Ejercicio 20:

suma = 0
val = 1

while val != 0:
   numb = int(input("Introduzca un número: "))
   if numb != 0:
      suma += numb
   else: 
      val = 0
else: 
   print(f"La sumatoria de valores es de: {suma}")

# Ejercicio 21:

mayor = 0
val = 1

while val != 0:
   numb = int(input("Introduzca un número: "))
   if numb != 0:
      if numb > mayor:
         mayor = numb
   else: 
      val = 0
else: 
   print(f"El mayor valor es: {mayor}")

# Ejercicio 22:

suma = 0
par = 0
val = 1

while val != 0:
   number = int(input("Ingrese un número: "))
   if number != -1: 
      if number % 2 == 0:
         par += 1
      number = list(str(number))
      for i in range(len(number)):
         suma += int(number[i])
         print(f"La suma de digitos es de: {suma}")
         suma = 0
   else:
      val = 0
else:
   print(f"Numeros pares: {par}")

# Ejercicio 23 y 24:

total = 0
val = 1

while val != 0:
   monto = int(input("Ingrese monto de compra: "))
   if monto < 0:
      print("Monto invalido, intente nuevamente !!!")
   elif monto != 0:
      total += monto
   else: 
      val = 0
else: 
   if total > 1000:
      descuento = total * .10
      print(f"Monto total: ${total - descuento}")
   else:
      print(f"Monto total: ${total}")

# Ejercicio 25:

numero = int(input("Ingrese un número: "))
total = 1

for i in range(1, numero + 1):
   total *= i
else: 
   print(f"El factorial de {numero} es de: {total}")
