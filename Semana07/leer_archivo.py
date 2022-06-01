# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:32:33 2022

@author: Emily
"""

noticia = open("noticia.txt", "rt", encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)