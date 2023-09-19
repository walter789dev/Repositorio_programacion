values = lambda add, number: add + number
  
def digits(digit, number):
   total_digit = digit
   v_digit = number
   
   if len(v_digit) != 0:
      for i in range(len(v_digit)):
         total_digit += int(v_digit[i])
   else:
      total_digit += int(number)
   return total_digit

