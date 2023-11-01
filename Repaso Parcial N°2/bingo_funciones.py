from random import randint
from re import search

# -------------------  Entrada del Bingo -------------------------
def start_bingo(arr, rows): # Rows indica la cantidad de filas del carton
   n_coincidence = [] # Mantiene los números que se han mostrado al usuario para evitar numeros repetiods
   matriz = bingo_fill_matriz(arr, rows) # Construye la matriz de N x N
   count = 0
   print("------ Salida de números ---------")
   
   while True:
      rand_number = randint(1, 75)
      #Verifico que el número se encuentre en la matriz y que no se halla mostrado al usuario
      if rand_number in arr and rand_number not in n_coincidence:
         print(f"Ha salido el nùmero {rand_number}")
         n_coincidence.append(rand_number) # Lo guardo para evitar mostrarle al usuario un número que ya salio anteriormente
         count = assign_position(matriz, rand_number, count)
         
         print("¡¡¡ Se encuentra en tu carton !!! \n\nEstado del Carton: ")
         for row in range(rows): print(matriz[row]) # Muestro las filas de la matriz
         
         if count >= rows: # Si la cantidad de coincidencias es igual al tamaño de las filas, verfico si hay bingo o no
            msj, validate = check_bingo(matriz, rows) #Verifica si hay una linea vertical, horizontal o diagonal
            if validate: 
               print(f"\n¡¡¡ Bingo !!! {msj}")
               break
         
         input("Presione Enter para continuar: ") # Pauso para que el usuario vea los números que salen
           
      elif rand_number not in arr and rand_number not in n_coincidence:
         print(f"Ha salido el nùmero {rand_number}")
         print("El nùmero no se encuentra en tu carton \n")
         n_coincidence.append(rand_number)
         
         input("Presione Enter para continuar: ")

# ---------------------- Funciones Bingo -----------------------
"""
# Funcion bingo_fill_matriz: 
    Ordena los números ingresados por el usuario en una matriz cuadrada
"""
def bingo_fill_matriz(arr, tam):
   new_arr = []
   i = 0
   for x in range(tam):
      row = []
      for y in range(tam): 
         row.append(arr[i])
         i += 1
      new_arr.append(row)
   return new_arr
"""
# Funcion assign_position:
   Busca la coincidencia y la cambia por una X
"""
def assign_position(arr, number, c):
   for x in range(len(arr[0])):
      for y in range(len(arr[0])):
         if arr[x][y] == number:
            arr[x][y] = "X"
            return c + 1 
"""
# Funcion check_bingo:
   Verifica si hay bingo de forma vertical, horizontal o diagonal
"""
def check_bingo(arr, row):
   v = vertical(arr, row)
   if v: return ["Linea Vertical", v]
   
   h = horizontal(arr, row)
   if h: return ["Linea Horizontal", h]
   
   d = diagonal(arr, row)
   if d: return ["Diagonal", d]
   else: return ["", False]
   
# Chequea verticalmente por columna si hay bingo
def vertical(arr, row):
   count = 0
   y = 0
   
   for i in range(row):
      for j in range(row): 
         y = i
         if arr[j][i] == "X": count += 1
         else: break
      if count == row: return True
      else: count = 0
   else: return False 
      
# Chequea horizontalmente por fila si hay bingo
def horizontal(arr, row):
   count = 0
   x = 0
   
   for i in range(row):
      for j in range(row): 
         x = i
         if arr[i][j] == "X": count += 1
         else: break
      if count == row: return True
      else: count = 0
   else: return False 
   
# Verifica en las diagonales de la matriz si hay bingo
def diagonal(arr, row):
   items = [str(arr[i][i]) for i in range(row)]
   items = " ".join(items)
   
   if not search(r'\d', items): return True
   j = 0
   
   for i in range(row - 1, -1, -1):
      if arr[j][i] == "X": j += 1
      else: break
      
   if j == row: return True
   else: return False
   
      
   

