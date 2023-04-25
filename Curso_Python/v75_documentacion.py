#!/usr/bin/python3

from v34_modulos import v34_funciones_matematicas

"""
Programa para practicar documentación dentro del código.
"""


class Areas:
	"""
	Esta clase calcula las areas de diversas formas geométricas.
	"""
	def area_cuadrado(lado):
		"""
		Calcula el area de un cuadrado elevando al cuadrado el lado pasado por parámetro.
		"""
		return "El área del cuadrado es: " + str(lado*lado)


	def area_triangulo(base, altura):
		"""
		Calcula el area de un triángulo utilizandolos parámetros base y altura.
		"""

		return  "El área del triángulo es: " + str((base*altura)/2)


print(Areas.area_cuadrado(1))
print("--------------")
print(Areas.area_cuadrado.__doc__)
print("--------------")
help(Areas.area_cuadrado)
print("--------------")
help(Areas)
print("--------------")
help(v34_funciones_matematicas)