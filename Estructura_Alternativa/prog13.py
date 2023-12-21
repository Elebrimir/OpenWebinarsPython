# Ejercicio 13

# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

day = int(input("Introduzca el dia: "))
month = int(input("Introduzca el mes(búmero): "))
year = int(input("Introduzca el año: "))

if (
    (day <= 30 and month == (4 or 6 or 9 or 11))
    or (day <= 31 and month == (1 or 3 or 5 or 7 or 8 or 10 or 12))
    or (day <= 29 and month == 2)
):
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
