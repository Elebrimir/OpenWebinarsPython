#Ejercicio 7

#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutes=int(input("Introduzca la cantidad de minutos a convertir: "))

hours=minutes//60
minutesRest=minutes%60

print("El resultado es:",hours,"horas y",minutesRest,"minutos")