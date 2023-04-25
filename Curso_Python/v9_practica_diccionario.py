midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

print(midiccionario, "este es el diccionario")

midiccionario["Italia"]="Lisboa"

print(midiccionario, "este es el diccionario con Italia añadido")

midiccionario["Italia"]="Roma"

print(midiccionario, "este es el diccionario con Italia corregido")

del midiccionario["Reino Unido"]

print(midiccionario, "este es el diccionario con Reino Unido borrado")

print(midiccionario["Italia"] + "aaaaaaaaaaaaa")


milista=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario2={milista[0]:"Madrid", milista[1]:"París", milista[2]:"Londres", milista[3]:"Berlín"}
print(midiccionario2["Francia"], "contenido de clave indicada habiendo creado las claves a partir de una lista")

mitupla=("España", "Francia", "Reino Unido", "Alemania")
midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(midiccionario2["España"], "contenido de clave indicada habiendo creado las claves a partir de una tupla")

#diccionario contiene diccionario que contiene una tupla
midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":(1991, 1992, 1993, 1996, 1997, 1998)}}

print(midiccionario3.keys(), "son las claves del diccionario3")
print(midiccionario3.values(), "son los valores del diccionario3")
print(midiccionario3["anillos"], "es el contenido del sub diccionario anillos")
print(" ")
print((midiccionario3), "es el contenido del diccionario")
print(len(midiccionario3), "es la longitud del diccionario")


