#Ejercicio 13

#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

num=float(input("Introduzca un número:"))

squareRoot=num**(1/2)
cubeRoot=num**(1/3)

print("La raíz cuadrada de",num,"es: %.2f" %squareRoot)
print("La raíz cúbica de",num,"es: %.2f" %cubeRoot)