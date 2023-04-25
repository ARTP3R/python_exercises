#!/usr/bin/python3

def area_triangulo(base, altura):
	"""
	
	Calcula el area de un triángulo.
	
	>>> area_triangulo(3,6)
	9.0


	"""
	return (base*altura)/2


def area_triangulo_cadena(base, altura):
	"""
	
	Calcula el area de un triángulo.
	
	>>> area_triangulo_cadena(3,6)
	'El area del triángulo es: 9.0'

	>>> area_triangulo_cadena(4,5)
	'El area del triángulo es: 10.0'

	>>> area_triangulo_cadena(9,3)
	'El area del triángulo es: 13.5'

	"""
	return "El area del triángulo es: " + str((base*altura)/2)


def comprueba_mail(mail_usuario):
	"""
	Evalúa un email recibido en busca de la @. Si tiene una @ es correcto.
	Si tiene más de una o si esta está al final es incorrecto.

	>>> comprueba_mail('juan@cursos.com')
	True
	
	>>> comprueba_mail('juancursos.com@')
	False

	>>> comprueba_mail('juancursos.com')
	False

	>>> comprueba_mail('jua@ncu@rsos.com')
	False



	"""

	arroba=mail_usuario.count('@')
	if (arroba!=1 or mail_usuario.rfind('@')==(len(mail_usuario)-1) or mail_usuario.find('@')==0):
		return False
	else:
		return True
import doctest
doctest.testmod()