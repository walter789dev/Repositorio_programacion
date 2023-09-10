# Ejercicio 1
print("1. Calcular el perímetro y área de un rectángulo dada su base y su altura.")
base = float(input("igresar base: "))
altura = float(input("ingresar altura"))

area = base * altura
perimetro = base*2+ altura*2
print("El area es de",area)
print("El perimetro es de",perimetro)

# Ejercicio 2
cateto1 = float(input("Ingesa cateto 1 : "))
print("cateto 1 es: "+str(cateto1))
cateto2 = float(input("Ingresa cateto 2: "))
print("cateto 2 es: "+str(cateto2))
hipo = ((cateto1**2)+(cateto2**2))**1/2
print("La hipotenusa es: ",hipo)

# Ejercicio 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

# Ejercicio 4
fahrenheit = int(input("Ingrese temperatura"))
celcius = (fahrenheit - 32)*5/9
print(celcius)

# Ejercicio 5

# Ejercicio 5a
cancion = input("¿Cuál es tu canción favorita?")
# Ejercicio 5b

precio = input("Precio: ")
precio = int(precio)
total = precio + (precio * 0.1)
# Ejercicio 5c

edad = int(input("Edad: "))
print("tu edad es", edad)
# Ejercicio 5d

edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)


# Ejercicio 6 

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
media = (num1 + num2 + num3)/3
print(media)

# Ejercicio 7

minutos=int(input("Ingrese minutos a transformar: "))
minutos_extra = 0

if (minutos / 60) % 2 != 0:
   horas = round(minutos / 60) - 1
   minutos_extra = minutos % 60
else: 
   horas = minutos / 60

print(f"{minutos} corresponde a: {horas}hr/s con {minutos_extra} minuto/s")

# Ejercicio 8
sueldo = 5000
ventas = 3
comision = sueldo * .1

total = sueldo + (ventas * comision)
print(total)

# Ejercicio 9
precio = float(input("Ingrese el precio del producto: "))
descuento = precio * 0.15
print(f"El total a pagar es {precio - descuento}")

 # Ejercicio 10
parcial1 = int(input("Ingrese nota de parcial 1 "))
parcial2 = int(input("Ingrese nota de parcial 2 "))
parcial3 = int(input("Ingrese nota de parcial 3 "))
promedio = (parcial1 + parcial2 + parcial1) / 3

examen_final = int(input("Ingrese nota de examen final "))
trabajo_final = int(input("Ingrese nota de trabajo final "))

calificacion_final = .55 * promedio + .30 * examen_final + .15 * trabajo_final
print(calificacion_final)

# Ejercicio 11
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
distancia = abs(num1 - num2)
print(f"La distancia entre {num1} y {num2} es {distancia}")

# Ejercicio 12
numero = int(input("Ingrese un numero: "))
raiz_cuadrada = numero ** .5
raiz_cubica = numero ** (1/3)

print(raiz_cuadrada, raiz_cubica)

# Ejercicio 13
num = input("Ingrese un numero de dos digitos")
num = int(num)
primero = int(num / 10)
segundo = num % 10
print(str(segundo) + str(primero))


# Ejercicio 14
numeroa = int(input("Numero A:"))
numerob = int(input("Numero B:"))
numeroa_ = numeroa
numeroa = numerob
numerob = numeroa_
print("Numero A: ", numeroa, " Numero B ", numerob)


# Ejercicio 15 #se pide a que hora salio

seconds_init = int(input("Ingrese el tiempo de viaje en segundos: "))
hours = seconds_init / 3600
minutes = 0
seconds = 0

if hours % 2 != 0:
   hours = round(hours) - 1 if hours % 2 >= 0.5 else round(hours)
   extra = seconds_init % 3600
   minutes = extra / 60
   
   if minutes % 2 != 0:
      minutes = round(minutes) - 1 if minutes % 2 >= 0.5 else round(minutes)
   
   seconds = extra % 60

print(f"El viaje demoro: {hours}hr/s con {minutes}min y {seconds}s")

# Ejercicio 16
nombre = input("Ingrese su nombre ")
apellido1 = input("Ingrese su primer apellido ")
apellido2 = input("Ingrese su segundo apellido ")

iniciales = f"Nombre:{nombre[0]}, Apellidos: {apellido1[0]}, {apellido2[0]}"
print(iniciales)

# Ejercicio 17
usuario = input("Ingrese su nombre")
print("Ahora estás en la matrix, " , usuario)

# Ejercicio 18
costo = int(input("Ingrese costo"))

servicio = .062
propina = .1

total = costo + (costo * servicio) + (costo * propina)
print(total)

# Ejercicio 19
dia = input("Ingrese el dia de su nacimiento")
mes = input("Ingrese el mes de su nacimiento")
anio = input("Ingrese el dia de su nacimiento")
print(dia,"/",mes,"/",anio)
 

# Ejercicio 20
age = input("Ingres fecha de nacimiento en formato DDMMAAAA: ")
print(f"Fecha: {age[0:2]}/{age[2:4]}/{age[4:8]}")

# Ejercicio 21
kilometro_litro = int(input("ingrese cantidad de kilometros por litro: "))
capacidad_litros = int(input("ingrese cantidad de litros disponibles: "))
kilometros = int(input("ingrese cantidad de kilometros: "))

cantidad_tanques = kilometros / (capacidad_litros * kilometro_litro)

if cantidad_tanques % 1 != 0:
  print((cantidad_tanques -cantidad_tanques % 1) + 1)
else:
  print(cantidad_tanques) 
