#!/usr/bin/python3


def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs): #por convención pero vale cualquier nombre
		# decoraciones
		# conectar base de datos, etc
		print("Realizando cálculo")
		funcion_parametro(*args, **kwargs)
		# más decoraciones
		# desconectar base de datos, etc
		print("Cálculo finalizado.")
	return funcion_interior



@funcion_decoradora
def suma(num1, num2, num3):
	print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))


suma(7,5,10000)

resta(12,10)



potencia(base=3,exponente=3)







