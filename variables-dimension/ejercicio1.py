from funct_ejercicio1 import *

cities = []
passengers = []

while True:
   print("\n¿Que operaciòn desea realizar?")
   print("1. Agregar pasajero\n2. Agregar cuidad \n3. ¿A que cuidad viaja?")
   print("4. ¿Cuantos pasajeros viajan a la ciudad 'x'?\n5. ¿A que pais viaja?")
   print("6. ¿Cuantos pasajeros viajan al pais 'x'? \n7. Salir")
   option = int(input(": "))
   
   if option == 1: 
      passengers.append(set_info_passenger(cities))
   elif option == 2:
      set_cities(cities)
   elif option == 3: 
      get_passenger(passengers)
   elif option == 4: 
      count_passengers(passengers)
   elif option == 5: 
      get_country(passengers, cities)
   elif option == 6: 
      count_passengers(passengers, option="pais")
   elif option == 7: 
      break
   else:
        print("Opcion invalida, intente nuevamente \n")