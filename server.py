############################################################################
#
#                        Import lib souhaiter
#
###########################################################################

import socket #         permet de gerer les connexion réseau
from _thread import * # permet la gestion des thread
import json #           pour la gestion des datas en json

############################################################################
#
#      creation d'une variable pour les résultat des recherches
#
###########################################################################

search_global = []  

############################################################################
#
# Class pour stockage données
#
###########################################################################


class Article: #on definie la class article
    def __init__(self, author, title, year, journal, volume, number, pages, month, notes):
        self.author = author
        self.title = title
        self.year = year
        self.journal = journal
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.notes = notes

       
        search_global.append(self)

    def printPubli(self): #fonction affichage de l'article
        print(f"Auteur : {self.author}")
        print(f"Titre : {self.title}")
        print(f"Journal : {self.journal}")
        print(f"Année : {self.year}")
        print(f"Volume : {self.volume}")
        print(f"Numéro : {self.number}")
        print(f"Pages : {self.pages}")
        print(f"Mois : {self.month}")
        print(f"Notes : {self.notes}")
        print("\n")
        
        return (self.author, self.title, self.year, self.journal, self.volume, self.number, self.pages, self.month, self.notes)
    
        # Recherche globale
    def search(critere, valeur):
        resultats = []  #les objets qui répondent aux critères de recherche
        for elm in search_global: # parcourt chaque élément (elm) de la liste search_global qui contient toutes éléments d'objets des classes
            if hasattr(elm, critere) and getattr(elm, critere) == valeur:
                resultats.append(elm)
        return resultats

 

class Book(Article): #maintenant une class book qui hérite des article


    def __init__(self, author, title, year, journal, volume, number, pages, month, notes, publisher, series, address, edition):
        super().__init__(author, title, year, journal, volume, number, pages, month, notes)
        self.publisher = publisher
        self.series = series
        self.address = address
        self.edition = edition

        search_global.append(self)

        

    def printBook(self): #fonction affichage des livres
        self.printPubli() #associe a la fonction print publi plus haut
        print(f"Éditeur : {self.publisher}")
        print(f"Série : {self.series}")
        print(f"Adresse : {self.address}")
        print(f"Édition : {self.edition}")
        print("\n")

        return(self.publisher, self.series, self.address, self.edition)





# Ajout de certains Article et Livre pour les tests
publications = [
Article("Jean Dupont", "Un Article Test", "2023", "Le journal", '1', '1', "1-10", "Janvier", "ceci est une note"),
Article("Dana", "Ferronerie et compagnie", "2022", "Le fere", "2", "3", "15-20", "aout", "un article qui vous surprendra"),
Article("Lisandru", "Le cinema", "2022", "Ciné and co", "2", "3", "15-20", "Avril", "article parlan de cinema"),
Book("Stephen King", "Ca", "2004", "Horror", "1", "1", "1-200", "Otobre", "Livre d'horreur", "Horror publisher", "ça 1", "england", "edit"),
Book("Eichiro Oda", "One piece", "1997", "Shonen Jump", "1", "1", "1-100", "Mars", "Manga", "Shonen", "anime", "place", "kona" ),
Book("Moon", "The starts", "2006", "test", "1", "1", "1-100", "octobre", "eng book", "book", "test", "test", "test" )
]


############################################################################
#
#                            Gestion de connexion 
#                           Serveur TCP Multi Thread
#               repris du TD mais légèrement modifiera + commentaire
#
###########################################################################


ServerSocket = None #   initialisation de la variable socket (du serveur)
host = '127.0.0.1' #    initialisation de l'ip du server (ici 127.0.0.1 cad Local host)
port = 9090 #           le port sur le quel le serveur ecoute les connexions
clients = [] #          liste permetant de stoquer les connexions des client
nbclients = 0 #         compteur du nbr de client
numclient = None

####
def main():
    global nbclients
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #          creation d'un socket TCP
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#         Permet de réutiliser l'adresse et le port immédiatement après une fermeture du socket
    try:
        ServerSocket.bind((host, port))#                                        Lier l'adresse IP et le port au socket
    except socket.error as e: #                                                 Pour la gestion des erreurs
        print(str(e))
    finally:
        print('En attente de connexion...')
        ServerSocket.listen()#                                                 Le serveur commence à écouter les connexions entrantes, avec une limite de 5 connexions en attente.
    # Attente de connexion + creation des threads :
    while True:
        client, address = ServerSocket.accept() #                               Le serveur attend une connexion entrante, puis l'accepte
        print('Connecter à : ' + address[0] + ':' + str(address[1]))
        client.send(str.encode(str(nbclients)))#                                Envoie le nombre de clients connectés à ce client
        clients.append(client)#                                                 Ajoute la connexion client à la liste des clients.
        print("Liste des clients : ", clients)# Lance un thread pour gérer ce client spécifiquement en appelant la fonction threaded_client (ci dessous)
        start_new_thread(threaded_client, (client, ))
        nbclients+=1
        print('Nombre de thread : ' + str(nbclients))


#Gestion des clients :
def threaded_client(connection):
    global nbclients
    print("connection", connection)
    while True: #pour l'attente de connection
        data = connection.recv(2048) #on associe les données que l'on va recevoir suite a la connnextion a la variable data
        commande = json.loads(data.decode()) #on encode les data en json
        
        mess = {} #dictionnaire qui sera ensuite encoder en json pour le transfert
        
        #Fonction affichage bibli
        if commande["fonction"] == "bibli": #ici quand le serveur va détecter que le client lui aura pour clef associé a 'fonction' -> "bibli" il excutera la suite
            allpubli = []
            for elm in publications: # on parcours tous les élément
                allpubli.append(elm.printPubli()) #ici on apelle la fonction print publication pour 
            mess["resultat"] = allpubli # si dans le message du client il y a une variable qui s'apl "resulata" on apl la fonction print ici
            connection.sendall(json.dumps(mess).encode('utf-8')) #et on envois au client en json


        if commande["fonction"] == "printBook":
            allBook = []
            for elm in publications:
                if hasattr(elm, "printBook"):  # Vérifie si l'objet possède la méthode printBook
                    allBook.append(elm.printBook())
            mess["resultat"] = elm.printBook()
            connection.sendall(json.dumps(mess).encode('utf-8'))
        
        #Commande de recherche
        if commande["fonction"] == "search":
            critere = commande["critere"] #on associe au critère l'entrée du client
            valeur = commande["valeur"]#pareil que ligne du dessus
            results = Article.search(critere, valeur)# maintneant on fait une recherche avec la fonction search de la class article
            mess["resultat"] = [elm.printPubli() for elm in results] #on associe le resultat a une variable
            connection.sendall(json.dumps(mess).encode('utf-8')) #on renvoie le resultat en json

        #Commande add :
        if commande["fonction"] == "addArt": #ajout d'un article
            author = commande.get("author") #on récupère l'entrée du client et on l'associe a une variable
            title = commande.get("title") #pareil que au dessus
            year = commande.get("year")
            journal = commande.get("journal")
            volume = commande.get("volume")
            number = commande.get("number")
            pages = commande.get("pages")
            month = commande.get("month")
            notes = commande.get("notes")

            if all([author, title, year, journal, volume, number, pages, month, notes]): #ici on verrifie que l'on as bien tous les élément avant de passer a la suite
                newArticle = Article(author, title, year, journal, volume, number, pages, month, notes)#on les ajoute a la table article
                publications.append(newArticle)#et a la liste des publications
                mess["resultat"] = newArticle.printPubli() #puis on associe tous ça au résultat pour l'afficher
                connection.sendall(json.dumps(mess).encode('utf-8')) # et on l'envoie
            else:
                mess["error"] = "Il manque des donnée" #sinon on renvoie une ereur (debugage)
                connection.sendall(json.dumps(mess).encode('utf-8'))      
                    
        if commande["fonction"] == "quit": #fermeture de connexion
            connection.close() #on ferme la co
            clients.remove(connection)
            nbclients -= 1 #on décrémente le nombre de lient
            print('Client déconnecté. Nombre de clients restants : ' + str(nbclients))
            break

if __name__== "__main__":
    main()
