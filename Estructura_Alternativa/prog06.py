# Ejercicio 6

# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

chain = str(input('Introduzca una palabra: '))

if chain == chain.upper():
    print('La cadena introducida esta en mayúsculas')
else:
    print('La cadena introducida no esta en mayúsculas')