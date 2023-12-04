#Ejercicio 15

#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

numA=int(input("Introduce el valor de A: "))
numB=int(input("Introduce el valor de B: "))

numC=numA
numA=numB
numB=numC

print("Ahora el valor de A es",numA,"y el valor de B es",numB)