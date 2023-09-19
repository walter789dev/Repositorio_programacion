# Exercise 1:
most = lambda a, b: a if a > b else b
least = lambda a, b: a if a < b else b

x = int(input("Un número: "))  
y = int(input("Otro número: "))  

print(most(x - 3, least(x + 2, y - 5)))

# Exercise 2:
import sum 
sum_dig = 0 
sum_val = 0

while True:
   number = input("Ingrese un número mayor a 0 o 0 para salir: ")

   if number.isnumeric():
      if int(number) != 0:
         sum_val = sum.values(sum_val, int(number))
         sum_dig = sum.digits(sum_dig, number)
      else:
         if sum_val == 0:
            break
         else:
            print(f"La suma de los valores ingresados es: {sum_val}")
            print(f"La suma de los digitos ingresados es: {sum_dig}")
            break
   else:
      print("Valor invalido, intente nuevamente")

# Exercise 'Ahorcado'
import hangman

intents = 4
words = [
   "bug", "codigo", "programacion",
   "variable", "funcion", "bucle", "diagrama",
   "condicional", "error", "arhivo", "interprete"
]

hangman.play(words, intents, theme="Programacion")

