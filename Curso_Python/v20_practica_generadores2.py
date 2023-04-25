def devuelve_letras(*letras): # USANDO YIELD
	for elemento in letras:
		print(elemento, " - elemento recorrido")
		for subElemento in elemento:
			print(subElemento, " - subElemento recorrido")
			yield subElemento

letras_devueltas=devuelve_letras(str(input("Introduzca texto: ")),\
	str(input("Introduzca texto: ")),\
	str(input("Introduzca texto: ")),\
	"ABCD", "EFGH", "IJKL")


print("-----------------------")

i=0
while i < 10:
	print(next(letras_devueltas), " - imprimiendo next(letras_devueltas)")
	i+=1

print("-----------------------")






def devuelve_letras_ciudades(*ciudades): # USANDO YIELD FROM
	for elemento in ciudades:
		print(elemento, " - elemento recorrido")
		yield from elemento

letras_ciudades_devueltas=devuelve_letras_ciudades(\
	str(input("Introduzca una ciudad: ")),\
	str(input("Introduzca una ciudad: ")),\
	str(input("Introduzca una ciudad: ")),\
	"Madrid", "París", "Roma")

print("-----------------------")
i=0
longitud=(int(input("Introduzca longitud: ")))
while i < longitud:
	try:
		print(next(letras_ciudades_devueltas), " - imprimiendo next(letras_ciudades_devueltas)")
		i+=1
	except StopIteration:
		print("Final del array bidimensional alcanzado.")
		print("break")
		break
	
	