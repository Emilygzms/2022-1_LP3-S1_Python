# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:46:18 2022

@author: Emily
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ DELETE FROM EDITORIAL
                WHERE
                    IDEDITORIAL = 5
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
