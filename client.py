############################################################################
#
#                            Import
#
###########################################################################

#import la librairie pour la création de la fenetre
from tkinter.simpledialog import askstring
from tkinter import *

#import de la librairie pour la gestion de socket
import socket


############################################################################
#
#                            Gestion de l'interface
#
###########################################################################

#import la librairie pour la création de la fenetre

fenetre = Tk() #ici on creer la fenetre

def show():
   search = askstring("Input", "Par quel type voulez vous faire une recherche ")
   print(search)

def printAll():
    print("insert le print du programme client")

def addArticle():
    print("insert de l'ajout des article")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Recherche", command=show)
menu1.add_command(label="Affichage", command=printAll)
menu1.add_command(label="Ajouter", command=addArticle)
menu1.add_separator()
menubar.add_cascade(label="Action a realiser", menu=menu1)

fenetre.config(menu=menubar)



boutonfermer = Button(fenetre, text="quitter", command=fenetre.quit)  # ici on creer le bouton avec le texte inter et a quoi il sert
boutonfermer.pack(side=BOTTOM)

fenetre.mainloop()
