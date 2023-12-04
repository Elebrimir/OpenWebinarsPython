#Ejercicio 14

#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

num=int(input("Introduzca un número de 2 cirfras:"))

digit1=num//10
digit2=num%10

print("Numero introducido con las cifras invertidas:",str(digit2)+str(digit1))