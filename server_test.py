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
#   gestion de ticket
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

import socket # initialisation du serveur 

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

serveur.bind(('', 3000)) # Ecoute sur le port 3000 
serveur.listen() 

test=True
while test :  
    client, infosclient = serveur.accept()  
    request = client.recv(1024)
    print(request.decode("utf-8")) #affiche les données du client  
    print("IP client connecté: ", socket.gethostbyname(socket.gethostname()))  
    client.close() 

serveur.close()

