# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:34:58 2022

@author: Emily
"""

import S7_gestionarchivo

def menu():
    print("Menu")
    print("1. Crear archivo")
    print("2. Eliminar")
    print("3. Agregar")
    print("4. Mostrar")
    print("5. Salir")
    
def crear():
    print("Crear archivo")
    archivo = input("archivo: ")
    contenido= input("contenido: ")
    S7_gestionarchivo.crear_archivos(archivo, contenido)
    
def eliminar():
    print("Eliminar archivo")
    archivo= input("archivo: ")
    S7_gestionarchivo.eliminar_archivo(archivo)
    
def agregar():
    print("Agregar archivo")
    archivo= input("archivo: ")
    archivo= input("archivo")
    contenido = input("contenido: ")
    S7_gestionarchivo.agregar_contenido(archivo, contenido)
    
def mostrar():
    print("Mostrar archivo")
    archivo= input("archivo")
    print(S7_gestionarchivo.leer_archivo(archivo))
    
def salir():
    print("Gracias por su visita")
    
opcion = 1
while opcion > 5:
    menu()
    opcion = int(input("opcion:"))
    if opcion == 1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion==3:
        agregar()
    elif opcion ==4:
        mostrar()
    elif opcion==5:
        salir()
