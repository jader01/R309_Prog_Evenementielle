############################################################################
#
#                            Import
#
###########################################################################

#import la librairie pour la création de la fenetre
from tkinter import *

#import de la librairie pour la gestion de socket
import socket


############################################################################
#
#                            Gestion de l'interface
#
###########################################################################


#On cree une fenetre avec différents parametres :
fenetre = Tk() #ici on creer la fenetre

#On cree une un bouton avec différentes parametres :
boutonfermer = Button(fenetre, text="quitter", command=fenetre.quit)  # ici on creer le bouton avec le texte inter et a quoi il sert
boutonfermer.pack(side=BOTTOM)

#On creer un LABEL cad un espaces précus pour écrire du texte : 
label=Label(fenetre, text="recherche")
label.pack(side=RIGHT)

value = StringVar()
value.set("insert de la requete")
entree = Entry(fenetre, width=30)
entree.pack()


#On lance la boucle principale:
fenetre.mainloop()


############################################################################
#
#                            Gestion de la connexion
#
###########################################################################

#!/usr/bin/env python3 
import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("localhost", 3000)) 

client.sendall(b"hello serveur\n") 

client.close()