


def generaPares2(limite2): #USANDO UNA LISTA SERÍA ASÍ
	num2=1
	milista2=[]
	while num2<limite2:
		milista2.append(num2*2)
		num2+=1
	return milista2
print(generaPares2(10))


def generaPares(limite): # CON UN GENERADOR ES ASÍ
	num=1
	
	while num<limite:
		yield num*2
		num+=1
devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Aquí podría ir más código...")
print(next(devuelvePares))
print("Aquí podría ir más código...")
print(next(devuelvePares))

for i in devuelvePares:
	print(i, " (valor de i)")
	print("Código generado automaticamente...")

