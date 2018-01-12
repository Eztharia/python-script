#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :menu.py
# description     :TP 1 - Python
# author          :dominique.tauzin@ynov.com
# date            :11/01/2018
# version         :0.1
# usage           :python TP1.py
# python_version  :2.7.14
#=======================================================================

# Ecrire un programme pour créer des mots de passealéatoires avec le plus de modularité possible.

import datetime
import random
import string


def LongueurPassword():
    """ Verification de l'entrée utilisateur """
    userInput = 0
    while True:
        try:
            userInput = int(input("Longeur du mot de passe (8-24) : "))
        except ValueError:
            print("Erreur : Vous n'avez pas entré un nombre entier !")
            print("-------------------------------------------------")
        else:
            if userInput >= 2 and userInput <= 20:
                return userInput
            else:
                print("Erreur : Longeur incorrecte veuillez choisir entre 8 et 24 !")
                print("------------------------------------------------------------")


def generate_password(size, chars=string.digits + string.punctuation + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


longeur_mot_de_passe = LongueurPassword()
mot_de_passe = generate_password(longeur_mot_de_passe)
print ("Votre mot de passe : " + mot_de_passe)
print("-----------------------------------")
