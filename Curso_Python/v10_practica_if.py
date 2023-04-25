print("Programa de evaluación de notas de aliumnos")

nota_alumno=int(input("Introduzca la nota de alumno: "))

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		
	return valoracion

print(evaluacion(nota_alumno))
