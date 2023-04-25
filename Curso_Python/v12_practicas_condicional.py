edad=722

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad es incorrecta")




salario_presi=int(input("Introduzca salario presidente: "))
print("Salario presidente: " + str(salario_presi))

salario_dire=int(input("Introduzca salario director: "))
print("Salario director: " + str(salario_dire))

salario_jefearea=int(input("Introduzca salario jefe de area: "))
print("Salario jefe de area: " + str(salario_presi))

salario_admi=int(input("Introduzca salario administrativo: "))
print("Salario administrativo: " + str(salario_admi))

if salario_admi<salario_jefearea<salario_dire<salario_presi:
	print("Todo ok")
else:
	print("Aquí hay gato encerrado")