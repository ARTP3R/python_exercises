#!/usr/bin/python3


def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		# decoraciones
		# conectar base de datos, etc
		print("Realizando cálculo")
		funcion_parametro()
		# más decoraciones
		# desconectar base de datos, etc
		print("Cálculo finalizado.")
	return funcion_interior



@funcion_decoradora
def suma():
	print(2+2)

@funcion_decoradora
def resta():
	print(6-3)

suma()

resta()











