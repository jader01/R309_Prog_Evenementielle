# R309 - Programmation Événementielle

## Objectifs

L’objectif de ce projet est de comprendre et d'implémenter la **programmation par événements**. Il s'agit de concevoir un programme en Python capable de déclencher des fonctions *callback* en réponse à des événements spécifiques. Ce projet combine plusieurs aspects, dont l'interface graphique, les communications réseau, et la gestion du multithreading.  

### Travail réalisé

L'application à développer permet de consulter et gérer des **références bibliographiques**. Ce projet comprend les étapes suivantes :  
1. **Interface graphique avec Tkinter** :  
   - Création des widgets (boutons, champs de texte, menus, etc.).  
   - Gestion de leur placement dans l'application.  
   - Ajout d’événements et fonctions *callback* pour rendre l'interface interactive.  
2. **Communication réseau** :  
   - Développement d'une architecture client/serveur basée sur des sockets TCP/IP.  
   - Échange de données en temps réel entre le client et le serveur.  
3. **Multithreading** :  
   - Gestion simultanée des connexions réseau et des mises à jour de l'interface graphique.  
   - Implémentation de threads pour gérer les tâches asynchrones.  
4. **Fonctionnalités principales** :  
   - Ajout d'une nouvelle publication dans la base de données.  
   - Consultation et affichage de toutes les publications disponibles.  
   - Recherche de publications selon différents critères.  
   - Export des résultats dans un fichier texte ou JSON.  

---

## Programmes

### [Serveur](server.py)  

Ce programme gère les fonctionnalités côté serveur. Il est responsable de :  
- **Gestion des classes** : Définition des objets représentant les publications (par exemple, `Article` et `Book`).  
- **Fonctions principales** :  
  - Ajouter une nouvelle publication.  
  - Rechercher des publications selon des critères.  
  - Afficher toutes les publications disponibles.  
- **Connexion TCP/IP** : Gestion des connexions réseau avec les clients via des sockets.  

---

### [Client](client.py)  

Ce programme gère l'interface utilisateur et la communication avec le serveur. Il est responsable de :  
- **Interface graphique avec Tkinter** :  
  - Création de l'interface utilisateur (widgets et conteneurs).  
  - Mise à jour des widgets en fonction des événements (résultats de recherche, ajout d'un article).  
- **Connexion TCP/IP** : Établissement et gestion de la connexion avec le serveur.  


## Comment tester le programme  

1. **Lancer le serveur :**  
   - Exécutez le fichier [server.py](server.py).  
   - Cela démarre le serveur et initialise la gestion des publications ainsi que la connexion TCP côté serveur.  

2. **Lancer le client :**  
   - Exécutez le fichier [client.py](client.py).  
   - Cela ouvre l'interface graphique Tkinter et connecte le client au serveur.  

3. **Utiliser l'interface graphique :**  
   - **Afficher les publications :** Cliquez sur le bouton **Afficher publication** pour récupérer et afficher toutes les publications disponibles.  
   - **Afficher les livres :** Cliquez sur le bouton **Afficher livre** pour afficher uniquement les livres.  
   - **Effectuer une recherche :**  
     - Cliquez sur le bouton **Recherche**.  
     - Une fenêtre s'ouvre pour indiquer le critère de recherche (par exemple : `author` pour rechercher par auteur, `year` pour rechercher par année, ou `title` pour rechercher par titre).  
     - Une seconde fenêtre permet de saisir la valeur à rechercher.  
   - **Ajouter une publication :**  
     - Cliquez sur **Ajouter** en haut à droite, puis sur **Ajouter article**.  
     - Une série de fenêtres apparaîtront pour demander les informations nécessaires (par exemple : nom de l'auteur, titre, année, etc.). Remplissez ces champs pour ajouter un nouvel article.  

---
