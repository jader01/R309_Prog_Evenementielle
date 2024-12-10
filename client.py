
############################################################################
#
#                        Import lib souhaiter
#
###########################################################################

#import la librairie pour la création de la fenetre
from tkinter.simpledialog import askstring
from tkinter import *

#import de la librairie pour la gestion de socket
import socket

#Import des librairie souhaiter
import socket #         permet de gerer les connexion réseau
from _thread import * # permet la gestion des thread
import json #           pour la gestion des datas en json


############################################################################
#
#                        Gestion de la connexion
#
###########################################################################

#Déclaration des varibale que nous allons utiliser plus bas dans notre server :
ClientSocket = None #   initialisation de la variable socket (du serveur)
host = '127.0.0.1' #    initialisation de l'ip du server (ici 127.0.0.1 cad Local host)
port = 9090 #           le port sur le quel le client se connecte au serveur
myNumber = 0 #          identifie le client lors de la déconnexion.


def main():
    global ClientSocket
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#          creation d'un socket TCP
    ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#        Permet de réutiliser l'adresse et le port immédiatement après une fermeture du socket
    try:
        ClientSocket.connect((host, port))#                                    connexion serv en utilisant le socket créé si dessus
    except socket.error as e:
        print(str(e))
    finally:
        print("connection au serveur réussi !")
        myNumber = int(ClientSocket.recv(1024))
        print("nombre de client reçu : ", myNumber)
    
    # Créer la fenêtre
    window = MyWindow(ClientSocket) #pour la fentre client

    # Démarrer le thread serveur en passant la zone de texte de la fenêtre
    start_new_thread(threaded_server, (ClientSocket, myNumber, window.text_zone))

    # Lancer la boucle principale de la fenêtre
    window.mainloop()


def threaded_server(connection, num, text_zone):
    while True:
        try:
            response = connection.recv(1024) #connexion au serv
            decode_rep = json.loads(response.decode('utf-8')) #on decode le json pour le re mettre sous forme de dico
            messages = decode_rep["resultat"] #on associe a la variable message ce que l'on viens de décoder ci dessus

            # Utiliser after pour mettre à jour la zone de texte dans le thread principal
            text_zone.after(0, lambda: text_zone.delete('1.0', END)) # Effacer le texte existant
            for message in messages :
                text_zone.after(0, lambda: text_zone.insert(END, f"{message}\n"))
            text_zone.after(0, lambda : text_zone.see(END))
            
        except Exception as e:
            print(f"Erreur dans le thread serveur : {e}")
            break


############################################################################
#
#                       Partie int tkinter
#
###########################################################################


class MyWindow(Tk): #classe pour l'interface graphique
    def __init__(self, client_socket):
        Tk.__init__(self)
        self.client_socket = client_socket

        self.geometry("500x400")
        self.title("R309 Prog even")

        #label_t = Label(self, text="Bibliothèque:\n")
        #label_t.pack()

        button_bibli = Button(self, text="Afficher article", command=self.printBibli) #bouton affichage des article
        button_bibli.pack()

        button_livre = Button(self, text="Afficher livre", command=self.printLivre) #bouton affichage des livre
        button_livre.pack()

        button_add = Button(self, text="Recherche", command=self.recherche) #bouton recherche
        button_add.pack()

        button_json = Button(self, text="Exporter en JSON", command=self.jsonexport) #bouton recherche
        button_json.pack()

        menubar = Menu(self) #bare de menu

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Ajouter Article", command=self.addArt) #onglet de l'ajout d'un article

        menubar.add_cascade(label="Ajouter", menu=menu1)#le nom du menu
        self.config(menu=menubar)



        boutonfermer = Button(self, text="quitter", command=self.quitclient)  # bouton fermeture de co
        boutonfermer.pack(side=BOTTOM)


        # Ajouter la zone de texte comme un attribut de l'objet
        self.text_zone = Text(self, height=10, width=50) #zone de texte
        self.text_zone.pack()


############################################################################
#
#             Fonction déclencher par l'int graphique
#
###########################################################################

    def printBibli(self):
        message = {}
        message["fonction"] = "bibli" #fonction affichage des article
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))


    def printLivre(self):
        message = {"fonction": "printBook"} #de meme pour affichage des livre
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))


    
    def recherche(self): #fonction qui apl la fonction de recherche sur le serveur
        critere = askstring("Input", "Critère de recherche (author, title, year, ...):") #ici on demande le critère de la recher
        search = askstring("Input", "Que voulez vous rechercher ?") #ici on demande la valeur a rechercher
        message = { #ont met tous ça dans un dico pour l'envoyer en json
            "fonction": "search", 
            "critere": critere, 
            "valeur": search 
            }
       
        message = json.dumps(message) #on met en json
        self.client_socket.sendall(str.encode(message)) #on envoie au serveur
    
    def addArt(self):#fonction qui apl l'ajout d'article sur le serveur
        #demande de toutes les valeur pour créée un artcicle
        auteur= askstring("Input", "Ajouter le nom de l'auteur") 
        titre = askstring("Input", "Ajouter le titre")
        year = askstring("Input", "Ajouter l'anéee")
        journal = askstring("Input", "Ajouteur le nom du journal dans le quel est publier l'article")
        volume= askstring("Input", "Ajouter le nom du volume")
        number= askstring("Input", "Ajouter le nom du volume")
        pages = askstring("Input", "Ajouter le nombre de page")
        mois= askstring("Input", "Ajouter le mois")
        note= askstring("Input", "Ajouter une note")
        message = { #on met tous dans un dico pour envoyer en json après
            "fonction": "addArt",
            "author": auteur,
            "title": titre, 
            "year": year,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": mois,
            "notes": note
        }
        message = json.dumps(message) 
        self.client_socket.sendall(str.encode(message))

    def addBook(self): #pareil que la fonction d'avant mais pour les livres
        auteur = askstring("Input", "Ajouter le nom de l'auteur")
        titre = askstring("Input", "Ajouter le titre")
        year = askstring("Input", "Ajouter l'année")
        journal = askstring("Input", "Ajouter le nom du journal dans lequel est publié le livre")
        volume = askstring("Input", "Ajouter le nom du volume")
        number = askstring("Input", "Ajouter le numéro")
        pages = askstring("Input", "Ajouter le nombre de pages")
        mois = askstring("Input", "Ajouter le mois")
        note = askstring("Input", "Ajouter une note")
        publisher = askstring("Input", "Ajouter l'éditeur")
        series = askstring("Input", "Ajouter la série")
        address = askstring("Input", "Ajouter l'adresse")
        edition = askstring("Input", "Ajouter l'édition")
        message = {
            "fonction": "addBook",
            "author": auteur,
            "title": titre,
            "year": year,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": mois,
            "notes": note,
            "publisher": publisher,
            "series": series,
            "address": address,
            "edition": edition
        }
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))
    
    def jsonexport(self):
        contenue = self.text_zone.get("1.0", END).strip()  #Recup contenu affichage
        if not contenue:
            print("Aucune donnée à sauvegarder.")
            return

        # pour faire des ligne
        lines = contenue.split("\n")
        # Créer un dico json avec les data
        data = {"entries": lines}

        # Enregistrer dans un fichier JSON
        filename = "fichier.json"  # Le fichier sera enregistré dans le répertoire actuel
        with open(filename, "w", encoding="utf-8") as json_file: # "with" pour ouvrir le fichier dans un bloc, garantit que le fichier sera automatiquement fermé lorsque le bloc sera terminé
            json.dump(data, json_file, indent=4) # "json file" alias temporerer au fichier json pour utliser le fichier
        print(f"Données sauvegardées dans le fichier : {filename}")


    def quitclient(self): #pour fermet la co avec le serv
        message = {"fonction": "quit"}
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))
        self.client_socket.close()
        self.destroy()
        
        

if __name__ == "__main__":
    main()
