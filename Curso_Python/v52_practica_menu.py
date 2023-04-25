#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox # Para el cuadro de mensaje

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

# ---------------------------- ventanas emergentes ---------------------------------

def info_adicional():
	messagebox.showinfo("Procesador de Arturo", "Ventana chula de mi pirula")

def aviso_licencia():
	messagebox.showwarning("Licencia", "Producto con licencia abierta GNU")

def Salir():
	var_salir=messagebox.askquestion("Salir", "¿Desea cerrar la aplicación?")
	if var_salir=="yes":
		raise SystemExit

def Salir2(): #otra forma de hacerlo
	var_salir=messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?")
	if var_salir==True:
		root.destroy()

def cerrar_documento():
	messagebox.showinfo("Cierre de documento", "El documento va a cerrarse")
	var_cerrar=True
	while var_cerrar==True:
		var_cerrar=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado.")
		

# ---------------------------- menu ---------------------------------


barra_menu=Menu(root)
root.config(menu=barra_menu)

menu_archivo=Menu(barra_menu, tearoff=0)
menu_edicion=Menu(barra_menu, tearoff=0)
menu_herramientas=Menu(barra_menu, tearoff=0)
menu_ayuda=Menu(barra_menu, tearoff=0)

menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()
menu_archivo.add_command(label="Cerrar", command=cerrar_documento)
menu_archivo.add_command(label="Salir", command=Salir)

menu_edicion.add_command(label="Copiar")
menu_edicion.add_command(label="Cortar")
menu_edicion.add_command(label="Pegar")

menu_ayuda.add_command(label="Licencia", command=aviso_licencia)
menu_ayuda.add_command(label="Acerca de...", command=info_adicional)



barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


root.mainloop()