#Ejercicio 11

#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

import math

num1=float(input("Introduzca el valor del primer número: "))
num2=float(input("Introduzca el valor del segundo número: "))

distance=abs(num1-num2)

print("La distancia entre los dos números de de: %d" %distance)