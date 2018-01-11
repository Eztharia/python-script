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

# Écrire une fonction permettant de calculer la somme des entiers positifs inférieurs à 1000 qui ne sont divisibles ni par 3 ni par 5.

entiers = 0
for i in range(1, 1000):
    if i%3 == 0 and i%5 == 0:
        entiers += i
print(entiers)