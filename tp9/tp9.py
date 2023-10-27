from Person import Person
from Account import Account
from Diary import Diary
from Triangle import Triangle

# Exercise 1 y Exercise 2:
my_person = Person("Pedro", 23, 34567890)
my_headline = Account("Rodriguez", 1500)

my_person.set_age(35)
my_person.get_dni()
my_headline.enter_amount(2500.50)
my_headline.extract_amount(200.50)

my_person.get_info()
my_headline.get_info()

# Exercise 3:
side1 = int(input("Ingrese lado: "))
side2 = int(input("Ingrese lado: "))
side3 = int(input("Ingrese lado: "))

my_triangle = Triangle(side1, side2, side3)
print(f"El lado mayor es: {my_triangle.higher_side()}")
print(f"El triangulo es: {my_triangle.type_triangle()}")

# Exercise 4:
my_diary = Diary()
my_diary.open_diary()
