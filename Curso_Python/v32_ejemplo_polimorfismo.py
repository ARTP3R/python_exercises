#!/usr/bin/python3

class Coche(object):
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")


class Moto(object):
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")



class Camion(object):
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")



def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


VoyManejando=Moto()

desplazamientoVehiculo(VoyManejando)

VoyManejando=Camion()

desplazamientoVehiculo(VoyManejando)