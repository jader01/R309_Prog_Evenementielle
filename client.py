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
#                        Gestion de la connexion
#
###########################################################################

#!/usr/bin/env python3
import socket
import os
from _thread import *
ClientSocket = None
host = '127.0.0.1'
port = 9090
myNumber = 0

def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    finally:
        print("connection au serveur réussi !")
        myNumber = int(ClientSocket.recv(1024))
        print("nombre de client reçu : ", myNumber)
    start_new_thread(threaded_server, (ClientSocket, myNumber))
    
    while True:
        msg = input('') # bloquant les retours => nécessite un thread
        ClientSocket.send(str.encode(msg))
        if msg == "quit": # Bogue sur le quit !
            ClientSocket.send(str.encode(str(myNumber)))
            break

def threaded_server(connection, num):
    while True:
        response = connection.recv(1024)
        print(response.decode('utf-8'))

if __name__== "__main__":
    main()