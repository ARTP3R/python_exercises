#!/usr/bin/python3

def evaluaEdad(edad):
	
	# EJEMPLO DE RAISE
	if edad<0:
		raise TypeError("No se permiten edades negativas.")


	if edad<20:
		return "Eres muy joven."
	elif edad<40:
		return "Eres joven."
	elif edad<65:
		return "Eres maduro."
	elif edad <100:
		return "Cuídate."

print(evaluaEdad(98))


print("--------------------------------------------------------------")

import math

def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError ("El número no puede ser negativo.")

	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))


try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print ("Programa terminado")