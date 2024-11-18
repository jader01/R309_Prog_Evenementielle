from tkinter import *
 
 
#Fonction déplacement de la balle :
def deplacement():
    global dx, dy
    if (canvas.coords(balle1)[1]<0): #rebond de la balle
        dy=-1*dy
    if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>500): #rebond de la balle
        dx=-1*dx
    if (canvas.coords(balle1)[3]>400) :
        perdu=Label(tk, text="perdu !", font=("arial", 500)) #on creer un variable perdu label([la fenetre], [on affiche du texte "le texte en question"], [la taille du texte])
        perdu.pack()
        canvas.delete(balle1) #je tue la balle
   
    #Test de la collision avec la raquette :
    if len(canvas.find_overlapping(canvas.coords(raquette)[0],canvas.coords(raquette)[1],canvas.coords(raquette)[2],canvas.coords(raquette)[3]))>1: #[0] haut de la raquette
        dy=-1*dy #balle part en sens inverse quand elle touche la raquette
    
    #Collistion + destricution des briques
    coll = canvas.find_overlapping(canvas.coords(balle1)[0],canvas.coords(balle1)[1],canvas.coords(balle1)[2],canvas.coords(balle1)[3])
    print(coll)
    if len(coll)>=2 : #c'est une collision
        if coll[1]>=3 : #c'est une brique
            canvas.delete(coll[1])
            dy = -1 * dy #balle part en sens inverse quand elle touche une brique

   
    #On deplace la balle :
    canvas.move(1,dx,dy)
   
    #On repete cette fonction
    tk.after(20,deplacement)
   
#Fonction pour le deplacement vers la droite de la raquette:
def droite(event):
    if (canvas.coords(raquette)[2])<500 :
        canvas.move(raquette,20,0) #20 sur x et 0 sur y
   
#Fonction pour le deplacement vers la gauche de la raquette:
def gauche(event):
    if (canvas.coords(raquette)[0])>0 :
        canvas.move(raquette,-20,0) #-20 sur l'axe x et 0 sur y
 
#Fonction creation brique :

def briques():
    for yb in range(0,100,40) : #(0), commence à 0 (100) va jusqua 100 en y en comptant de 20 en 20 (100/20=5 brique)
        for xb in range(0,500,100) : #commence à 0 va jusqu'a 500 (autre bout de la ligne) et creer  tout les 100 (donc 1/2)
            brique=canvas.create_rectangle(xb,yb, xb+50, yb+20, fil =('purple'))
        for xb in range(50,500,100) : #commence à 50 pour pas se superposer, va jusqu'a 500 en comptant de 100
            brique=canvas.create_rectangle(xb,yb, xb+50, yb+20, fil =('red'))
    
    for yb in range(20,100,40) : #(0), commence à 0 (100) va jusqua 100 en y en comptant de 20 en 20 (100/20=5 brique)
        for xb in range(0,500,100) : #commence à 0 va jusqu'a 500 (autre bout de la ligne) et creer  tout les 100 (donc 1/2)
            brique=canvas.create_rectangle(xb,yb, xb+50, yb+20, fil =('red'))
        for xb in range(50,500,100) : #commence à 50 pour pas se superposer, va jusqu'a 500 en comptant de 100
            brique=canvas.create_rectangle(xb,yb, xb+50, yb+20, fil =('purple'))

#Vitesse de deplacement de la balle:
dx=5
dy=5

#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='quitte', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenetre :
Bouton_Quitter.pack()
 
#On cree une balle:
balle1 = canvas.create_oval(200,200,230,230,fill='purple')

#On cree une raquette:
raquette = canvas.create_rectangle(100,380,300,390,fill='black') #permier partie largeur de la raquette, bas, file=couleur raquette




 #On associe les fleches du clavier aux fonctions droite() et gauche():
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)

#On lance la fonction brique :
briques()

#On lance le mouvement:
deplacement()
 
#On lance la boucle principale:
tk.mainloop()