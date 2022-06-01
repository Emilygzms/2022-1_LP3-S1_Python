# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:36:49 2022

@author: Emily
"""
#Importar libreria

import camelcase

#Caneda nombre y se muestra en formato titulo
nombre = "emily Gomez marcos"
print(nombre.upper())
print(nombre.title())

#Crear objeto llamado cam

cam= camelcase.CamelCase()
print("Con camelcase...")

#Imprimir el nombre en formato titulo
#Utilizar camelcase

print(cam.hump(nombre))

print("Resolviendo..")

#Resolviendo problema
#Crear objeto llamado cam2, se incluyen los argumentos 'emily' y 'marcos'

cam2=camelcase.CamelCase('emily', 'marcos')
print(cam2.hump(nombre))

"""
import camelcase

# Tenemos una cadena llamada nombre y se desea 
# que se muestre en formato título
nombre = "flor elizabeth Cerdán león"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam= camelcase.CamelCase()
print("Con camelcase....")

# Imprimimos el nombre en formato título
#Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto, incluimos los argumentos
# 'flor' y
"""