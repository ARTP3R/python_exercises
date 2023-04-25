for i in range(5,50,3):
	print(f"Valor de i = {i}", end=" ")
	print("Valor de i = ", i, end=" ")
	print("Valor de i = " + str(i))

valido=False
email=input("Introduzca su email: ")

for i in range(len(email)):

	if email[i]=="@":
		valido=True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")