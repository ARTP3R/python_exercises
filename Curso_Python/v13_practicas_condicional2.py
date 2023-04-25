print("Programa de becas 2021")
dist_esc=int(input("Introduzca distancia a escuela en Km: "))
print(dist_esc)

num_herm=int(input("Introduzca número de hermanos en el centro: "))
print(num_herm)

salario_fam=int(input("Introduzca salario familiar anual bruto: "))
print(salario_fam)

if dist_esc>40 and num_herm>2 or salario_fam<=20000:
	print("Enhorabuena. Tiene derecho a beca.")
else:
	print("Lo siento. No tiene derecho a beca.")