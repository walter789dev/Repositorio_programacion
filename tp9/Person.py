class Person:

    def __init__(self, name = "", age = "", dni = 0):
        self.name = name
        self.age = age
        self.dni = dni

    def get_name(self):
        if len(self.name) == 0: print("No ha ingresado su nombre")
        else: print(f"Tu nombre es: {self.age}")

    def get_age(self):
        if self.age == 0: print("No ha ingresado su edad")
        else: print(f"Tu edad es: {self.age}")

    def get_dni(self):
        if self.dni == 0: print("No ha ingresado su dni")
        elif len(str(self.dni)) < 8 or len(str(self.age)) > 8: print("Dni invalido")
        else: print(f"Tu dni es: {self.age}")

    def get_info(self):
        print(f"Nombre: {self.name or 'Desconocido'}, Edad: {self.age or 'Desconocido'}, Dni: {self.dni or 'Desconocido'}")
    
    def set_name(self, n):
        n = str(n)
        if len(n) > 0 and not n.isnumeric():
            self.name = n
            print(f"Se ha modificado el nombre a '{self.name}'")
        else: print("El nombre ingresado no es valido")

    def set_age(self, age):
        age = str(age)
        if len(age) > 0 and age.isnumeric():
            self.age = int(age)
            print(f"Se ha modificado la edad a '{self.age}'")
        else: print("La edad ingresada no es valida")

    def set_dni(self, dni):
        dni = str(dni)
        if len(dni) > 0 and dni.isnumeric():
            self.dni = int(dni)
            print(f"Se ha modificado la edad a '{self.dni}'")
        else: print("El dni ingresado no es valido")
    
    def isOlder(self):
        if self.age >= 18 and self.age != 0: return True
        else: return False

    

    