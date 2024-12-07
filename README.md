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

### [Serveur](serveur.py)  

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
  - Mise à jour des widgets en fonction des événements (par exemple, résultats de recherche).  
- **Connexion TCP/IP** : Établissement et gestion de la connexion avec le serveur.  

---

## Fonctionnalités Avancées (Bonus)  

Pour enrichir le projet, les fonctionnalités suivantes peuvent être implémentées :  
- Ajout de sous-classes spécifiques aux publications (ex. : articles scientifiques, livres, rapports).  
- Affichage amélioré des résultats de recherche (par exemple, avec des **onglets** ou des **fenêtres flottantes**).  
- Export avancé des résultats avec des options de tri ou de filtrage.  
