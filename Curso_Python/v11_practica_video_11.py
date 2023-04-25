
num1=(int(input("Introduce un numero: ")))
num2=(int(input("Introduce otro numero: ")))


def DevuelveMax(n1, n2):
	if n1 < n2:
		mx=n2
	elif n2 < n1:
		mx=n1
	else:
		mx="Ninguno por que son iguales"
	print(mx)


print("el número más alto es...")

DevuelveMax(num1, num2)
