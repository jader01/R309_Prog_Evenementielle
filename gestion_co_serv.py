
############################################################################
#
#                            Gestion de connexion 
#                           Serveur TCP Multi Thread
#                       repris du TD mais avec commentaire
#
###########################################################################

#Import des librairie souhaiter

import socket #         permet de gerer les connexion réseau

from _thread import * # permet la gestion des thread

import json #           pour la gestion des datas en json


#Déclaration des varibale que nous allons utiliser plus bas dans notre server :
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

