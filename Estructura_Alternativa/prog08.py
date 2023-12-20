# Ejercicio 8

# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el
# mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
# dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe
# imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

score = int(input('Introduzca la nota: '))
age = int(input('Introduzca la edad: '))
genre = str(input('Género M o F: ')).upper()

if score>=5 and age >= 18 and genre=='F':
    print('ACEPTADA')
elif score>=5 and age >= 18 and genre=='M':
    print('POSIBLE')
else:
    print('NO ACEPTADA')