# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:18:45 2022

@author: Emily
"""

consulta_editorial = """INSERT INTO 
                EDITORIAL(NOMBRE, ESTADO) 
                VALUES ('EIU', 'A'),
                VALUES ('Macro', 'A'),
                VALUES ('Bosch', 'A'),
                VALUES ('Lima Sur', 'A'),
                VALUES ('Pirámide', 'A'),
                VALUES ('Colombus', 'A'),
                VALUES ('Centro', 'A')
            """

consulta_autor = """INSERT INTO 
                AUTOR(NOMBRE, F_NACIMIENTO) 
                VALUES ('Flor Cerdán', '25/10/1978'),                  
                VALUES ('Daniel Levano', '17/01/1980'),
                VALUES ('Omar Peña', '15/10/1978'),
                VALUES ('Cesar Zapata', '15/10/1960')

            """
consulta_libro = """INSERT INTO 
                LIBRO(TITULO, CANTIDAD, ANIO, PRECIO, ESTADO, IDAUTOR, IDEDITORIAL, IDPAIS) 
                VALUES ('Oracle 11g', 10, 2019, 50, 'A', 1, 1, 1),                  
                VALUES ('Sistemas Operativos', 14, 2016, 59, 'A', 1, 4, 3),
                VALUES ('Estructuras de Datos', 6, 2018, 20, 'A', 2, 2, 3),
                VALUES ('Algoritmos con Python', 8, 2017, 70, 'A', 2, 2, 1),
                VALUES ('BI', 6, 1998, 50, 'A', 1, 4, 2),
                VALUES ('Ing. de Software', 9, 2000, 56, 'A', 3, 2, 4),
                VALUES ('Organización de PC', 9, 2016, 60, 'A', 7, 2, 1),
                VALUES ('Ensamblaje', 9, 2018, 50, 'A', 4, 4, 3)

            """