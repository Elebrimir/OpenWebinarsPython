#Ejercicio 9

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

purchase = float(input("Introduzca el valor de la compra: "))

discount = purchase*0.15

total = purchase - discount

print("La cantidad a pagar con el descuento del 15 por ciento es de: %.2f" %total)