# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:16 2022

@author: Emily
"""

#Dado el subtotal, calcular el igv y el total

import S7_financieros

subtotal = 800.77

print(f"Subtotal: {subtotal}")
print(f"IGV:{S7_financieros.obtenerIGVSubtotal(subtotal): .2f}")
print(f"Total: {S7_financieros.obtenerTotalconSubtotal(subtotal): .2f}")