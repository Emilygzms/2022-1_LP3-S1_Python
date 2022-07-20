# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:35:55 2022

@author: Emily
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ SELECT * 
                FROM LIBRO
                WHERE
                    precio >= 55
                ORDER BY titulo
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()

for libro in libros:
    print(libro)
conexion.close()
