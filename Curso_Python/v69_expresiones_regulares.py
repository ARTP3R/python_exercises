#!/usr/bin/python3

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla."

print(re.search("aprender", cadena, flags=0))

texto_buscar="aprender"

if re.search(texto_buscar, cadena) is not None:
	print("Texto encontrado")
else:
	print("Texto no encontrado")

texto_encontrado=re.search(texto_buscar, cadena)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())

texto_buscar="Python"

print(re.findall(texto_buscar, cadena))
print(len(re.findall(texto_buscar, cadena)))
