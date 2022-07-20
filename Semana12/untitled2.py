# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:29:06 2022

@author: Emily
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:59:11 2022

@author: Emily
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta_pais = """INSERT INTO 
                PAIS (NOMBRE, ESTADO)
                VALUES ('Colombia', 'A')
            """



cursor = conexion.cursor()
cursor.execute(consulta_pais)
conexion.commit()

conexion.close()
