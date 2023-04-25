#!/usr/bin/python3

from io import open

archivo_texto=open("v38_archivo.txt", "r+") # LECTURA Y ESCRITURA

archivo_texto.seek(len(archivo_texto.read())/2) # SITUA EL CURSOR A LA MITAD DEL TEXTO

print(archivo_texto.read())

archivo_texto.seek(11) # SITUA EL CURSOR EN EL CARACTER 11

print(archivo_texto.read())

print(archivo_texto.readline())

archivo_texto.seek(len(archivo_texto.readline())) # SITÚA EL CURSOS AL FINAL DE LA LINEA

lista_texto=archivo_texto.readlines()

lista_texto[2]="Esta linea ha sido incluída desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()