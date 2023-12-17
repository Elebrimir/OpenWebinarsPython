# Ejercicio 1

# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segundo número: '))

if num1>num2:
    print("El primero es mayor")
elif num2>num1:
    print("El segundo es mayor")
else:
    print("Son iguales")