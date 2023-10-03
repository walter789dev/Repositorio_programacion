import pytest
from funcionesTp5 import *

#Testing Exercise 1:
@pytest.mark.parametrize("dni, res",[
   (3425678, True),
   (123456, False),
   (89234567, True)
])

def test_dni(dni, res):
   assert verify_dni(dni) == res

#Testing Exercise 2:
@pytest.mark.parametrize("word, res",[
   ("Hello world", 5),
   ("Pedro", 5),
   ("Que onda cracks", 6)
])

def test_long_last_word(word, res):
   assert long_last_word(word) == res
    
#Testing Exercise 3:
@pytest.mark.parametrize("name, dni, res",[
   ("Pedro Rodriguez", "2345678", "Pedro9234"),
   ("Ismael, Pablo, Arza", "12345678", "Ismael4123"),
   ("Ivan Alfaro", "1234567", "Ivan6123")
])

def test_identify(name, dni, res):
   assert identify(name, dni) == res

#Testing Exercise 4:
@pytest.mark.parametrize("numb1, numb2, res",[
   (10, 5, "10 es multiplo de 5"),
   (23, 2, "23 no es multiplo de 2"),
   (10, 10, "10 es multiplo de 10")
])

def test_multiple(numb1, numb2, res):
   assert multiple(numb1, numb2) == res
    
#Testing Exercise 5:
@pytest.mark.parametrize("t_max, t_min, res",[
   (25, 15, 20),
   (35, 10, 22.5),
   (40, 9, 24.5)
])

def test_medium_temp(t_max, t_min, res):
   assert medium_temp(t_max, t_min) == res
    
#Testing Exercise 6:
@pytest.mark.parametrize("text, res",[
   ("Hola, tu", "H o l a ,  t u "),
   ("Pedro Pica", "P e d r o  P i c a "),
   ("Messi", "M e s s i ")
])

def test_space_text(text, res):
   assert space_text(text) == res
    
#Testing Exercise 7:
@pytest.mark.parametrize("numbers, res",[
   ([12, 23, 45, 100, 500, 10], [500, 10]),
   ([1, 5, 6, 9], [9, 1]),
   ([10, 20, 40, 60, 61], [61, 10])
])

def test_min_max(numbers, res):
   assert min_max(numbers) == res
    
#Testing Exercise 8:
@pytest.mark.parametrize("radio, res",[
   (15, [94.25, 706.86]),
   (10, [62.83, 314.16]),
   (25, [157.08,1963.50])
])

def test_perimeter_area(radio, res):
   assert perimeter_area(radio) == res
    
#Testing Exercise 9:
@pytest.mark.parametrize("name, passw, res",[
   ("usuario1", "asdasd", True),
   ("usuario1123", "dfsfsdfs", False),
   ("usuario123", "1123234235", False)
])

def test_login(name, passw, res):
   assert login(name, passw) == res
    
#Testing Exercise 10:
@pytest.mark.parametrize("products, res",[
   ({
     "arroz": [1200, 5],
     "papa": [1000, 13],
     "camote": [1500, 15]
   }, 3285),
   ({
     "arroz": [150, 15],
     "papa": [120, 10],
     "camote": [250, 20]
   }, 435.5),
   ({
     "arroz": [1000, 5],
     "papa": [1100, 10],
     "camote": [1900, 20]
   }, 3460)
])

def test_discount(products, res):
   assert discount(products) == res

#Testing Exercise 11:
@pytest.mark.parametrize("list, funct, res",[
   ([2, 4, 6, 8, 10], dobule_list, [4, 8, 12, 16, 20]),
   ([10, 20, 30, 40, 50], multiple_next, [200, 600, 1200, 2000, 500]),
   ([2, 3, 4, 5, 6], multiple_previous, [12, 6, 12, 20, 30])
])

def test_info_words(list, funct, res):
    assert info_words(list, funct) == res
    
#Testing Exercise 12:
@pytest.mark.parametrize("phase, res",[
   ("Esto también pasará", {
      "Esto": 4,
      "también": 7,
      "pasará": 6
   }),
   ("La vida es una colección", {
      "La": 2,
      "vida": 4,
      "es": 2,
      "una": 3,
      "colección": 9
   }),
   ("Un día sin reír", {
      "Un": 2,
      "día": 3,
      "sin": 3,
      "reír": 4
   })
])

def test_info_words(phase, res):
    assert info_words(phase) == res
    
#Testing Exercise 13:
@pytest.mark.parametrize("a, b, res",[
   (2, 3, 3.61),
   (5, 6, 7.81),
   (4, 5, 6.40)
])

def test_module_vector(a, b, res):
   assert module_vector(a, b) == res

#Testing Exercise 14:
@pytest.mark.parametrize("number, res",[
   (6, False),
   (37, True),
   (89, True)
])

def test_prime_number(number, res):
   assert prime_number(number) == res
   
#Testing Exercise 15:
@pytest.mark.parametrize("numb, res",[
   (4, 24),
   (5, 120),
   (6, 720)
])

def test_factorial(numb, res):
   assert factorial(numb) == res
   
#Testing Exercise 16:
@pytest.mark.parametrize("numb, digit, res",[
   (42424, 4, 3),
   (5112323, 1, 2),
   (6000, 5, 0)
])

def test_count_digit(numb, digit, res):
   assert count_digit(numb, digit) == res
   
#Testing Exercise 16:
@pytest.mark.parametrize("numb, res",[
   (24, 6),
   (1234, 10),
   (5555, 20)
])

def test_sum_digit(numb, res):
   assert sum_digit(numb) == res