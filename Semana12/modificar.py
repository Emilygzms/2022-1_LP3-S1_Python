# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:46:39 2022

@author: Emily
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ UPDATE EDITORIAL
                SET
                    NOMBRE = 'Editorial Imprenta Unión'
                WHERE
                    IDEDITORIAL = 1
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
