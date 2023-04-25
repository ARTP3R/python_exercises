#!/usr/bin/python3

import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con nombre: ", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class lista_personas:

	personas=[]

	def __init__(self):
		lista_de_personas=open("v41_fichero_externo.bin", "ab+")
		lista_de_personas.seek(0)

		try:
			self.personas=pickle.load(lista_de_personas)
			print("Se han cargado {} personas del ficharo externo".format(len(self.personas)))
		except:
			print("El fichero está vacío.")
		finally:
			lista_de_personas.close()
			del lista_de_personas

	def agregar_personas(self, p):
		self.personas.append(p)
		self.guardar_personas_fichero_externo()
	def mostrar_personas(self):
		for p in self.personas:
			print(p)
	def guardar_personas_fichero_externo(self):
		lista_de_personas=open("v41_fichero_externo.bin", "wb")
		pickle.dump(self.personas, lista_de_personas)
		lista_de_personas.close()
		del lista_de_personas
	def mostrar_info_fichero_externo(self):
		print("Fichero externo")
		for p in self.personas:
			print(p)

mi_lista=lista_personas()
persona=Persona("Paco", "Masculino", 43)
mi_lista.agregar_personas(persona)

persona=Persona("Manolo", "No Binario", 13)
mi_lista.agregar_personas(persona)

persona=Persona("Sandra", "Femenino", 29)
mi_lista.agregar_personas(persona)

mi_lista.mostrar_info_fichero_externo()