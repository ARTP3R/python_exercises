#!/usr/bin/python3


class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

lista_empleados=[
Empleado("Juan", "Director", 6750),
Empleado("Ana", "Presidente", 7850),
Empleado("Antonio", "Administrativo", 2550),
Empleado("Sara", "Secretario", 2260),
Empleado("Mario", "Asistente", 1250)
]


def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03
		print("Aplicada comisión por sueldo menor de 3000€ a "+empleado.nombre)
	return empleado

lista_empleados_comision=map(calculo_comision, lista_empleados)

for empleado in lista_empleados_comision:
	print(empleado)



