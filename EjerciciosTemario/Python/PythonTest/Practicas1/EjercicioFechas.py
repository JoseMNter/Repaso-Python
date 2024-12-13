from datetime import datetime
from datetime import timedelta
""" Para realizar estos ejercicios parte de dos listas, una con fechas representadas como cadenas en formato YYYY-MM-DD y otra con horas con cadenas en formato HH:MM:SS """

fechas = ['2024-09-09', '2023-08-15', '2022-07-01']
horas = ['14:30:00', '09:15:00', '23:59:59']

fechas_convertidas=[]
horas_convertidas=[]
fecha_y_hora_Combinadas=[]

""" Convierte cada cadena de la lista fechas a un objeto date. """
for fecha in fechas:
    fechas_convertida=datetime.strptime(fecha, "%Y-%m-%d").date()
    fechas_convertidas.append(fechas_convertida)

for hora in horas:
    hora_convertida=datetime.strptime(hora, "%H:%M:%S").time()
    horas_convertidas.append(hora_convertida)

for i in range(len(fechas_convertidas)):
    fecha_y_hora_Combinadas.append(datetime.combine(fechas_convertidas[i],horas_convertidas[i]))
print(fecha_y_hora_Combinadas)

""" Convierte cada cadena de la lista horas a un objeto time """
""" Combina cada elemento de los objetos date y los objetos time de los dos ejercicios anteriores para crear una lista de objetos datetime. """
""" Calcula los días de diferencia que hay entre los objetos date resultantes del ejercicio 1 y la fecha actual. """
listaDeFechasEnMilisegundos=[]
diadehoy = datetime.now()
print(diadehoy)
milisegundosDeLaFechaDehoy= int(diadehoy.timestamp()*1000)
print(milisegundosDeLaFechaDehoy)
for fecha in fechas:
    # Convertir cada fecha a un objeto datetime
    fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")
    # Convertir a milisegundos
    milisegundos = int(fecha_objeto.timestamp() * 1000)
    listaDeFechasEnMilisegundos.append(milisegundos)

for fecha in listaDeFechasEnMilisegundos:
    print(f"Diferencia de días: {round((milisegundosDeLaFechaDehoy-fecha)/86400000)}")

""" Elige una fecha de los objetos date resultantes del ejercicio 1 y  cambiar su año a 2025. """

nuevaFecha = fechas_convertidas[1]
print(nuevaFecha)
nuevaFecha=nuevaFecha.replace(year=2025)
print(nuevaFecha)


""" Convierte cada objeto datetime resultante del ejercicio 3 en una cadena con el formato DD/MM/YYYY HH:MM """

listaNuevaEjercicio6=[]
print(fecha_y_hora_Combinadas)
for fecha in fecha_y_hora_Combinadas:
    listaNuevaEjercicio6.append(datetime.strftime(fecha, "%d/%m/%Y %H:%M"))
print(listaNuevaEjercicio6)

	
