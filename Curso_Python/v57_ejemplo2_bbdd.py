#!/usr/bin/python3

import sqlite3

mi_conexion=sqlite3.connect("v57_gestion_productos.sqlite")

mi_cursor=mi_conexion.cursor()

#TRES COMILLAS PARA PODER SEPARAR LA LA INSTRUCCION SQL EN VARIAS LINEAS
mi_cursor.execute(''' 
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')



productos=[
	("Camiseta", 10, "Deportes"),
	("Jarrón", 50, "Cerámica"),
	("Camión", 20, "Juguetería"),
	("Jamón", 300, "Supermercado")
]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



mi_conexion.commit()

mi_conexion.close()