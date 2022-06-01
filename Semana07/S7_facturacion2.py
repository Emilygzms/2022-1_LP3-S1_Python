# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:52:34 2022

@author: Emily
"""

#Dado el total, calcular el IGV y el subtotal

import S7_financieros

total = 1000.49

print(f"Subtotal: {S7_financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {S7_financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}") 

