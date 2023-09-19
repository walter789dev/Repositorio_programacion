import random

def play(words, intents, theme="Estandar"):
   print(f"Juego del ahorcado, Tematica: '{theme}' \nTienes {intents} intentos para adivinar la palabra")
   # generated a random number from the random library 
   number_random = random.randrange(len(words))
   word = words[number_random]
   
   char = []
   text = "_" * len(word)
   
   while intents >= 1:
      letter = input("Ingrese una letra: ").lower()
      # valid for the character to be an alphabetic character
      if letter.isalpha():
         if (letter in word) and (letter in char): print("Ya has adivinado la letra ingresada")
         
         elif letter in word:
            print("Adivinaste una letra correctamente")
            char.append(letter)
            text = check_pos(text, word, letter)
            
            if "_" not in text: 
               # If you don't find the character it's because you guessed the word
               print(f"Has adivinado la palabra '{word}', ¡¡ Felicitaciones !!!")
               break
         else:
            intents -= 1
            print(f"Letra incorrecta, te quedan {intents} intentos")
            
         print(text + "\n")
      else: print("Caracter invalido, por favor ingrese caracteres alfabeticos")
   else: print(f"Te has quedado sin intentos, la palabra ha adivinar era: {word}")
  
  
def check_pos(text, word, letter):
   text_r = list(text) 
   # I convert to list to check character by character to replace matches
   for i in range(len(word)):
      if word[i] == letter:
         text_r[i] = letter
   return "".join(text_r)