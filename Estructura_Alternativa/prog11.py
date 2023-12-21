# Ejercicio 11

# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

#     Si se cumple Pitágoras entonces es triángulo rectángulo
#     Si sólo dos lados del triángulo son iguales entonces es isósceles.
#     Si los 3 lados son iguales entonces es equilátero.
#     Si no se cumple ninguna de las condiciones anteriores, es escaleno.

sideA = int(input("Introduzca los datos del Lado A: "))
sideB = int(input("Introduzca los datos del Lado B: "))
sideC = int(input("Introduzca los datos del Lado C: "))

if sideA**2 == (sideB**2 + sideC**2):
    print("Es un Triangulo Rectangulo")
elif (sideA == sideB and sideA != sideC) or (
    sideA == sideC and sideA != sideB or (sideB == sideC and sideB != sideA)
):
    print("Es un Triangulo Isósceles.")
elif sideA == sideB and sideA == sideC and sideB == sideC:
    print("Es un Triangulo Equilatero.")
else:
    print("Es un Triangulo Escaleno")