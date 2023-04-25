#!/usr/bin/python3

import re

lista_nombres=[
	"Ana Gómez",
	"Sandra Gon",
	"Sandra Pérez",
	"María Martín",
	"Sandra López",
	"Santiago Martín"
]
print("Encontrar nombres que empiecen por Sandra")
for elemento in lista_nombres:
	if re.findall("^Sandra", elemento):
		print(elemento)

print("Encontrar nombres que terminen por Martín")
for elemento in lista_nombres:
	if re.findall("Martín$", elemento):
		print(elemento)



lista_dominios=[
	"http://pildorasinformaticas.es",
	"ftp://pildorasinformaticas.es",
	"http://google.es",
	"ftp://google.es",
	"http://informaticaenespaña.es"
]

print("Encontrar dominios que comiencen por ftp")
for elemento in lista_dominios:
	if re.findall("^ftp", elemento):
		print(elemento)

print("Encontrar dominios que contengan la Ñ")
for elemento in lista_dominios:
	if re.findall("[ñ]", elemento):
		print(elemento)



lista_personas=[
	"hombres",
	"mujeres",
	"mascotas",
	"niños",
	"niñas",
	"niñes",
	"camión",
	"camion",
	"camiones"
]
print("Encontrar niños de forma inclusiva")
for elemento in lista_personas:
	if re.findall("niñ[oa]s", elemento):
		print(elemento)

print("Encontrar camiones con tilde o sin ella")
for elemento in lista_personas:
	if re.findall("cami[oó]n", elemento):
		print(elemento)