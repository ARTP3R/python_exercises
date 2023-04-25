#!/usr/bin/python3

import sqlite3

mi_conexion=sqlite3.connect("v57_gestion_productos.sqlite")

mi_cursor=mi_conexion.cursor()






mi_cursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren', 15, 'Juguetería')")



mi_conexion.commit()

mi_conexion.close()