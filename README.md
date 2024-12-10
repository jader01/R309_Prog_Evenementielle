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
   - **Exporter le contenu de la fenêtre en JSON :**  
     - Après avoir affiché ou recherché des données, cliquez sur le bouton **Exporter en JSON**.  
     - Cette action enregistrera automatiquement le contenu affiché dans la fenêtre dans un fichier **`data.json`** situé dans le même répertoire que celui où le programme est exécuté.
