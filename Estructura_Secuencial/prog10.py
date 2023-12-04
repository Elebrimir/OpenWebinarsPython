#Ejercicio 10

#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#    55% del promedio de sus tres calificaciones parciales.
#    30% de la calificación del examen final.
#    15% de la calificación de un trabajo final.


midterm1=float(input("Calificación Primer Parcial: "))
midterm2=float(input("Calificación Segundo Parcial: "))
midterm3=float(input("Calificación Tercer Parcial: "))
finalExam=float(input("Calificación de la Prueba Final: "))
finalWork=float(input("Calificación Trabajo Final: "))

finalMark=(0.55*(midterm1+midterm2+midterm3)/3)+(0.3*finalExam)+(0.15*finalWork)

print("La nota final de la materia es de: %.2f" %finalMark)