# Ejercicio 14

# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

initialPrice = float(input("Introduzca precio inicial de la Uva: "))
grapeType = str(input("Indique si es del tipo A o B: ")).upper()
grapeSize = int(input("Indique el tamaño de la uva, 1 o 2: "))

if grapeType == "A" and grapeSize == 1:
    print("La ganancia es del ", (initialPrice + 20 * 100) / initialPrice, "%")
elif grapeType == "A" and grapeSize == 2:
    print("La ganancia es del ", (initialPrice + 30 * 100) / initialPrice, "%")
elif grapeType == "B" and grapeSize == 1:
    print("La ganancia es del ", (initialPrice - 30 * 100) / initialPrice, "%")
elif grapeType == "B" and grapeSize == 2:
    print("La ganancia es del ", (initialPrice - 50 * 100) / initialPrice, "%")
else:
    print("Error en los datos introducidos")
