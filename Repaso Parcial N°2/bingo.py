from bingo_funciones import start_bingo
from math import sqrt
"""
# Funcion get_uniques_numbers:
   Valida que los números ingresados sean únicos, en caso de que ingrese un número ya ingresado lo solicitara nuevamente, tambien lo hara si no ingresa un número o exceda en rango solicitado
"""
def get_uniques_numbers(arr, tam):
   i = tam # Tamaño de la lista de números únicos
   
   while i > 0:
      number = input("Ingrese un nùmero que se encuentre entre 1 y 75: ")
      if number.isnumeric(): # Si el valor ingresado es un número
         number = int(number)

         if number >= 1 and number <= 75: # Que no exceda el rango
            if number not in arr:
               arr.append(number)
               i -= 1 # Indica los números faltantes
               print(f"Faltan {i} nùmeros \n")
            else: 
               print(f"Ya ha ingresado el nùmero '{number}', intente nuevamente \n")
         else: 
            print("El nùmero ingresado excede el rango solicitado, intente nueavmente \n")
      else: 
         print("No ha ingresado un nùmero, intente nuevamente \n")

uniques_numbers = [] # Almacena los números únicos
long = 9 # Cantidad de números solicitados

print(f"¡¡¡ Bienvenido al Bingo !!! \nDebe ingresar {long} nùmeros ùnicos, estos se ubicaran en un carton de 5x5\n")

while True:
   get_uniques_numbers(uniques_numbers, long) # Rellena uniques_numbers
   start_bingo(uniques_numbers, int(sqrt(long))) # Inicia el Bingo
   option = input("¿Desea continuar? S. si, N. no").lower()
   if option != "s": break



