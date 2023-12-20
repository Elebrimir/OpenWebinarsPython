#Ejercicio 7

#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

   # El exponente sea positivo, sólo tienes que imprimir la potencia.
   # El exponente sea 0, el resultado es 1.
   # El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=int(input('Introduce la base: '))
exponent=int(input('Introduce el exponente: '))

if exponent>0:
    print(base**exponent)
elif exponent==0:
    print(1)
elif exponent<1:
    print(1/base**abs(exponent))
else:
    print('Datos introducidos no válidos')
