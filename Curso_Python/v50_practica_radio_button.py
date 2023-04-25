#!/usr/bin/python3

from tkinter import *


root = Tk()

# ------------------------ posicion ventana -------------------------------

ancho_ventana = 900
alto_ventana = 300

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) +\
	"+" + str(y_ventana)
root.geometry(posicion)

root.resizable(0,0)
root.title("Ventana de ejemplo")

# -------------------------------------------------------------------------

var_opcion=IntVar()

def imprimir():
	#print(var_opcion.get())
	if var_opcion.get()==1:
		etiqueta.config(text="Elegido tetamen rico")

	elif var_opcion.get()==2:
		etiqueta.config(text="Elegido chochete sabroso")
	else:
		etiqueta.config(text="Elegido culamen tremendo")

Label(root, text="Menú:").pack()

Radiobutton(root, text="Tetamen", variable=var_opcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Chochete", variable=var_opcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Culamen", variable=var_opcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()