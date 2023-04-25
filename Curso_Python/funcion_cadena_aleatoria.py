#!/usr/bin/python3

def cadena_aleatoria(longitud_cadena):
	import string
	import random
	string_random=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud_cadena))
	return string_random

def intro_reg_aleatorio():
	str_nombre=cadena_aleatoria(12)
	str_passwd=cadena_aleatoria(8)
	str_apellido=cadena_aleatoria(12)
	str_direccion=cadena_aleatoria(30)
	str_comentario=cadena_aleatoria(50)

	lista_usuarios=[str_nombre, str_passwd, str_apellido, str_direccion, str_comentario]