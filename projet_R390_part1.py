###############################################################################
#
#       Toutes les bases de creation de "widget" tkinter pour le projet
#
#############################################################################

#import la librairie
from tkinter import *

#On cree une fenetre avec différents parametres :
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


#Les différents type de curseur : 
Button(fenetre, text ="arrow", relief=RAISED, cursor="arrow").pack()
Button(fenetre, text ="circle", relief=RAISED, cursor="circle").pack()
Button(fenetre, text ="clock", relief=RAISED, cursor="clock").pack()
Button(fenetre, text ="cross", relief=RAISED, cursor="cross").pack()
Button(fenetre, text ="dotbox", relief=RAISED, cursor="dotbox").pack()
Button(fenetre, text ="exchange", relief=RAISED, cursor="exchange").pack()
Button(fenetre, text ="fleur", relief=RAISED, cursor="fleur").pack()
Button(fenetre, text ="heart", relief=RAISED, cursor="heart").pack()
Button(fenetre, text ="man", relief=RAISED, cursor="man").pack()
Button(fenetre, text ="mouse", relief=RAISED, cursor="mouse").pack()
Button(fenetre, text ="pirate", relief=RAISED, cursor="pirate").pack()
Button(fenetre, text ="plus", relief=RAISED, cursor="plus").pack()
Button(fenetre, text ="shuttle", relief=RAISED, cursor="shuttle").pack()
Button(fenetre, text ="sizing", relief=RAISED, cursor="sizing").pack()
Button(fenetre, text ="spider", relief=RAISED, cursor="spider").pack()
Button(fenetre, text ="spraycan", relief=RAISED, cursor="spraycan").pack()
Button(fenetre, text ="star", relief=RAISED, cursor="star").pack()
Button(fenetre, text ="target", relief=RAISED, cursor="target").pack()
Button(fenetre, text ="tcross", relief=RAISED, cursor="tcross").pack()
Button(fenetre, text ="trek", relief=RAISED, cursor="trek").pack()
Button(fenetre, text ="watch", relief=RAISED, cursor="watch").pack()

b1 = Button(fenetre, text ="FLAT", relief=FLAT).pack()
b2 = Button(fenetre, text ="RAISED", relief=RAISED).pack()
b3 = Button(fenetre, text ="SUNKEN", relief=SUNKEN).pack()
b4 = Button(fenetre, text ="GROOVE", relief=GROOVE).pack()
b5 = Button(fenetre, text ="RIDGE", relief=RIDGE).pack()




#On lance toute la fenetre
fenetre.mainloop()



