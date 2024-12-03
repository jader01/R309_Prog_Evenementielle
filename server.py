############################################################################
#
#      creation d'une variable pour les résultat des recherches
#
###########################################################################

search_global = []  

############################################################################
#
# Class pour stockage BDD
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

        # Ajoute automatiquement l'instance à la liste globale
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


class Book(Article):
    def __init__(self, author, title, year, journal, volume, number, pages, month, notes, publisher, series, address, edition):
        super().__init__(author, title, year, journal, volume, number, pages, month, notes)
        self.publisher = publisher
        self.series = series
        self.address = address
        self.edition = edition

    def printBook(self):
        self.printPubli()
        print(f"Éditeur : {self.publisher}")
        print(f"Série : {self.series}")
        print(f"Adresse : {self.address}")
        print(f"Édition : {self.edition}")


# Fonction de recherche globale
def search(critere, valeur):
    resultats = []  #les objets qui répondent aux critères de recherche
    for elm in search_global: # )arcourt chaque élément (elm) de la liste search_global qui contient toutes éléments d'objets des classes
        if hasattr(elm, critere) and getattr(elm, critere) == valeur:
            resultats.append(elm)
    return resultats


# Exemple d'utilisation
publi1 = Article("Jean Dupont", "Un Article Test", "2023", "Le Monde", 1, 1, "1-10", "Janvier", "ceci est une note")
publi2 = Article("Alice Martin", "Un Second Article", "2022", "Science Today", 2, 3, "15-20", "Février", "Autre note")
livre = Book("Jean Dupont", "Un Livre Test", "2023", "Le Monde", 1, 1, "1-10", "Janvier", "livre de jean ayant pour titre test", "michel lafon", "libre jeunesse", "Paris", "1ère Édition")

publi3 = Article("Stephen King", "Ca", "2004", "Horror", "1", "1", "1-200", "Otobre", "Livre d'horreur")


# Recherche globale
resultats = search(input("Quel type de donner souhaiter vous rechercher : "), input("la donner a recherche "))

print("\nRésultats de la recherche globale :")
for elm in resultats:
    if isinstance(elm, Book):
        elm.printBook()  # Affiche un livre
    elif isinstance(elm, Article):
        elm.printPubli()  # Affiche un article
