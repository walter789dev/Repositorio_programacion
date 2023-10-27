class Account:

   def __init__(self, headline = "", amount = 0):
      while True:
         if headline == "" or headline.isnumeric():
            headline = input("Titular invalido, ingrese un valor valido: ")
         else:
            self.__headline = headline
            break
         
      self.__amount = amount

   @property
   def headline(self):
      return self.__headline
   
   @property
   def amount(self):
      return self.__amount
    
   def get_info(self):
      print(f"Titular: {self.__headline or 'Desconocido'}, Cantidad: {self.__amount}")
      
   def set_headline(self, headline):
      if headline.isnumeric():
         print("Valor invalido")
      else: 
         if len(headline) != 0:
            print("Se ha actualizado correctamente")
            self.__headline = headline
         else: 
            print("No ha ingresado datos")
   
   def enter_amount(self, amount):
      extra = str(int(amount))
      if extra.isnumeric():
         if amount > 0: print("El monto ingresado es invalido")
         else: self.__amount += float(amount)
      else:
         print("El dato ingresado no es un valor númerico")
   
   def extract_amount(self, amount):
      extra = str(int(amount))
      if extra.isnumeric():
         if (self.__amount - amount) < 0: print("El monto solicitado excede el monto que posee")
         else: self.__amount -= float(amount)
      else:
         print("El dato ingresado no es un valor númerico")
   
   

   