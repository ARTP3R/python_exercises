#!/usr/bin/python3

class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	def arranque(self):
		self.enMarcha=True
	
	def estado(self):
		if self.enMarcha:
			return "El coche está en marcha."
		else:
			return "El coche está parado."


miCoche=Coche()  # INSTANCIAR UNA CLASE

print("El largo del coche es ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")


print(miCoche.estado())

miCoche.arranque()

print(miCoche.estado())


