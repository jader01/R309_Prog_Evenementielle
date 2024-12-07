
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
        ClientSocket.connect((host, port))#              à                      connexion serv en utilisant le socket créé si dessus
    except socket.error as e:
        print(str(e))
    finally:
        print("connection au serveur réussi !")
        myNumber = int(ClientSocket.recv(1024))
        print("nombre de client reçu : ", myNumber)
    
    # Créer la fenêtre
    window = MyWindow(ClientSocket)

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


class MyWindow(Tk): #classe pour l'interface graphique
    def __init__(self, client_socket):
        Tk.__init__(self)
        self.client_socket = client_socket

        self.geometry("500x400")
        self.title("R309 Prog even")

        #label_t = Label(self, text="Bibliothèque:\n")
        #label_t.pack()

        button_bibli = Button(self, text="Afficher publication", command=self.printBibli)
        button_bibli.pack()

        button_livre = Button(self, text="Afficher livre", command=self.printLivre)
        button_livre.pack()

        button_add = Button(self, text="Recherche", command=self.recherche)
        button_add.pack()

        menubar = Menu(self)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Ajouter Publi", command=self.addArt)
        menu1.add_command(label="Ajouter Livre", command=self.addBook)

        menubar.add_cascade(label="Ajouter", menu=menu1)
        self.config(menu=menubar)



        boutonfermer = Button(self, text="quitter", command=self.quitclient)  # A FAIRE : CREER UN BOUTON FERMETURE CFONNEXION
        boutonfermer.pack(side=BOTTOM)


        # Ajouter la zone de texte comme un attribut de l'objet
        self.text_zone = Text(self, height=10, width=50)
        self.text_zone.pack()

    def printBibli(self):
        message = {}
        message["fonction"] = "bibli"
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))


    def printLivre(self):
        message = {"fonction": "printBook"}
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))


    
    def recherche(self):
        critere = askstring("Input", "Critère de recherche (author, title, year, ...):")
        search = askstring("Input", "Que voulez vous rechercher ?")
        message = { 
            "fonction": "search", 
            "critere": critere, 
            "valeur": search 
            }
       
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))
    
    def addArt(self):
        auteur= askstring("Input", "Ajouter le nom de l'auteur")
        titre = askstring("Input", "Ajouter le titre")
        year = askstring("Input", "Ajouter l'anéee")
        journal = askstring("Input", "Ajouteur le nom du journal dans le quel est publier l'article")
        volume= askstring("Input", "Ajouter le nom du volume")
        number= askstring("Input", "Ajouter le nom du volume")
        pages = askstring("Input", "Ajouter le nombre de page")
        mois= askstring("Input", "Ajouter le mois")
        note= askstring("Input", "Ajouter une note")
        message = {
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

    def addBook(self):
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

    def quitclient(self):
        message = {"fonction": "quit"}
        message = json.dumps(message)
        self.client_socket.sendall(str.encode(message))
        self.client_socket.close()
        self.destroy()
        
        

if __name__ == "__main__":
    main()
