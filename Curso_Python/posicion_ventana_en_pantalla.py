#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox # Para el cuadro de mensaje

root = Tk()

# ------------------------ posicion ventana -------------------------------

ancho_ventana = 900
alto_ventana = 350

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) +\
	"+" + str(y_ventana)
root.geometry(posicion)
root.config(bg="darkgrey", width="600", height="300", bd=5, relief="raised", cursor="pirate")
root.resizable(1,1)
root.title("Ventana centrada")