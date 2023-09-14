# -----------Ejercicio 1

phase = input("Ingrese una palabra o frase: ")

if len(phase) == 0: print("No se han ingresado caracteres")
elif len(phase) <= 4: print(f"Tu frase es: {phase}!")
else: print(f"Tu frase es: {phase}?")

# -------------Ejercicio 2
import random

words = ["gorila", "pelicano", "perro", 
   "ornitorrinco", "gato", "mono", 
   "morza", "iguana", "foca", "raton"]

print("¡¡¡¡ Adivina la palabra !!! Tematica: Animales")
print("\nCuidado: Tienes 4 intentos para adivinar la palabra")

number_random = random.randrange(10)
text = ""
word_select = words[number_random]
position = 0
tries = 4

print(f"\nPista: la palabra posee {len(word_select)} letras\n")

while tries >= 1:
   letter = input("Ingrese una letra: ")

   if letter == word_select[position]:
      text += letter
      print(f"\n¡¡Letra acertada!! Palabra: {text}\n")

      if len(text) == len(word_select):
         print(f"¡¡Ganaste!! La palabra era: {word_select}")
         break

   elif letter != word_select[position] and len(text) == 0:
      tries -= 1
      print(f"\n¡¡Letra Incorrecta!! Tienes {tries} intentos \n")
   else:
      tries -= 1
      print(f"\n¡¡Letra Incorrecta!!\nTienes {tries} intentos")
      print(f"\nPalabra: {text}\n")

if tries == 0: print(f"¡¡Perdiste!! La palabra era: {word_select}")

# ------------------- Ejercicio 3

phase = input("Ingrese una oraciòn: ")

if len(phase) == 0: print("No se han ingresado caracteres")
else: 
   count_phase = phase.split(" ")
   print(f"Se han ingresado: {len(count_phase)} palabra/s")

# ----------------------- Ejercicio 4

salary = int(input("Ingrese salario mensual: "))
month_assistance = input("¿Asistio todo el mes? \nS. si \nN. no \n: ").lower()
sunday = int(input("Ingrese horas trabajadas en dias domingos: "))

if month_assistance == "s" and (sunday >= 3 and sunday <= 5):
   print(f"Le corresponde un plus del 3% \nTotal: {salary + (salary * .03)}")
elif month_assistance == "s" and (sunday >= 6 and sunday <= 10):
   print(f"Le corresponde un plus del 10% \nTotal: {salary + (salary * .10)}")
elif month_assistance == "n" and (sunday >= 3 and sunday <= 10):
   print(f"Le corresponde un plus del 2% \nTotal: {salary + (salary * .02)}")
else:
   print(f"No le corresponde ningun plus \nTotal: {salary}")

# ----------------------- Ejercicio 5

number_1 = int(input("Ingrese un número: "))
number_2 = int(input("Ingrese otro número: "))

if number_1 == number_2: print(f"{number_1} x {number_2} = {number_1 * number_2}")
elif number_1 > number_2: print(f"{number_1} - {number_2} = {number_1 - number_2}")
else: print(f"{number_1} + {number_2} = {number_1 + number_2}")

# ----------------------- Ejercicio 6

print("Jubilacion 2010")
age = int(input("Ingrese su edad: "))
age_work = int(input("Ingrese años de antiguedad laboral: "))

if age >= 60 and age_work < 25: 
   print("Le corresponde una jubilacion por edad")
elif age < 60 and age_work >= 25: 
   print("Le corresponde una jubilacion por antiguedad joven")
elif age >= 60 and age_work >= 25: 
   print("Le corresponde una jubilacion por antiguedad adulta")
elif age < 40:
   print("No le corresponde jubilacion")

# ----------------------- Ejercicio 7

years = int(input("Seleccione su antiguedad en la empresa\n1. Menor a 1 año \n2. Mayor a 1 año pero menor a 2 años\n3. Mayor a 2 años pero menor a 5 años \n4. Mayor a 5 años pero menor a 10 años \n5. Mayor a 10 años \n: "))
salary = int(input("Ingrese su salario mensual: "))

while True:
   if years == 1:
      print(f"Le corresponde: ${salary + (salary * .05)}")
   elif years == 2:
      print(f"Le corresponde: ${salary + (salary * .07)}")
   elif years == 3:
      print(f"Le corresponde: ${salary + (salary * .10)}")
   elif years == 4:
      print(f"Le corresponde: ${salary + (salary * .15)}")
   elif years == 5:
      print(f"Le corresponde: ${salary + (salary * .20)}")
   if years > 5: 
      print("Opcion invalida, por favor intente nuevamente")
   else: 
      break