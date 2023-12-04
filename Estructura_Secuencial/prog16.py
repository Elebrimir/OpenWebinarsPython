#Ejercicio 16

#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

v1 = float(input("Introduzca la velocidad del vehiculo 1: "))
v2 = float(input("Introduzca la velocidad del vehiculo 2, que es más rapido que el vehiculo 1: "))
distance = float(input("Distancia entre los dos vehiculos: "))

difVel=v2-v1
timeToEncounter=(distance/difVel)*60

print("Tiempo (min) que tardará el Vehiculo 2 para alcanzar al vehiculo 1: %d" %timeToEncounter)