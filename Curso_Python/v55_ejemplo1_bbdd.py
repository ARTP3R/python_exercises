#!/usr/bin/python3

import sqlite3

mi_conexion=sqlite3.connect("v55_primera_base_de_datos.sqlite")

mi_cursor=mi_conexion.cursor()

mi_cursor=mi_conexion.cursor()

mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

mi_conexion.commit()

mi_conexion.close()