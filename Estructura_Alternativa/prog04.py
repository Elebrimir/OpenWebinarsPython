#Ejercicio 4

#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

if num2!=0:
    print("La división es: ",num1/num2)
else:
    print("No se puede dividir entre 0")