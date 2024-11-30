############################################################################
#
#                           Import des librairie utiles
#
###########################################################################

#import de la librairie pour la gestion de socket
import socket

############################################################################
#
# Class pour stockage BDD
#
###########################################################################

class Article : #creation de la classe "mere"
    
    def __init__(self, autheur, titre, annee, journal, vol, nombre, page, mois, notes): #on initalise la class avec ces attribus de base
        #print('lancement initialisation'
        self.author = autheur
        self.title = titre
        self.journal = journal
        self.year = annee
        self.volume = vol
        self.number = nombre
        self.pages = page
        self.month = mois
        self.notes = notes
        

    def printPubli(self): # affichage de la publication
        if self.author is not None :
            print(self.author)
            print(self.title)
            print(self.journal)
            print(self.year)
            print(self.volume)
            print(self.number)
            print(self.pages)
            print(self.month)
            print(self.notes)
    
    def Addpubli(self, autheurchoisi, titrechoisi, anneechoisi):
        self.author.append(autheurchoisi)
        self.title.append(titrechoisi)
        self.year.append(anneechoisi)
        

class Book(Article) :
    
    def __init__(self, publi, serie, adress, editeur):
        self.publisher = publi
        self.series = serie
        self.address = adress
        self.edition = editeur

    def printBook(self):
        if self.ref is not None :
            print(self.ref)

class Improceeding(Book) :
    
    def __init__(self, titredulivre, editeur, orga):
        self.booktitle = titredulivre
        self.editor = editeur
        self.organization = orga

class phdthesis(Improceeding):

    def __init__(self, ecole, type) :
        self.school = ecole
        self.type = type


###############################################################
#
#   gestion 
#
################################################################

publi1 = Article("jean", "test", 2004, "le figaro", 12, 2, "12 - 15", "mars", "test de revue1")
publi1.printPubli()

#publi2 = Article()
#publi2.Addpubli("3", "eichiro oda", "one piece", 2003)
#publi2.printPubli()


############################################################################
#
#                            Gestion de connexion
#
###########################################################################


#!/usr/bin/env python3
# Serveur TCP Multi Thread
import socket
import os
from _thread import *
ServerSocket = None
host = '127.0.0.1'
port = 9090
clients = []
nbclients = 0
numclient = None

def main():
    global nbclients
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    finally:
        print('En attente de connexion...')
        ServerSocket.listen(5)
    while True:
        client, address = ServerSocket.accept()
        print('Connecter à : ' + address[0] + ':' + str(address[1]))
        client.send(str.encode(str(nbclients)))
        clients.append(client)
        print("Liste des clients : ", clients)
        start_new_thread(threaded_client, (client, ))
        nbclients+=1
        print('Nombre de thread : ' + str(nbclients))
    
def threaded_client(connection):
    global nbclients
    print("connection", connection)
    while True:
        data = connection.recv(2048)
        reply = '\n>>' + data.decode('utf-8') + '\n'
        for client in clients:
            client.sendall(str.encode(reply))
        if data == "quit": # Bogue sur le quit !
            numclient = int(connection.recv(2048))
            clients[numclient].close()
            clients.pop(numclient)
            nbclients-=1

if __name__== "__main__":
    main()

