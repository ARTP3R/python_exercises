i=1

while i<=10:
	print("Ejecución", str(i))
	i+=1

print("Terminó la ejecución")


edad=int(input("Introduzca su edad por favor: "))
while edad<0 or edad>100:
	print("Ha introducido una edad incorrecta. Vuelva a intentarlo")
	edad=int(input("Introduzca su edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante ", edad)
print("Tiene " + str(edad) + " años.")

import math
print("Programa de cálculo de raíz cuadrada")

numero=int(input("Introduce un número por favor: "))
intentos=0
while numero<0:
	print("No se puede hallar la raíz de un número negativo")
	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		break;

	numero=int(input("Introduce un número por favor: "))
	if numero<0:
		intentos+=1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de ", str(numero), " es ", str(solucion))