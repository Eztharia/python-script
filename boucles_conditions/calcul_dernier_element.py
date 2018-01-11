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

# Ecrire une fonction permettant de calculer le nième élément de la suite de fibonacci en utilisant une méthode récursive.

def calcul(x):
 if x==1 or x==2:
  return 1
 return calcul(x-1)+calcul(x-2)
print calcul(5)