#!/usr/bin/python3

from tkinter import *


raiz = Tk()

raiz.title("Práctica Label")

raiz.resizable(True, True)

raiz.geometry("650x350")

raiz.config(bg="grey", bd=10, relief="groove")

mi_frame=Frame(raiz, width=500, height=200)

#mi_frame.pack(side="right")
mi_frame.pack(fill="both", expand="True")

mi_frame.config(bg="darkgrey", width="600", height="300",\
	bd=10, relief="raised", cursor="pirate")


mi_imagen=PhotoImage(file="Imágenes/v44logo.gif")
Label(mi_frame, image=mi_imagen).place(x=50, y=50)

Label(mi_frame, text="HOLA MUNDO", fg="red", font=("Arial", 18)).place(x=150, y=50)

Label(mi_frame, text="Darme 1000€", fg="red", font=("Arial", 18)).place(x=150, y=100)



raiz.mainloop() # SIEMPRE AL FINAL
