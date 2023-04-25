#!/usr/bin/python3

class Coche():
	
	def __init__(self):    # ESTO ES UN CONSTRUCTOR, UNA FUNCIÓN CON EL NOMBRE __init__
	                       # PARA ESTABLECER LOS VALORES INICIALES.
		self.__largoChasis=250   
		self.__anchoChasis=120 # PARA CREAR VARIABLES ENCAPSULADAS SE LES PONE __ DELANTE
		self.__ruedas=4        # DEL NOMBRE Y ASÍ SOLO SE PUEDEN MODIFICAR MEDIANTE
		self.__enMarcha=False  # LOS MÉTODOS

	def arrancar(self, arrancamos):
		self.enMarcha=arrancamos

		if (self.enMarcha):
			return "El coche está en marcha."
		else:
			return "El coche está parado."
	
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Ancho de ", self.__anchoChasis,\
		" y un largo de ", self.__largoChasis)


miCoche=Coche()  # ESTO ES INSTANCIAR UNA CLASE

print(miCoche.arrancar(True))

miCoche.estado()

print("---------------------- A continuación creamos el segundo objeto --------------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas=2        # AL ESTAR RUEDAS ENCAPSULADA NO SE PUEDE MODIFICAR EL VALOR
miCoche2.__ruedas=2      # DESDE FUERA DEL OBJETO, NI AUNQUE USEMOS __

miCoche2.estado()
