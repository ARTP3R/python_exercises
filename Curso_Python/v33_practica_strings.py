#!/usr/bin/python3

nombre_usuario=input("Introduce tu nombre de usuario: ")

print("------------------------------------")
print("El nombre iuntroducido es:")
print(nombre_usuario.upper())
print(nombre_usuario.lower())
print(nombre_usuario.capitalize())

edad=input("Introduce la edad: ")
print(edad.isdigit())


while(edad.isdigit()==False):
	print("Por favor tontopolla, introduzca un valor numérico: ")
	edad=input("Introduce la edad: ")

if (int(edad)<18):
	print("No puede pasar.")
else:
	print("Puede pasar")