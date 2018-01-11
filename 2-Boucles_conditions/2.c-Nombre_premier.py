#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :TP 1 - Python
#author          :dominique.tauzin@ynov.com
#date            :11/01/2018
#version         :0.1
#usage           :python TP1.py
#python_version  :2.7.14
#=======================================================================

# Ecrire une fonction vérifiant si n est un nombre premier ou non.
from math import *

x=int(input("C'est quoi ton nombre ? : "))
y=0
for i in range (2,int(sqrt(x))):
    if x%i == 0:
        y = 1
if y == 0:
    print ("\n%s est un nombre premier") % (x)
else:
    print ("\n%s n'est pas un nombre premier") % (x)