#!/usr/bin/python3

from tkinter import *


raiz = Tk()

mi_frame=Frame(raiz, width=1200, height=600)
mi_frame.pack()


cuadro_texto=Entry(raiz)
cuadro_texto.grid(row=2, column=1)

nombre_label=Label(mi_frame, text="Nombre:")
nombre_label.grid(row=0, column=0)

raiz.mainloop() # SIEMPRE AL FINAL
