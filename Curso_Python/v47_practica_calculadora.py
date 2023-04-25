#!/usr/bin/python3

from tkinter import *


raiz = Tk()

raiz.title("CalcuLOCA")

mi_frame=Frame(raiz)
mi_frame.pack()

operacion=""
resultado=0

ancho_boton=7
alto_boton=3
fuente_boton=("Arial",20)

# --------------------------- pantalla ---------------------------

numero_pantalla=StringVar()

pantalla=Entry(mi_frame, font=("Arial",20), width=35, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#01f943", justify="right")

# --------------------------- pantalla ---------------------------

def numero_pulsado(num):
	global operacion
	if operacion!="":
		numero_pantalla.set(num)
		operacion=""
	else:
		numero_pantalla.set(numero_pantalla.get() + num)

# --------------------------- función suma ---------------------------

def suma(num):
	global operacion

	global resultado

	resultado+=int(num)
	operacion="suma"
	numero_pantalla.set(resultado)

	# --------------------------- función resta ---------------------------

def resta(num):
	global operacion

	global resultado

	resultado=resultado-int(num)
	operacion="resta"
	numero_pantalla.set(resultado)

	# --------------------------- función total ---------------------------

def total(num):
	global resultado

	numero_pantalla.set(resultado+int(numero_pantalla.get()))
	resultado=0

# --------------------------- fila 1 ---------------------------

boton7=Button(mi_frame, text="7", command=lambda:numero_pulsado("7"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton7.grid(row=2, column=1)
boton8=Button(mi_frame, text="8", command=lambda:numero_pulsado("8"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton8.grid(row=2, column=2)
boton9=Button(mi_frame, text="9", command=lambda:numero_pulsado("9"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton9.grid(row=2, column=3)
boton_div=Button(mi_frame, text="/", font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_div.grid(row=2, column=4)

# --------------------------- fila 2 ---------------------------

boton4=Button(mi_frame, text="4", command=lambda:numero_pulsado("4"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton4.grid(row=3, column=1)
boton5=Button(mi_frame, text="5", command=lambda:numero_pulsado("5"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton5.grid(row=3, column=2)
boton6=Button(mi_frame, text="6", command=lambda:numero_pulsado("6"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton6.grid(row=3, column=3)
boton_mult=Button(mi_frame, text="X", font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_mult.grid(row=3, column=4)

# --------------------------- fila 3 ---------------------------

boton1=Button(mi_frame, text="1", command=lambda:numero_pulsado("1"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton1.grid(row=4, column=1)
boton2=Button(mi_frame, text="2", command=lambda:numero_pulsado("2"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton2.grid(row=4, column=2)
boton3=Button(mi_frame, text="3", command=lambda:numero_pulsado("3"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton3.grid(row=4, column=3)
boton_res=Button(mi_frame, text="-", command=lambda:resta(numero_pantalla.get()), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_res.grid(row=4, column=4)

# --------------------------- fila 4 ---------------------------

boton_cero=Button(mi_frame, text="0", command=lambda:numero_pulsado("0"), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_cero.grid(row=5, column=1)
boton_coma=Button(mi_frame, text=",", command=lambda:numero_pulsado(","), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_coma.grid(row=5, column=2)
boton_igual=Button(mi_frame, text="=", command=lambda:total(numero_pantalla.get()), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_igual.grid(row=5, column=3)
boton_sum=Button(mi_frame, text="+", command=lambda:suma(numero_pantalla.get()), font=fuente_boton, width=ancho_boton, heigh=alto_boton)
boton_sum.grid(row=5, column=4)

raiz.mainloop() # SIEMPRE AL FINAL