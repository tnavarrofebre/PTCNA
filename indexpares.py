#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:15:08 2023

@author: Francisco Manuel Diaz Torres
"""

import numpy as np

grupo_items = []

for i in range(8908, 8965):
    for j in [10, 11, 13, 14, 15]:
        grupo="[ "+str(j)+"-"+str(i)+" ]"
        grupo_items.append([grupo, (j, i)])

with open("pares2.ndx", "w") as archivo:
    for nombre_grupo, tupla in grupo_items:
        archivo.write(nombre_grupo + "\n")
        archivo.write("   ".join(map(str, tupla)) + "\n")
