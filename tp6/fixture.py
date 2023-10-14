from itertools import combinations
from random import randint

def fixture(teams):
   l_teams = list(teams.keys()) # a list of football team names
   long = len(l_teams)
   pre_s = [] # temporarily stores soccer teams that already have a defined match
   count = 1 # counts meetings defined by date
   
   positions = [i for i in range(long)] # I create a list of numbers that contains from 0 to the size of the teams.
   list_combinations = [] # I store all possible combinations of two values

   for combo in combinations(positions, 2):
      if len(list(combo)) == 2: # I only store the combinations of two values
        list_combinations.append(list(combo))
   
   for i in range(long - 1): # counts soccer matches defined by date
      print(f"--------------- Fecha {i + 1} --------------")
      j = 0 # contains the current team to search for match
      pre_position = [] # stores the matches already defined by date
      
      while True:
         while count <= (long / 2): 
            if j not in pre_s:
               number_random = randint(0, long - 1)
               if number_random not in pre_s and number_random != j:
                  if [j, number_random] not in list_combinations:
                     # If the match already exists and there are no more soccer teams available, I reassign the crossings again.
                     count = 1
                     j = 0
                     pre_position.clear()
                     pre_s.clear()
                     break
                  else:  
                     pre_position.append([j, number_random])
                     pre_s += [j, number_random]
                     j += 1
                     count += 1
            else: j += 1
         # Once the soccer crosses have been obtained, I show the teams that will face each other by date.
         if len(pre_position) == (long / 2):
            for i in range(len(pre_position)):
               local = l_teams[pre_position[i][0]]
               visit = l_teams[pre_position[i][1]]
               
               print(f"\n----- Partido {i + 1}: {local} vs {visit} -------")
               result(teams, local, visit)
               list_combinations.remove(pre_position[i])
               
            count = 1
            pre_s.clear()
            break


def result(teams, local, visit):
   while True:
      pre_result = input("> Ingrese resultado en el siguiente formato\nEj: 1-0 \n> Resultado: ")
      result = pre_result.split("-")
      # valid that the results entered are valid data
      if len(result) == 2 and result[0].isnumeric() and result[1].isnumeric():
         rst_local = int(result[0])
         rst_visit = int(result[1])

         if rst_local >= 0 and rst_visit >= 0:
            # I validate that the result is valid
            if rst_local > rst_visit:
               # If the local team wins, I add the points obtained, the victory obtained, the goals for and against. To the rival I add the defeat, the goals for and against.
               teams[local]["victories"] += 1
               teams[local]["points"] += 3
               teams[local]["goals in favor"] += rst_local
               teams[local]["goals against"] += rst_visit
               
               teams[visit]["defeats"] += 1
               teams[visit]["goals in favor"] += rst_visit
               teams[visit]["goals against"] += rst_local

            elif rst_local == rst_visit:
               teams[local]["ties"] += 1
               teams[local]["points"] += 1

               teams[visit]["ties"] += 1
               teams[visit]["points"] += 1
            else:
               # If the visitor wins, I add the points obtained, the victory obtained, the goals for and against. To the rival I add the defeat, the goals for and against.
               teams[visit]["victories"] += 1
               teams[visit]["points"] += 3
               teams[visit]["goals in favor"] += rst_visit
               teams[visit]["goals against"] += rst_local
               
               teams[local]["defeats"] += 1
               teams[local]["goals in favor"] += rst_local
               teams[local]["goals against"] += rst_visit
            break
         else: print("Resultado invalido, intente nuevamente")
      else: print("Datos invalidos")
      

def team_champion(teams):
   champion = [0, ""]

   for i in list(teams.keys()):
      if teams[i]["points"] > champion[0]:
         champion[0] = teams[i]["points"]
         champion[1] = i
      
   print(f"El campeón del torneo es: {champion[1]} con {champion[0]} puntos, ¡¡¡ Felicitaciones !!!")