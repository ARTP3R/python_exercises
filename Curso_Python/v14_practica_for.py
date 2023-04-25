#!/usr/bin/python3

for i in ["Primavera", "Verano", "Otoño", "Invierno", 3]:
	print("Hola", end=" ")
	print(i)




arrobas=0
puntos=0
caracteres_OK=0
caracteres_incorrectos=0
correcto=True
detectado_dominio=False
cadena_dominio=""
detectada_extension=False
cadena_extension=""
email=input("Introduzca su email: ")
print("Ha introducido el email ", str.lower(email))


for i in email:
	print("Carácter analizado: ", i, end=" ")
	
	if(i=="@"):
		arrobas+=1
		print("Arroba. A partir de aquí empieza el dominio del email. Arrobas = ", arrobas)
		detectado_dominio=True
		cadena_dominio=""

	elif(i=="." and detectado_dominio==True):
		puntos+=1
		print("Punto de la dirección del dominio del email. Puntos = ", puntos)
		cadena_dominio = cadena_dominio + i
		cadena_extension = cadena_extension + i
		detectada_extension=True

	elif(i=="."):
		puntos+=1
		print("Punto. Puntos = ", puntos)
		cadena_dominio=""
		cadena_extension=""
					
	elif(i=="-" or i=="_"):
		caracteres_OK+=1
		print("Correcto. Es un carácter especial admitido en la dirección de email.")
		print("Caracteres especiales admitidos = ", caracteres_OK)
		if detectado_dominio==True:
			cadena_dominio = cadena_dominio + i
		if detectada_extension==True:
			cadena_extension = cadena_extension + i

	elif(str.isalnum(i)==False):
		caracteres_incorrectos+=1
		correcto=False
		print("Incorrecto. No es una arroba ni un punto ni un carácter especial admitido\
		 en la dirección de email.")
		print("Caracteres especiales NO admitidos = ", caracteres_incorrectos)
		if detectado_dominio==True:
			cadena_dominio = cadena_dominio + i
		if detectada_extension==True:
			cadena_extension = cadena_extension + i

	else:
		print("Correcto.")
		if detectado_dominio==True:
			cadena_dominio = cadena_dominio + i
		if detectada_extension==True:
			cadena_extension = cadena_extension + i

print("Total Puntos ............................. ", puntos)
print("Total Arrobas ............................ ", arrobas)
print("Total Caracteres especiales admitidos ···· ", caracteres_OK)
print("Total Caracteres especiales NO admitidos · ", caracteres_incorrectos)
print("Dominio de email ......................... ", cadena_dominio)
print("Extensión de dominio ..................... ", cadena_extension)
if arrobas==1 and puntos>=1 and correcto==True and str.isalnum(cadena_extension)==True:  #PENDIENTE DE DEPURAR. No sé pa que sirve esto que hice.
	print("Es una dirección de email correcta")

elif  str.isalnum(cadena_extension)==False:
	print("Extensión de dirección de dominio incorrecta")
else:
	print("NO es una dirección de email correcta") #PENDIENTE DE DEPURAR