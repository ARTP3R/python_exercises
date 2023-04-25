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
print("Encontrar nombres de un rango de letras")
for elemento in lista_nombres:
	if re.findall("[o-t]", elemento):
		print(elemento)

print("Encontrar nombres de un rango de letras")
for elemento in lista_nombres:
	if re.findall("^[O-T]", elemento):
		print(elemento)


print("Encontrar nombres de un rango de letras")
for elemento in lista_nombres:
	if re.findall("[o-t]$", elemento):
		print(elemento)


lista_sucursales=[
	"Ma1",
	"Se1",
	"Ba1",
	"Ma2",
	"Va1",
	"Va3",
	"BaA",
	"Ma3",
	"VaA",
	"VaB",
	"MaA"
]
print("Encontrar sucursales de Madrid")
for elemento in lista_sucursales:
	if re.findall("Ma[0-3A-B]", elemento):
		print(elemento)


lista_sucursales=[
	"Ma1",
	"Se1",
	"Ba1",
	"Ma2",
	"Va1",
	"Ma:3",
	"BaA",
	"Ma3",
	"Va.A",
	"VaB",
	"Ma:A"
]
print("Encontrar sucursales de Madrid cuyo tercer caracter sea . o :")
for elemento in lista_sucursales:
	if re.findall("Ma[.:]", elemento):
		print(elemento)