#Ejercicio 8

# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
# y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

salary=float(input("Introduzca el salario base: "))
sales=int(input("Introduzca las ventas del mes: "))

commission=(salary*0.1)*sales
totalFee=salary+commission

print("Las comisiones ascienden a: %.2f" %commission)
print("El total de la remuneración de este mes es de: %.2f" %totalFee)