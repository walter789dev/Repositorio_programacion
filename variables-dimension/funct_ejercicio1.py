#I request information about the passenger. 
# Valid that it be entered in a valid format. 
# In addition to sending your destination information to the function validate_travel
def set_info_passenger(cities):
   while True:
      print("\nIngrese la siguiente informaciòn en el formato indicado")
      info_passenger = input("Ej: Nombre, Dni (8 digitos), Cuidad, Pais \n: ")
      new_passenger = info_passenger.split(", ")

      if len(new_passenger) == 4 and len(new_passenger[1]) == 8:
         city = new_passenger.pop(3)
         validate_travel(cities, (new_passenger[2], city))
         break
      else: 
         print("Formato incorrecto")
   return tuple(new_passenger)

#I request that you enter city and country to store it in 'cities'. 
# I also send the information to the function validate_travel
def set_cities(cities):
   while True:
      print("\nIngrese una cuidad en el formato indicado")
      city = input("Ej: Cuidad, Pais \n: ")
      new_travel = city.split(", ")
   
      if len(new_travel) == 2:
         if validate_travel(cities, tuple(new_travel)): 
            print("La cuidad ingresada ya se encuentra en el sistema")
         break
      else:
         print("Formato incorrecto")
      
# I verify that the destination information is not found in the list of tuples (cities)
def validate_travel(cities, travel):
   if travel not in cities:
      cities.append(travel)
   else:
      return True
   
# I verify that the ID entered has 8 digits
# I verify that there is a passenger registered with the ID entered and obtain their destination city
def get_passenger(passengers):
   while True:
      dni = input("Ingrese Dni del pasajero: ")
   
      if len(dni) == 8 and dni.isnumeric():
         for passenger in passengers:
            if passenger[1] == dni:
               print(f"Su destino (cuidad) es: {passenger[2]}")
               break
         else:
            print("No se ha encontrado un pasajero con el dni ingresado")
         break
      else: print("Formato de dni invalido")
      

# I request the ID, I search the passengers if I find a user that matches the ID and I get the city. 
# With the city, I search in cities and verify the one that matches and extract its country
def get_country(passengers, cities):
   while True:
      dni = input("Ingrese Dni del pasajero: ")
      v_city = ""
   
      if len(dni) == 8 and dni.isnumeric():
         for passenger in passengers:
            if passenger[1] == dni:
               city = passenger[-1]
               break
         
         if len(v_city) != 0:
            for city in cities:
               if city[0] == v_city:
                  print(f"Su destino (cuidad) es: {city[1]}")
                  break
         else:
            print("No se ha encontrado un pasajero con el dni ingresado")
         break
      else: print("Formato de dni invalido")

# I check passengers if I find the chosen city or country and count the matches
def count_passengers(passengers, option = "ciudad"):
   count = 0
   destiny = input(f"Ingrese {option}: ")
   for passenger in passengers:
      if option == "cuidad":
         if passenger[3] == destiny:
            count += 1
      if option == "cuidad":
         if passenger[-1] == destiny:
            count += 1
   else:
      print(f"Hay {count} pasajero/s para '{option.capitalize()}'")