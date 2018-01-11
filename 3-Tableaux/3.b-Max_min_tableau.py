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
# pip install numpy
# Ecrire une fonction permettant de trouver le maximum et le minimum d’un tableau.
import numpy as np

tab = [0,1,2,3,4,5,6,7,8,9,10]

def minimum():
    minimum = np.min(tab)
    print ("\nL'element le plus petit est %s") % (minimum)

def maximum():
    maximum = np.max(tab)
    print ("\nL'element le plus petit est %s") % (maximum)

minimum()
maximum()
