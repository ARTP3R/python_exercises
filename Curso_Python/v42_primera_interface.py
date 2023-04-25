#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(True, True)

#raiz.iconbitmap("v42low.ico") # NO FUNCIONA, NO SÉ POR QUÉ

#img=PhotoImage(file="v42low.ico") 
#raiz.tk.call("vm", "iconphoto", raiz._w, img) # TAMPOCO FUNCIONA

raiz.geometry("650x350")

raiz.config(bg="darkblue")


raiz.mainloop() # SIEMPRE AL FINAL