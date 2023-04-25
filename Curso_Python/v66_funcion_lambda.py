#!/usr/bin/python3


def area_triangulo2(base, altura):
	return (base*altura)/2

print(area_triangulo2(5,7))

triangulo2=area_triangulo2(9,6)

print(triangulo2)




area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(5,7))




al_cubo=lambda numero:numero**3

al_cubo2=lambda numero:pow(numero,3)

print(al_cubo(3))
print(al_cubo2(3))

destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))