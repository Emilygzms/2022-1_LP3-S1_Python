# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:29:53 2022

@author: Emily
"""

import os

#crear archivo, recibe como parametro el nombre del archivo
#y su contenido

def crea_archivo(nombre,contenido):
    archivo=open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()
    
#eliminar archivo, recibe el nombre del archivo a eliminar

def eliminar_archivo(nombre):
    os.remove(nombre)
    
#agregar contenido, debe existir el archivo
#se envia como parametro el nombre y el contenido
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

# Para leer un archivo, ya debe existir un archivo plano 
# Ejemplo: txt, py, java, ...
# Recibe como parámetro el nombre del archivo a leer
# y devuelve el contenido del archivo
def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido = archivo.read()
    return contenido
    
    