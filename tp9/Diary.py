class Diary:
   
   def __init__(self):
      self.__contacts = []
      
   def open_diary(self):
      while True:
         print("¿Que operación desea realizar?")
         option = int(input("1. Añadir contacto \n2. Lista de contactos \n3. Buscar contacto \n4. Editar contacto \n5. Cerrar agenda \nOpción: "))
         
         if option == 5: break
         else:
            if option == 1: self.add_contact()
            elif option == 2: self.read_contacts()
            elif option == 3: self.search_contact()
            elif option == 4: self.edit_contact()
      
   def add_contact(self):
      data = input("Ingrese su datos en el formato indicado: 'Nombre, Telefono, correo': ")
      if len(data.split(", ")) == 3: 
         name, tel, email = data.split(", ")
         
         if len(name) > 0 and tel.isnumeric() and email.find("@"):
            new_contact = [name.lower() , int(tel), email.lower()]
            self.__contacts.append(new_contact)
            print("Contacto Añadido")
         else:
            print("La información ingresada no coincide")
      else:
         print("Los datos no han sido ingresados en el formato solicitado")
   
   
   def read_contacts(self):
      if len(self.__contacts) == 0:
         print("No hay contactos disponibles")
      else:
         for contact in self.__contacts:
            print(f"{contact[0].capitalize()}: {contact[1]}, {contact[2]}")
      
            
   def search_contact(self):
      print("¿Con que dato desea buscar el contacto?")
      option = int(input("1. Nombre, 2. Número, 3. Correo: "))
      
      if option == 1:
         name = input("Ingrese nombre: ").lower()
         self.find_data(name)
         
      if option == 2:
         email = input("Ingrese correo: ").lower()
         
         if email.find("@"): self.find_data(email)
         else: print("Correo invalido")
         
      if option == 3:
         tel = input("Ingrese telefono: ")
         
         if len(tel) == 9 and tel.isnumeric(): self.find_data(int(tel))
         else: print("Número telefonico invalido")
         
      else: print("Opcion invalida")
      
   def edit_contact(self):
      print("¿Que contacto desea modificar?")
      contact = int(input("Ingrese número de contacto: "))
      arr = []
      
      for cont_list in self.__contacts:
         if contact in cont_list: 
            arr = cont_list
            break
      
      if len(arr) != 0: 
         self.__contacts.remove(arr)
         self.add_contact()
      else: print("El número ingresado no existe")
      
      
   def find_data(self, data):
      arr = []
      
      for contact in self.__contacts:
         if data in contact: 
            arr = contact
            break
   
      if len(arr) > 0: print(f"{arr[0]}: {arr[1]}, {arr[2]}")
      else: print("El valor ingresado no existe")