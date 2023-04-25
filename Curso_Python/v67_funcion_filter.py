#!/usr/bin/python3



numeros=[17,24,7,39,8,51,92]


# opcion 1

def numero_par(num):
	if num % 2==0:
		return True

print(list(filter(numero_par, numeros)))


# opcion 2

print(list(filter(lambda numero_par2: numero_par2%2==0, numeros)))




class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

lista_empleados=[
Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidente", 85000),
Empleado("Antonio", "Administrativo", 55000),
Empleado("Sara", "Secretario", 26000),
Empleado("Mario", "Asistente", 25000)
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, lista_empleados)

print("Salarios superiores a 50000")
for empleado_salario in salarios_altos:
	print(empleado_salario)






