#########################################################
#
#               Program test page de base
#
#########################################################

from tkinter import *



def on_double_click(event):
    print("Position de la souris:", event.x, event.y)

app = Tk()
app.bind("<Double-Button-1>", on_double_click)
#app.mainloop()



def incremente():
    "Incrémente le compteur à chaque seconde"
    global compteur
    compteur += 1
    compteur_lbl['text'] = str(compteur)
    app2.after(1000, incremente)

def incremente_rapide():
    "Incrémente le compteur toutes les 0.8 secondes"
    global compteur_rapide
    compteur_rapide += 1
    compteur_rapide_lbl['text'] = str(compteur_rapide)
    app2.after(800, incremente_rapide)

app2= Tk()
compteur = 0
compteur_rapide = 0
compteur_lbl = Label(app2, text=str(compteur), font=("", 16))
compteur_lbl.grid(padx=8, pady=8)
compteur_rapide_lbl = Label(app2, text=str(compteur_rapide), font=("", 16))
compteur_rapide_lbl.grid(padx=8, pady=8)

app2.after(1000, incremente)
app2.after(800, incremente_rapide)
app2.mainloop()
