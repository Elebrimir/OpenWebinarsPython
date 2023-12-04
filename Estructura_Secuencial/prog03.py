#Ejercicio 3

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cat01 = float(input("Longitud del cateto 1:"))
cat02 = float(input("Longitud del cateto 2:"))

hipotenuse = math.sqrt(cat01**2 + cat02**2)

print ("La hipotenusa de este triangulo es: %.4f" % hipotenuse)