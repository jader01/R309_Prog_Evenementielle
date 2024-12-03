
############################################################################
#
#                        Gestion de la connexion
#
###########################################################################

#Import des librairie souhaiter
import socket #         permet de gerer les connexion réseau
from _thread import * # permet la gestion des thread
import json #           pour la gestion des datas en json


#Déclaration des varibale que nous allons utiliser plus bas dans notre server :
ClientSocket = None #   initialisation de la variable socket (du serveur)
host = '127.0.0.1' #    initialisation de l'ip du server (ici 127.0.0.1 cad Local host)
port = 9090 #           le port sur le quel le client se connecte au serveur
myNumber = 0 #          identifie le client lors de la déconnexion.

def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #          creation d'un socket TCP
    ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#         Permet de réutiliser l'adresse et le port immédiatement après une fermeture du socket
    try:
        ClientSocket.connect((host, port))#                                     connexion serv en utilisant le socket créé si dessus
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