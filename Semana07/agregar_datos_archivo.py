# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:59:01 2022

@author: Emily
"""

archivo=open("noticia.txt","at" )
#\n es para agregar salto de línea
contenido="\nFuente:RPP"

archivo.write(contenido)
archivo.close()