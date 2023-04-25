mitupla=("Juan", 13,1,1995) #tupla, no son necesarios los paréntesis

milista=list(mitupla) #convertir tupla a lista

print(mitupla[2], "imprimiendo la posicion 2 de mitupla")

print(milista, "imprimiendo milista")


milista2=["Juan", 13,1,1995] #lista, SI son necesarios los paréntesis

mitupla2=tuple(milista2) #conviertiendo lista a tupla

print(mitupla2, "imprimiendo la tupla2")

print("Juan" in mitupla2, "que Juan está en la tupla2")

print(mitupla.count(13), "contando la posición de 13 en la tupla") 

print(len(mitupla), "es la longutud de la tupla")


mitupla3=("Juan", 13, 1, 1993)
nombre, día, mes, año=mitupla3 #desempaquetado de tuplas
print(mes, "variable mes")
print(nombre, "variable nombre")
print(día, "variable día")
print(año, "variable año") 