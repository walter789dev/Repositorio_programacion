class Triangle:
   
   def __init__(self, side_1, side_2, side_3):
      self.__s1 = side_1
      self.__s2 = side_2
      self.__s3 = side_3
      
   def higher_side(self):
      if self.__s1 >= self.__s2:
         if self.__s1 >= self.__s3: return self.__s1
         else: return self.__s3
      else:
         if self.__s2 >= self.__s3: return self.__s2
         else: return self.__s3
   
   def type_triangle(self):
      if self.__s1 == self.__s2 == self.__s3:
         return "Triangulo Equilatero"
      elif self.__s1 == self.__s2 != self.__s3 or self.__s1 != self.__s2 == self.__s3 or self.__s1 == self.__s3 != self.__s2:
         return "Triangulo Isoceles"
      else: 
         return "Triangulo Escaleno"
            
      