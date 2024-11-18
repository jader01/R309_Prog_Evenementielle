###############################################################################
#
#       Toutes les bases de creation de "widget" tkinter pour le projet
#
#############################################################################

#import la librairie
from tkinter import *

#On cree une fenetre avec différentes parametres :
fenetre = Tk() #ici on creer la fenetre

#On cree une un bouton avec différentes parametres :
boutonfermer = Button(fenetre, text="quitter", command=fenetre.quit)  # ici on creer le bouton avec le texte inter et a quoi il sert
boutonfermer.pack(side=BOTTOM)

#On creer un LABEL cad un espaces précus pour écrire du texte : 
label=Label(fenetre, text="ici on teste d'ajouter du text", bg="green")
label.pack(side=RIGHT)

#On crrer une entrer dans la quel on peut inserer du texte : 
value=StringVar()
value.set("texte par def")
entre = Entry(fenetre, width=30)
entre.pack(side=RIGHT)

#On creer une case a cocher :
acocher=Checkbutton(fenetre, text="test")
acocher.pack(side=LEFT)

#On creer un ensemble bouton que l'on peu cocher et si on en coche 1 ça dé coche un autre :
value=StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Maybe", variable=value, value=3)
bouton1.pack(side=LEFT)
bouton2.pack(side=LEFT)
bouton3.pack(side=LEFT)

#On creer une liste qui va permetre de recup la valeur sélectionner
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
liste.pack(side=LEFT)

#On creer un "canvas" (un tableau) c'est un espace qui nous servira de fenetre + tard
canvas = Canvas(fenetre, width = 500, height = 100, bg="white") #ici on a les paramêtres de la fenaitre
txt = canvas.create_text(75, 60, text="ceci est un test")
#test2 = canvas.create_window(bg="green")
canvas.pack()

#On peut aussi creer d'autre chose avec : 
'''
    create_arc()        :  arc de cercle
    create_bitmap()     :  bitmap
    create_image()      :  image
    create_line()       :  ligne
    create_oval()       :  ovale
    create_polygon()    :  polygone
    create_rectangle()  :  rectangle 
    create_text()       :  texte
    create_window()     :  fenetre
'''

#On creer un cadre : 
fenetre['bg']='white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

#On lance toute la fenetre
fenetre.mainloop()



