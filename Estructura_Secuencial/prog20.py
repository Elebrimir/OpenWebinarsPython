#Ejercicio 20

#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

eur=2*int(input("Cuantas monedas de 2€: "))
eur+=int(input("Cuantas de 1€: "))
cent=50*int(input("Cuantas de 50 centimos: "))
cent+=20*int(input("Cuantas de 20 centimos: "))
cent+=10*int(input("Cuantas de 10 centimos: "))

eur+=cent//100
cent%=100

print("Tenemos:",eur,"euros y",cent,"céntimos")