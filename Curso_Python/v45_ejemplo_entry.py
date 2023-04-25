#!/usr/bin/python3

from tkinter import *


raiz = Tk()

mi_frame=Frame(raiz, width=1200, height=600)
mi_frame.pack()

label_nombre=Label(mi_frame, text="Nombre ")
label_nombre.grid(row=0, column=0, sticky="e", padx=10, pady=10)
cuadro_nombre=Entry(mi_frame)
cuadro_nombre.grid(row=0, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="right")

label_pass=Label(mi_frame, text="Contraseña ")
label_pass.grid(row=1, column=0, sticky="e", padx=10, pady=10)
cuadro_pass=Entry(mi_frame)
cuadro_pass.grid(row=1, column=1, padx=10, pady=10)
cuadro_pass.config(show="*")

label_apellido=Label(mi_frame, text="Apellido ")
label_apellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)
cuadro_apellido=Entry(mi_frame)
cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)

label_direccion=Label(mi_frame, text="Dirección ")
label_direccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)
cuadro_direccion=Entry(mi_frame)
cuadro_direccion.grid(row=3, column=1, padx=10, pady=10)


raiz.mainloop() # SIEMPRE AL FINAL
