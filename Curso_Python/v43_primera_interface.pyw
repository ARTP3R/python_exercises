#!/usr/bin/python3

from tkinter import *


raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(True, True)

#raiz.iconbitmap("v42low.ico") # NO FUNCIONA, NO SÉ POR QUÉ

raiz.geometry("650x350")

raiz.config(bg="grey", bd=10, relief="groove")

mi_frame=Frame()

#mi_frame.pack(side="right")
mi_frame.pack(fill="both", expand="True")

mi_frame.config(bg="darkgrey", width="600", height="300",\
	bd=10, relief="raised", cursor="pirate")

raiz.mainloop() # SIEMPRE AL FINAL
