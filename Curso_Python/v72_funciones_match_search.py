#!/usr/bin/python3

import re

nombre1="Jara López"
nombre2="Antonio Gómez"
nombre3="Lara López"

if re.match(".ara", nombre1, re.IGNORECASE):
	print("Nombre encontrado")
else:
	print("Nombre no encontrado")

cadena1="Jara López"
cadena2="2456467234678"
cadena3="a2456467234678"


if re.match("\d", cadena2):
	print("comienza por un número")
else:
	print("no comienza por un número")



nombre1="Jara López"
nombre2="Antonio Gómez"
nombre3="Lara López"

if re.search("López", nombre1, re.IGNORECASE):
	print("Nombre encontrado")
else:
	print("Nombre no encontrado")


codigo1="asdgfas71gasrhgarsghrh"
codigo2="adsfgadsfrgrth71aerhreh"
codigo3="shrethdhsdrthasdrtharh"

if re.search("71", codigo2):
	print("Código encontrado")
else:
	print("Código no encontrado")