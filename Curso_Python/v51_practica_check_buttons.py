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

tetamen=IntVar()
culamen=IntVar()
chochamen=IntVar()

def opcion_sesuar():
	opcion_escogida=""
	if(culamen.get()==1):
		opcion_escogida+=" culamen"
	if(tetamen.get()==1):
		opcion_escogida+=" tetamen"
	if(chochamen.get()==1):
		opcion_escogida+=" chochamen"

	texto_final.config(text=opcion_escogida)

foto=PhotoImage(file="Imágenes/v44logo.gif")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elija qué va a comer: ", width=50).pack()

Checkbutton(root, text="Tetamen", variable=tetamen,\
	onvalue=1, offvalue=0, command=opcion_sesuar).pack()
Checkbutton(root, text="Culamen", variable=culamen,\
	onvalue=1, offvalue=0, command=opcion_sesuar).pack()
Checkbutton(root, text="Chochamen", variable=chochamen,\
	onvalue=1, offvalue=0, command=opcion_sesuar).pack()


etiqueta=Label(root)
etiqueta.pack()

texto_final=Label(frame)
texto_final.pack()

root.mainloop()