# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:38:21 2022

@author: Emily
"""

"""
Los módulos permiten crear librerias de funcionalidades que se
puedan utilizar o reutilizar en cualquier momento :D
"""

igv = 0.18

def obtenerIGVSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    #Subtotal + igv*subtotal
    #Subtotal*(1+0.8)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
