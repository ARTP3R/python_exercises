#!/usr/bin/python3

import pickle

from v40_serializar_objetos import Vehiculo

fichero_apertura=open("v40_fichero_coches.bin", "rb")

mis_coches=pickle.load(fichero_apertura)

fichero_apertura.close()

for c in mis_coches:
	print(c.estado())