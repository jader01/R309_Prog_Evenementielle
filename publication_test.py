############################################################################
#
# Class publication
#
###########################################################################

class Publication : #creation de la classe "mere"
    
    def __init__(self, reference, autheur, titre, annee): #on initalise la class avec ces attribus de base
        #print('lancement initialisation'
        self.ref = reference
        self.author = autheur
        self.title = titre
        self.year = annee

    def printPubli(self): # affichage de la publication
        if self.ref is not None :
            print(self.ref)
            print(self.author)
            print(self.title)
            print(self.year)
    
    def Addpubli(self, refchoisi, autheurchoisi, titrechoisi, anneechoisi):
        self.ref.append(refchoisi)
        self.author.append(autheurchoisi)
        self.title.append(titrechoisi)
        self.year.append(anneechoisi)

class Book(Publication) :
    
    def __init__(self, publi, vol, serie, adress, editeur, mois, notes):
        self.publisher = publi
        self.volume = vol
        self.series = serie
        self.address = adress
        self.edition = editeur
        self.month = mois
        self.note = notes

    def printBook(self):
        if self.ref is not None :
            print(self.ref)

class Improceeding(Publication) :
    
    def __init__(self, titredulivre, publieur, page, orga):
        self.booktitle = titredulivre
        self.publisher = publieur
        self.pages = page
        self.organization = orga

class phdthesis(Publication):

    def __init__(self, ecole, type) :
        self.school = ecole
        self.type = type





###############################################################
#
#   apl des fonctions
#
################################################################

publi1 = Publication("2", "jean", "revus ", 2004)
publi1.printPubli()

publi2 = Publication()
publi2.Addpubli("3", "eichiro oda", "one piece", 2003)
publi2.printPubli()