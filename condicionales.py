dias_semana = ["lunes","martes","miercoles","jueves","viernes"]

fecha = input("Ingrese fecha en formato: dia, DD/MM: ")

dia = fecha[0: fecha.find(",")].lower() # Extraer el dia de fecha
dia_valido = dia not in dias_semana # Validar el ingreso correcto de los dias de la semana
dia_mes = int(fecha[fecha.find(",") + 1: fecha.find("/")])
mes = int(fecha[fecha.find("/") + 1:])
validez = True

if dia_mes > 31: # Validar el correcto ingreso de datos (fecha)
  print("Se produjo un error: Dia del mes invalido")
  validez = False
elif mes > 12:
  print("Se produjo un error: Numero del mes invalido")
  validez = False
elif dia_valido == True:
  print("Se produjo un error: Dia invalido")
  validez = False

if validez == True and dia != dias_semana[3] and dia != dias_semana[4]: # Validar funcionalidad en relacion a los 3 primeros dias de la semana
  examenes = input("¿Se tomaron examenes?: ")
  
  if examenes.lower() == "si":
    aprobados = int(input("¿Cuantos alumnos aprobaron?: "))
    desaprobados = int(input("¿Cuantos desaprobaron?: "))
    promedio = aprobados * 100 / (aprobados + desaprobados)
    print(f"El porcentaje de aprobados es de: {round(promedio, 2)}%")

elif dia == dias_semana[3]: #Validar funcionalidad si es Jueves
  procentaje = int(input("Ingrese porcentaje de asistencia: "))
  if procentaje > 50:
    print("Asistio la mayoria")
  else: 
    print("No asistio la mayoria")

else: #Validar funcionalidad si es Viernes
  if (dia_mes == 1 and mes == 1) or (dia_mes == 1 and mes == 7): 
    print("¡¡¡Comienzo de nuevo ciclo!!!")
    cantidad_alumnos = int(input("Ingrese cantidad de alumnos: "))
    arancel = int(input("Ingrese arancel por alumno: "))
    print(f"Ingreso total: ${round(cantidad_alumnos * arancel, 2)}")
