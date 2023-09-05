# 1 - Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero_1 = 30

# 2 - crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = 4.5

# 3 - Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero_1 + numero2

# 4 - crear tres variables, (resta, multiplicación y división). Imprime estas variables.
resta = numero_1 - numero2
multiplicacion = numero_1 * numero2
division = numero_1 / numero2

print(resta)
print(multiplicacion)
print(division)

# 5 - Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Walter"

# 6 - Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.
precio = 30250.99

# 7 - crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo
descuento = .25

# 8 - Aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final". 
precio_final = precio - (descuento * precio)

# 9. Crea una variable llamada "cadena" y asignale un texto
cadena = "Esto es una frase"

# 10. crea una nueva variable llamada "longitud". Vas a almacenar la longitud en caracteres de la cadena
longitud = len(cadena)

"""
11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
mismo.
"""
precio = int(34500.99)

"""
12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
espacio entre medio. Puedes usar libremente la forma de concatenación que quieras
"""

nombre = "Roberto"
apellido = "Rodriguez"
nombre_completo = f"{nombre} {apellido}"


# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 22
edad += 5
edad -= 10

"""
14 - Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
centímetros. Multiplícala por 4 y luego divídela en 3
"""
altura = 1.88
altura *= 4
altura /= 3

# 15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas 
nombre_completo = "WALTER PLAZA"
print(nombre_completo.lower())

# 16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas excepto la primera letra.
print(nombre_completo.title())












