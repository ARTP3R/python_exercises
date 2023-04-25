def divide():
	try:
		op1=float(input("Número 1: "))
		op2=float(input("Número 2: "))
		print("La división es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido es erroneo.")

	except ZeroDivisionError:
		print("No se puede dividir entre 0.")

	except:
		print("Error desconocido.")
	
	finally: # SE EJECUTA SIEMPRE. ES OBLIGATORIO SI NO SE USA NINGÚN EXCEPT.

		print("Cálculo finalizado.")

divide()