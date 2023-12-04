#Ejercicio 4

#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = float(input("Valor del Primer número: "))
num2 = float(input("Valor del Segundo número: "))

plus = num1+num2
rest = num1-num2
division = num1/num2
multiply = num1*num2

print('''Resultado de la suma: %.2f
Resultado de la resta: %.2f
Resultado de la división: %.2f
Resultado de la multiplicación: %.2f''' %(plus,rest,division,multiply) )
