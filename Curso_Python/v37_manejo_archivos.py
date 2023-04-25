#!/usr/bin/python3

from io import open

archivo_texto=open("v37_archivo.txt", "w") # SOBREESCRIBE

archivo_texto.close()

archivo_texto=open("v37_archivo.txt", "a") # AÑADE

for i in "abcdefg":
	frase=(" Estupendo día para estudiar Python \n el miércoles\n")

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto=open("v37_archivo.txt", "r") #SOLO LECTURA

texto=archivo_texto.read()

archivo_texto.close()

print(texto)


archivo_texto=open("v37_archivo.txt", "r")

lineas_texto=archivo_texto.readlines()   # CREA UNA LISTA

archivo_texto.close()

print(lineas_texto[1]) 