from random import randint

# 1:
def experiment(option, min, total):
   if option == 1 and min == 3:
      number = randint(1, 3)
      experiment(number, 0, total)
   elif option == 2 and min == 5:
      number = randint(1, 3)
      experiment(number, 0, total)
   elif option == 3 and min == 7:
      print(f"El ratòn ha salido, tardo {total} minutos")
   else: 
      min += 1
      total += 1
      experiment(option, min, total)

number_azar = randint(1, 3)
experiment(number_azar, 0, 0)

# 2: Invierte el orden de los digitos
def f(n):
   s = str(n)
   if len(s) <= 1:
      return s
   return s[-1] + f(int(s[:-1]))