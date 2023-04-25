#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox # Para el cuadro de mensaje
#from tkinter import filedialog # Para el explorador de ficheros
import sqlite3 # Para la base de datos

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
root.title("Práctica guiada")


# ---------------------------- ventanas emergentes ---------------------------------

	
def googlealo():
	import webbrowser
	webbrowser.open("https://www.google.es/search?q=ayuda", new=2, autoraise=True)

def info_adicional():
	messagebox.showinfo("Procesador de Arturo", "Ventana chula de mi pirula")

def aviso_licencia():
	messagebox.showwarning("Licencia", "Producto con licencia abierta GNU")

def no_disponible():
	messagebox.showerror("No disponible", "Pendiente de programar")

def error_excepcion(titulo, texto):
	messagebox.showerror(titulo, texto)

def Salir():
	var_salir=messagebox.askquestion("Salir", "¿Desea cerrar la aplicación?")
	if var_salir=="yes":
		raise SystemExit

def Salir2(): #otra forma de hacerlo
	var_salir=messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?")
	if var_salir==True:
		root.destroy()



# ---------------------------- opciones BBDD ---------------------------------



def conectar_bd():
	global mi_conexion_bd1
	global mi_cursor_bd1
	mi_conexion_bd1=sqlite3.connect("v59_practica_guiada.sqlite")
	mi_cursor_bd1=mi_conexion_bd1.cursor()
	messagebox.showinfo("Éxito", "Base de datos conectada.")

def desconectar_bd():
	try:
		mi_conexion_bd1.close()
		messagebox.showinfo("Éxito", "Base de datos desconectada.")
	except NameError:
		error_excepcion("Error", "No hay base de datos conectada.")

def crear_tabla():
	try:
		mi_cursor_bd1.execute(''' 
			CREATE TABLE USUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50) UNIQUE,
			PASSWORD VARCHAR(20),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(100),
			COMENTARIOS VARCHAR(100))
		''')
		messagebox.showinfo("Éxito", "Tabla creada.")
	except Exception:
		error_excepcion("Error", "Error desconocido. La tabla ya existe o no hay base de datos conectada.")
	
def cadena_aleatoria(longitud_cadena):
	import string
	import random
	string_random=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud_cadena))
	return string_random

def intro_reg_aleatorio():
	str_nombre=cadena_aleatoria(12)
	str_passwd=cadena_aleatoria(8)
	str_apellido=cadena_aleatoria(12)
	str_direccion=cadena_aleatoria(30)
	str_comentario=cadena_aleatoria(50)

	lista_usuarios=[str_nombre, str_passwd, str_apellido, str_direccion, str_comentario]
	
	mi_cursor_bd1.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)", lista_usuarios)	
	mi_conexion_bd1.commit()
	messagebox.showinfo("Éxito", "Se ha creado un registro de usuario con el nombre "+str_nombre)
	
def borrar_formulario():
	cuadro_ID.delete(0, "end")
	cuadro_nombre.delete(0, "end")
	cuadro_pass.delete(0, "end")
	cuadro_apellido.delete(0, "end")
	cuadro_direccion.delete(0, "end")
	cuadro_comentarios.delete("1.0", "end")


# ---------------------------- opciones CRUD ---------------------------------


def crear_registro():
	try:
		str_nombre=cuadro_nombre.get()
		str_passwd=cuadro_pass.get()
		str_apellido=cuadro_apellido.get()
		str_direccion=cuadro_direccion.get()
		str_comentario=cuadro_comentarios.get("1.0", "end")

		lista_campos=[
			str_nombre,
			str_passwd,
			str_apellido,
			str_direccion,
			str_comentario
		]

		mi_cursor_bd1.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)", lista_campos)	
		mi_conexion_bd1.commit()
		messagebox.showinfo("Éxito", "Se ha creado un registro de usuario con el nombre "+str_nombre)
	except Exception:
		error_excepcion("Error", "Base de datos no conectada.")	

def leer_registro():
	
	id_usuario_buscado=cuadro_ID.get()
	mi_cursor_bd1.execute("SELECT * FROM USUARIOS WHERE ID = " + id_usuario_buscado)
	
	usuario_encontrado=mi_cursor_bd1.fetchone()
		
	print(id_usuario_buscado)
	print(usuario_encontrado)
	
	borrar_formulario()
	cuadro_ID.insert(0, usuario_encontrado[0])
	cuadro_nombre.insert(0, usuario_encontrado[1])
	cuadro_pass.insert(0, usuario_encontrado[2])
	cuadro_apellido.insert(0, usuario_encontrado[3])
	cuadro_direccion.insert(0, usuario_encontrado[4])
	cuadro_comentarios.insert("1.0", usuario_encontrado[5])

	mi_conexion_bd1.commit()

	messagebox.showinfo("Éxito", "Registro cargado en formulario.")

def actualizar_registro(): # FORMA MÁS SIMPLE Y ELEGANTE

	id_usuario_buscado=cuadro_ID.get()

	str_nombre=cuadro_nombre.get()
	str_passwd=cuadro_pass.get()
	str_apellido=cuadro_apellido.get()
	str_direccion=cuadro_direccion.get()
	str_comentario=cuadro_comentarios.get("1.0", "end")

	lista_campos=[
		str_nombre,
		str_passwd,
		str_apellido,
		str_direccion,
		str_comentario,
		id_usuario_buscado
	]

	mi_cursor_bd1.execute("UPDATE USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", lista_campos)


def actualizar_registro_b(): # OTRA FORMA DE HACER LA CONSULTA, AUNQUE MÁS LABORIOSA

	id_usuario_buscado=cuadro_ID.get()
	str_nombre=cuadro_nombre.get()
	str_passwd=cuadro_pass.get()
	str_apellido=cuadro_apellido.get()
	str_direccion=cuadro_direccion.get()
	str_comentario=cuadro_comentarios.get("1.0", "end")


	mi_cursor_bd1.execute("UPDATE USUARIOS SET \
		NOMBRE='"+str_nombre+"' , \
		PASSWORD='"+str_passwd+"', \
		APELLIDO='"+str_apellido+"', \
		DIRECCION='"+str_direccion+"', \
		COMENTARIOS='"+str_comentario+"' \
		WHERE ID= '"+id_usuario_buscado+"';")
	
	mi_conexion_bd1.commit()
	messagebox.showinfo("Éxito", "Registro actualizado.")


	

def borrar_registro():
	try:
		mi_cursor_bd1.execute("DELETE FROM USUARIOS WHERE ID="+cuadro_ID.get())
		mi_conexion_bd1.commit()
		messagebox.showinfo("Éxito", "Registro borrado.")
		borrar_formulario()
	except Exception:
		error_excepcion("Error", "No se puede borrar. Compruebe si la base de datos está conectada y el registro existe.")	

# ---------------------------- menu ---------------------------------

barra_menu=Menu(root)
root.config(menu=barra_menu)
# ----- menú principal  -----
menu_archivo=Menu(barra_menu, tearoff=0)
menu_edicion=Menu(barra_menu, tearoff=0)
menu_bbdd=Menu(barra_menu, tearoff=0)
menu_crud=Menu(barra_menu, tearoff=0)
menu_herramientas=Menu(barra_menu, tearoff=0)
menu_ayuda=Menu(barra_menu, tearoff=0)
# ----- submenús  -----
menu_archivo.add_command(label="Nuevo", command=no_disponible)
menu_archivo.add_command(label="Abrir", command=no_disponible)
menu_archivo.add_command(label="Guardar", command=no_disponible)
menu_archivo.add_command(label="Guardar como", command=no_disponible)
menu_archivo.add_separator()
menu_archivo.add_command(label="Cerrar", command=no_disponible)
menu_archivo.add_command(label="Salir", command=Salir)

menu_edicion.add_command(label="Borrar formulario", command=borrar_formulario)
menu_edicion.add_separator()
menu_edicion.add_command(label="Copiar", command=no_disponible)
menu_edicion.add_command(label="Cortar", command=no_disponible)
menu_edicion.add_command(label="Pegar", command=no_disponible)

menu_bbdd.add_command(label="Conectar Base de Datos", command=conectar_bd)
menu_bbdd.add_command(label="Desconectar Base de Datos", command=desconectar_bd)
menu_bbdd.add_command(label="Crear Tabla", command=crear_tabla)
menu_bbdd.add_command(label="Introducir registro aleatorio", command=intro_reg_aleatorio)

menu_crud.add_command(label="Create", command=crear_registro)
menu_crud.add_command(label="Read", command=leer_registro)
menu_crud.add_command(label="Update", command=actualizar_registro)
menu_crud.add_command(label="Delete", command=borrar_registro)

menu_herramientas.add_command(label="Taladro", command=no_disponible)
menu_herramientas.add_separator()
menu_herramientas.add_command(label="Destornillador", command=no_disponible)

menu_ayuda.add_command(label="Ayuda", command=googlealo)
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Licencia", command=aviso_licencia)
menu_ayuda.add_command(label="Acerca de...", command=info_adicional)

# ----- agregar a la barra de menú  -----
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
barra_menu.add_cascade(label="Base de Datos", menu=menu_bbdd)
barra_menu.add_cascade(label="CRUD", menu=menu_crud)
barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


# ------------------------ formulario  -------------------------------

mi_frame=Frame(root, width=1200, height=600)
mi_frame.config(bg="grey", width="600", height="300",bd=5, relief="raised", cursor="pirate")
mi_frame.pack()

label_ID=Label(mi_frame, text="ID ")
label_ID.grid(row=0, column=0, sticky="e", padx=5, pady=5)
cuadro_ID=Entry(mi_frame, width=20)
cuadro_ID.grid(row=0, column=1, columnspan=1, padx=5, pady=5, sticky="W")
cuadro_ID.config(fg="red", justify="center")

label_nombre=Label(mi_frame, text="Nombre ")
label_nombre.grid(row=1, column=0, sticky="e", padx=5, pady=5)
cuadro_nombre=Entry(mi_frame, width=80)
cuadro_nombre.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

label_pass=Label(mi_frame, text="Contraseña ")
label_pass.grid(row=2, column=0, sticky="e", padx=5, pady=5)
cuadro_pass=Entry(mi_frame, width=80)
cuadro_pass.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
cuadro_pass.config(show="*")

label_apellido=Label(mi_frame, text="Apellido ")
label_apellido.grid(row=3, column=0, sticky="e", padx=5, pady=5)
cuadro_apellido=Entry(mi_frame, width=80)
cuadro_apellido.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

label_direccion=Label(mi_frame, text="Dirección ")
label_direccion.grid(row=4, column=0, sticky="e", padx=5, pady=5)
cuadro_direccion=Entry(mi_frame, width=80)
cuadro_direccion.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

label_comentarios=Label(mi_frame, text="Comentarios ")
label_comentarios.grid(row=5, column=0, sticky="e", padx=5, pady=5)
cuadro_comentarios=Text(mi_frame, width=80, height=5)
cuadro_comentarios.grid(row=5, column=1, columnspan=3, padx=5, pady=5)#, ipady=10)
scroll_comentarios=Scrollbar(mi_frame, command=cuadro_comentarios.yview)
scroll_comentarios.grid(row=5, column=5, sticky="nsew", padx=5, pady=5)
cuadro_comentarios.config(yscrollcommand=scroll_comentarios.set)


# ---------------------------- botones ---------------------------------

frame_botones=Frame(root, width=1200, height=600)
frame_botones.config(bg="grey", width="600", height="300",\
	bd=5, relief="raised", cursor="heart")
frame_botones.pack()


boton_crear=Button(frame_botones, text="Crear", command=crear_registro)
boton_crear.grid(row=0, column=0, sticky="e", padx=5, pady=5)

boton_leer=Button(frame_botones, text="Leer", command=leer_registro)
boton_leer.grid(row=0, column=1, sticky="e", padx=5, pady=5)

boton_actualizar=Button(frame_botones, text="Actualizar", command=actualizar_registro)
boton_actualizar.grid(row=0, column=2, sticky="e", padx=5, pady=5)

boton_borrar=Button(frame_botones, text="Borrar", command=borrar_registro)
boton_borrar.grid(row=0, column=3, sticky="e", padx=5, pady=5)



# ---------------------------- YYY FIN ---------------------------------

root.mainloop()