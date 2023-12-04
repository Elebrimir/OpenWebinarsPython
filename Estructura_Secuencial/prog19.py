#Ejercicio 19

#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

correctAnswer = int(input("Respuestas correctas: "))
incorrectAnswer = int(input("Respuestas incorrectas: "))
nullAnswer = int(input("Respuestas en Blanco: "))

result = (correctAnswer*5)+(incorrectAnswer*-1)+(nullAnswer*0)

print("El resultado de la prueba es de: ", result)