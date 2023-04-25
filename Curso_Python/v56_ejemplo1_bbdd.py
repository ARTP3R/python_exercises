#!/usr/bin/python3

import sqlite3

mi_conexion=sqlite3.connect("v56_primera_base_de_datos.sqlite")

mi_cursor=mi_conexion.cursor()

#mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

varios_productos=[
	("Camiseta", 10, "Deportes"),
	("Jarrón", 10, "Cerámica"),
	("Camión", 10, "Juguetería")
]
#mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", varios_productos)


mi_cursor.execute("SELECT * FROM PRODUCTOS")

leer_varios_productos=mi_cursor.fetchall()

for producto in leer_varios_productos:
	print("Nombre Artículo:", producto[0], "--- Precio:", producto[1], " --- Sección:", producto[2])





mi_conexion.commit()

mi_conexion.close()