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

# Ecrire un programme qui demande l’âge de l’utilisateur sur stdin et affiche son âge sur stdout

def age():
    age = input("Quel est ton âge ?? : ")
    age_reformat = "\nGénial tu a : %s ans !\n" % (age)
    print(age_reformat)
age()

