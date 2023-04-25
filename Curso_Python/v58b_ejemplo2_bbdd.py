#!/usr/bin/python3

import sqlite3

mi_conexion=sqlite3.connect("v58_gestion_productos.sqlite")

mi_cursor=mi_conexion.cursor()






mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Cerámica'")

productos=mi_cursor.fetchall()
print(productos)


mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO=25 WHERE NOMBRE_ARTICULO='Camión'")

mi_cursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Jarrones'")

mi_conexion.commit()

mi_conexion.close()