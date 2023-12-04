#Ejercicio 2

#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Introduce la base del rectangulo:"))
height = float(input("Introduce la altura del rectangulo:"))

perimeter = 2*base+2*height
area = base * height

print("El perimetro del rectangulo es:",perimeter)
print("El area del rectangulo es:",area)