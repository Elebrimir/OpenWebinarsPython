#Ejercicio 5

#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

user=str(input("Introduce el ususario: "))
password=str(input("Introduce la contraseña: "))

if user=='pepe' and password=='asdasd':
    print("Has entrado al sistema")
else:
    print("El usuario o la contraseña no són válidos")