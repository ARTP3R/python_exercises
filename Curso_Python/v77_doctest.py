#!/usr/bin/python3

import math


def raiz_cuadrada(lista_numeros):
	"""
	Devuelve lista con la raíz cuadrada de los elementos
	numéricos pasados por parámetros en otra lista.

	>>> lista=[]
	>>> for i in [4,9,16]:
	...		lista.append(i) 			# LA IDENTACIÓN VA INDICADA CON TRES PUNTOS
	>>> raiz_cuadrada(lista)
	[2.0, 3.0, 4.0]

	
	>>> lizta=[]
	>>> for i in [4,-9, 16]:
	... 	lista.append(i)				# LA IDENTACIÓN VA INDICADA CON TRES PUNTOS
	>>> raiz_cuadrada(lista)
	Traceback (most recent call last):
		...								# TAMBIÉN SE PUEDE USAR DE COMODÍN INTERMEDIO
	ValueError: math domain error



	"""



	return [math.sqrt(n) for n in lista_numeros]



print (raiz_cuadrada([9,16,25,36]))

import doctest
doctest.testmod()