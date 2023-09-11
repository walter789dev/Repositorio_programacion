#Ejercicio 1:

letras = "abcdefghijklmnñopqrstuvwxyz"
encriptacion = int(input("Ingrese un numero para encriptacion: "))
mensaje_encrip = ""

for i in range(5):
  mensaje = input("Ingrese su mensaje: ")
  mensaje_lower = mensaje.lower()

  for j in mensaje_lower:
    letra = letras.find(j)

    if letra <= -1: 
       mensaje_encrip += j
    else: 
      search = letra + encriptacion
      if search >= 27:
         resto = search % 27
         mensaje_encrip += letras[resto]
      else: 
         mensaje_encrip += letras[letra + encriptacion]

  print(f"Tu mensaje es: {mensaje_encrip.upper()}")
  mensaje_encrip = ""

#Ejercicio 2:

val_1 = 1
d_par = 0
d_impar = 0

while val_1 != 0:
  number = int(input("Ingrese un número positivo: "))
  if number == 0:
    val_1 = 0
  else:
      t_number = list(str(number))
      i = 0
      d2_par = 0
      d2_impar = 0
      while i < (len(t_number)):
         if (int(t_number[i]) % 2) == 0:
            d2_par += 1
            d_par += 1
            i += 1
         else:
            d2_impar += 1
            d_impar += 1
            i += 1
      print(f"El numero posee {d2_par} digitos par y {d2_impar} digitos impar")
      
print(f"Digitos Pares: {d_par}")
print(f"Digitos Impares: {d_impar}")
        
   


