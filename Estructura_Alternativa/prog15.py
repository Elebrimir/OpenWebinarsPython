# Ejercicio 15

# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

nrStudents = int(input("Introduzca la cantidad de alumnos para el viaje: "))

if nrStudents >= 100:
    print("El precio por alumno es de 65€.")
elif nrStudents < 100 and nrStudents >= 50:
    print("El precio por alumno es de 70€.")
elif nrStudents < 50 and nrStudents >= 30:
    print("El precio por alumno es de 95€")
elif nrStudents < 30:
    print("El precio por alumno es de ", 4000 / nrStudents, "€")
else:
    print("Los datos introducidos no son correctos")
