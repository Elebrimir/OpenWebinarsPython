# Ejercicio 10

# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
# circunferencias y las clasifique en uno de estos estados:

#   exteriores
#   tangentes exteriores
#   secantes
#   tangentes interiores
#   interiores
#   concéntricas

from math import sqrt


x1 = int(input("Introduzca X1: "))
y1 = int(input("Introduzca y1: "))
x2 = int(input("Introduzca X2: "))
y2 = int(input("Introduzca y2: "))
r1 = int(input("Introduzca r1: "))
r2 = int(input("Introduzca r2: "))

# Calculamos la distacia entre los dos puntos centrales
distanceBetweenCenters = sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
radiiAddition = r2 + r1
radiiDiference = abs(r2 - r1)

if distanceBetweenCenters > radiiAddition:
    print("Son circumferencias exteriores.")
elif distanceBetweenCenters == radiiAddition:
    print("Son circumferencias tangentes exteriores.")
elif distanceBetweenCenters > radiiDiference:
    print("Son circumferencias secantes.")
elif distanceBetweenCenters == radiiDiference:
    print("Son circumferencias tangentes interiores.")
elif distanceBetweenCenters < radiiDiference and x1 != x2:
    print("Son circumferencias interiores.")
elif x1 == x2 and y1 == y2:
    print("Son circumferencias concéntricas.")
else:
    print("Los datos introducidos no són válidos.")
