print("Asignaturas optativas año 2021")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() # cambia valor cadena a minúsculas

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura.upper()) #imprime en mayúsculas

else:
	print("La asignatura escogida no está contemplada")
