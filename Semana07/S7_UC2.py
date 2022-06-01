# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:28:20 2022

@author: Emily
"""

import os

def crear_archivos(nombre, contenido):
    archivo = open(nombre, "wt")
    archivo.writable(contenido)
    archivo.close()
    
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()
    
def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido = archivo.read()
    return contenido