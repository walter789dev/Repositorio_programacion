# Exercise 9:
def memotest(matriz, couples):
   count = couples # stores the number of pairs of cards available
   i = 0 # counts the numbers entered
   total = 0 # stores the number of cards
   pre_pos = 0 # temporarily stores the first position entered
   
   pair = [[0, 0], [0, 0]]  # temporarily stores the values of the entered positions and the position
   pos = []  # stores the positions that matched their values in order to avoid requesting cards already found
   
   for list in matriz: # Graphically display the cards
      print(f"| {' [] ' * len(list)} |")
      total += len(list)
   
   while True:
      while i < 2:
         number = int(input("Ingrese el número de la carta que desee saber: "))
         if i == 1 and pre_pos == number: # I verify that the second position is not equal to the first position requested
            print("Ha ingresado el mismo número")
         else:
            if number not in pos: # If the number is not found in the variable that contains the positions of cards found, I check its value
               validate = find_cards(number, matriz, total)

               if validate == False: 
                  print("\nPosición invalida, intente nuevamente \n")
               else:
                  pre_pos = number
                  pair[i][0] = validate[0]
                  pair[i][1] = validate[1]
                  
                  print(f"El número es: {validate[0]}")
                  i += 1
            else:
               print("Ya ha encontrado la pareja \n")
      
      count = coincidences(pair, pos, count) # I check if the values of the positions match, if they match I subtract one from the couple counter
      i = 0 # reset both values to use them with the next pairs of cards
      pre_pos = 0
      
      if count == 0:  # If the counter is equal to zero it means you have found all the pairs
         print("¡¡ Felicitaciones !! Haz ganado el juego \n")
         break

def find_cards(number, matriz, total):
   fila = 0
   t_fila = len(matriz) - 1 # row size
   number = number - 1 # position
   
   if number >= total: return False
   else:
      # row size starting from 0, total cards, row size (jump)
      for i in range(t_fila, total + 1, t_fila + 1):
         # the possession must be less than the accumulated number of cards traveled and greater than the previous accumulated
         if number <= i and number > i - (t_fila + 1):
            pos = number % (t_fila + 1)
            return [matriz[fila][pos], number + 1]
         else:
            fila += 1

def coincidences(pair, pos, count):
   if pair[0][0] == pair[1][0]:
      count -= 1
      print(f"\nLos números coinciden, quedan {count} coincidencias \n")
      pos.append(pair[0][1])
      pos.append(pair[1][1])
   else:
      print(f"\nLos números no coinciden, quedan {count} coincidencias \n") 
   return count