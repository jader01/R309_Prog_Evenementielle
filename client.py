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


class Article:
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

    def printPubli(self):
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

 

class Book(Article):
    def __init__(self, author, title, year, journal, volume, number, pages, month, notes, publisher, series, address, edition):
        super().__init__(author, title, year, journal, volume, number, pages, month, notes)
        self.publisher = publisher
        self.series = series
        self.address = address
        self.edition = edition

        search_global.append(self)

        

    def printBook(self):
        self.printPubli()
        print(f"Éditeur : {self.publisher}")
        print(f"Série : {self.series}")
        print(f"Adresse : {self.address}")
        print(f"Édition : {self.edition}")
        print("\n")

        return(self.publisher, self.series, self.address, self.edition)





# Exemple d'utilisation
publications = [
Article("Jean Dupont", "Un Article Test", "2023", "Le Monde", 1, 1, "1-10", "Janvier", "ceci est une note"),
Article("Alice Martin", "Un Second Article", "2022", "Science Today", 2, 3, "15-20", "Février", "Autre note"),
Article("Stephen King", "Ca", "2004", "Horror", "1", "1", "1-200", "Otobre", "Livre d'horreur"),
Book("Jean Dupont", "Un Livre Test", "2023", "Le Monde", 1, 1, "1-10", "Janvier", "livre de jean ayant pour titre test", "michel lafon", "libre jeunesse", "Paris", "1ère Édition")
]


############################################################################
#
#                            Gestion de connexion 
#                           Serveur TCP Multi Thread
#                       repris du TD mais avec commentaire
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
    except socket.error as e:
        print(str(e))
    finally:
        print('En attente de connexion...')
        ServerSocket.listen(5)#                                                 Le serveur commence à écouter les connexions entrantes, avec une limite de 5 connexions en attente.
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
            for elm in publications: # on parcours tous les élément
                elm.printPubli() #ici on apelle la fonction print publication pour 
                mess["resultat"] = (elm.printPubli()) # si dans le message du client il y a une variable qui s'apl "resulata" on apl la fonction print ici
                connection.sendall(json.dumps(mess).encode('utf-8')) #et on envois au client en json


        if commande["fonction"] == "printBook":
            for elm in publications:
                if hasattr(elm, "printBook"):  # Vérifie si l'objet possède la méthode printBook
                    elm.printBook()
                    mess["resultat"] = elm.printBook()
                    connection.sendall(json.dumps(mess).encode('utf-8'))
        
        #Commande de recherche
        if commande["fonction"] == "search":
            critere = commande.get("critere")
            valeur = commande.get("valeur")
            results = Article.search(critere, valeur)
            mess["resultat"] = [elm.printPubli() for elm in results]
            connection.sendall(json.dumps(mess).encode('utf-8'))

        #Commande add :
        if commande["fonction"] == "addArt":
                newArticle =Article(commande["author"], commande["title"], commande["year"], commande["journal"], commande["volume"], commande["number"], commande["pages"], commande["month"], commande["notes"])
                mess["resultat"] = [elm.printPubli() for elm in newArticle]
                connection.sendall(json.dumps(mess).encode('utf-8'))
                
                    
        if data == "quit": # Bogue sur le quit !
            numclient = int(connection.recv(2048))
            clients[numclient].close()
            clients.pop(numclient)
            nbclients-=1

if __name__== "__main__":
    main()
