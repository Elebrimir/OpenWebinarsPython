#Ejercicio 17

#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

exitTimeHour = int(input("Hora: "))
exitTimeMinutes = int(input("Minutos: "))
exitTimeSeconds = int(input("Segundos: "))
travelTime = int(input("Tiempo de viaje a la ciudad B en segundos: "))
travelDay=0
travelHour=0
travelMinute=0
travelSecond=0

if travelTime>=86400:
    travelDay=(travelTime//86400)
    travelTime-=travelDay*86400

if travelTime<86400 and travelTime>=3600:
    travelHour = travelTime//3600
    travelTime-= travelHour*3600

if travelTime<3600 and travelTime>=60:
    travelMinute = travelTime//60
    travelTime-=travelMinute*60

if travelTime<60:
    travelSecond = travelTime

metaTimeDay = 0+travelDay
metaTimeHour = exitTimeHour+travelHour
metaTimeMinutes = exitTimeMinutes+travelMinute
metaTimeSeconds = exitTimeSeconds+travelSecond

if metaTimeDay>365:
    metaTimeDay-=365

if metaTimeHour>24:
    metaTimeDay+=1
    metaTimeHour-=24

if metaTimeMinutes>60:
    metaTimeHour+=1
    metaTimeMinutes-=60

if metaTimeSeconds>60:
    metaTimeMinutes+=1
    metaTimeSeconds-=60

print("Hora de llegada:",metaTimeDay,"dias,",metaTimeHour,"horas,",metaTimeMinutes,"minutos",metaTimeSeconds,"segundos")
