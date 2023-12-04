#Ejercicio 12

#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

import math

x1=float(input("Valor de x1:"))
y1=float(input("Valor de y1:"))
x2=float(input("Valor de x2:"))
y2=float(input("Valor de y2:"))

cat1=x2-x1
cat2=y2-y1

distance=math.sqrt(cat1**2+cat2**2)

print("La distancia entre los dos puntos es de: %.2f" %distance)