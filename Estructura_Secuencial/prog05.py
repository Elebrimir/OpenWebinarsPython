# Ejercicio 5

# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

# C = (F-32)*5/9

farenheit = float(input("Introduzca la temperatura en ºF: "))

celsius = (farenheit-32)*5/9

print("La temperatura en ºCelsius es de: %.2f" % celsius)