

frase = str(input("Introduzca frase: "))
contador = 0

for letra in frase:
	
	if letra=="h": #SI ES UNA h NO LA IMPRIME
		continue
		
	contador+=1
	print("Viendo la letra: " + letra)
	

print("Longitud frase: ", len(frase))
print("Longitud frase: ", contador)



email=input("Introduzca su email cachocarne: ")

for i in email:
	if i=="@":
		arroba=True
		break;

else:
	arroba=False

print(arroba)