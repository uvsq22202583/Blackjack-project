import random
import tkinter as tk
nombre_joueur = 1
carte_tirée = []
nombre_tiré =[]
croupier = 0
joueur_1 = 0
nombre_ale = 0
nom_du_joueur="joueur 1"
racine = tk.Tk() 
racine.title("Blackjack") 
labelnom = tk.Label(racine, text = "Quel est votre nom ?",font=("helvetica","20"))
labelnom.grid()
nomString = tk.StringVar()
entrynom = tk.Entry(racine, textvariable=nomString)
entrynom.grid(column=1, row=0, padx=10)

def associer_nom_joueur():
    nom_du_joueur = 0
    nom_du_joueur = nomString

valider_nom = tk.Button(racine, text="valider",font=("helvetica","20"), command = lambda: racine.destroy)
valider_nom.grid(row = 2, column = 1)

def associer_as_un():
    nombre_tiré.append(1)

def associer_as_onze():
    nombre_tiré.append(11)


def tirer_une_carte_aléatoire ():
    nombre_ale = random.randint(1,13)
    couleur_ale = random.randint(1,4)
    
    if couleur_ale == 1 :
        couleur_ale = " de coeur"
    elif couleur_ale == 2 :
        couleur_ale = " de pique"
    elif couleur_ale == 3 :
        couleur_ale = " de carreau"
    elif couleur_ale == 4 :
        couleur_ale = " de trèfle"
    carte = str(nombre_ale)+str(couleur_ale)
    if carte not in carte_tirée:
        if  nombre_ale > 1 and nombre_ale < 10 :
            carte_tirée.append(carte)
            nombre_tiré.append(nombre_ale)
        elif nombre_ale >= 10:
            nombre_ale = 10
            nombre_tiré.append(nombre_ale)
            carte = str(nombre_ale)+str(couleur_ale)
            carte_tirée.append(carte)
        elif nombre_ale == 1 :
            carte_tirée.append(carte)
            racine = tk.Tk()
            racine.title("Blackjack") 
            label_as_onze = tk.Label(racine, text="Vous avez pioché un as, vous voulez qu'il compte pour un ou pour onze ?", font=("helvetica", "20")) 
            label_as_onze.grid(row = 0, column = 1, columnspan = 2)
            espace = tk.Label(racine, text = "   ", font=("helvetica", "20"))
            espace.grid(row = 1)
            as_un = tk.Button(racine, text="un",font=("helvetica","20"), command = associer_as_un)
            as_onze = tk.Button(racine, text="onze",font=("helvetica","20"), command = associer_as_onze)
            as_un.grid(row = 2, column = 0, columnspan = 2, ipadx = 50)
            as_onze.grid(row = 2, column = 2, ipadx = 50)
            valider_nom = tk.Button(racine, text="valider",font=("helvetica","20"), command = racine.destroy)
            valider_nom.grid(row = 3, column = 1)
            racine.mainloop() 
            

for i in range (4):
    tirer_une_carte_aléatoire()
    
score_croupier = nombre_tiré[0] + nombre_tiré[2]
score_joueur_1 = nombre_tiré[1] + nombre_tiré[3]

racine = tk.Tk()
racine.title("Blackjack") 
label_main_croupier = tk.Label (racine, text="Le croupier a pioché un "+ carte_tirée[0], font=("helvetica", "20"))
label_main_croupier.grid()
label_main_joueur = tk.Label(racine, text=nom_du_joueur + " a pioché un "+ carte_tirée[1] + " et un "+ carte_tirée[3], font=("helvetica", "20"))
label_main_joueur.grid()
valider_main = tk.Button(racine, text="ok",font=("helvetica","20"), command = racine.destroy)
valider_main.grid(row = 3, column = 1)
racine.mainloop()

#jusque la ca fonctionne


def tirer_une_carte_alé_deux_plus_joueur (score_joueur_1):
    nombre_ale = random.randint(1,13)
    couleur_ale = random.randint(1,4)
    carte = str(nombre_ale)+str(couleur_ale)
    if carte not in carte_tirée:
        if  nombre_ale > 1 and nombre_ale < 10 :
            carte_tirée.append(carte)
            nombre_tiré.append(nombre_ale)
            score_joueur_1 = score_joueur_1 + nombre_tiré[-1]
        elif nombre_ale >= 10:
            carte_tirée.append(carte)
            nombre_ale = 10
            nombre_tiré.append(nombre_ale)
            score_joueur_1 = score_joueur_1 + nombre_tiré[-1]
        elif nombre_ale == 1 :
            carte_tirée.append(carte)
            racine = tk.Tk()
            racine.title("Blackjack") 
            label_as_onze = tk.Label(racine, text="Vous avez pioché un as, vous voulez qu'il compte pour un ou pour onze ?", font=("helvetica", "20")) 
            label_as_onze.grid(row = 0, column = 1, columnspan = 2)
            espace = tk.Label(racine, text = "   ", font=("helvetica", "20"))
            espace.grid(row = 1)
            as_un = tk.Button(racine, text="un",font=("helvetica","20"), command = associer_as_un)
            as_onze = tk.Button(racine, text="onze",font=("helvetica","20"), command = associer_as_onze)
            as_un.grid(row = 2, column = 0, columnspan = 2, ipadx = 50)
            as_onze.grid(row = 2, column = 2, ipadx = 50)
            valider_nom = tk.Button(racine, text="valider",font=("helvetica","20"), command = racine.destroy)
            valider_nom.grid(row = 3, column = 1)
            racine.mainloop() 
            score_joueur_1 = score_joueur_1 + nombre_tiré[-1]
    racine = tk.Tk()
    racine.title("Blackjack")
    label_main_joueur = tk.Label (racine, text=nom_du_joueur + " a pioché un "+ str(nombre_tiré[-1]) , font=("helvetica", "20"))
    label_main_joueur.grid() 
    racine.mainloop       
    
while score_joueur_1 < 21:
    racine = tk.Tk()
    racine.title("Blackjack") 
    label_score = tk.Label(racine, text = "Vous avez un score de" + str(score_joueur_1) )
    label_carte = tk.Label(racine, text="Voulez-vous pioché une carte ?", font=("helvetica", "20")) 
    label_carte.grid(row = 0, column = 1, columnspan = 2)
    espace = tk.Label(racine, text = "   ", font=("helvetica", "20"))
    espace.grid(row = 1)
    oui_nvl_carte = tk.Button(racine, text="oui",font=("helvetica","20"), command = tirer_une_carte_alé_deux_plus_joueur(score_joueur_1))
    oui_nvl_carte.grid(row = 2, column = 0, columnspan = 2, ipadx = 50)
    non_nvl_carte = tk.Button(racine, text="non",font=("helvetica","20"), command = racine.destroy)
    non_nvl_carte.grid(row = 2, column = 2, ipadx = 50)
    valider_nvl_carte = tk.Button(racine, text="valider",font=("helvetica","20"), command = racine.destroy)
    valider_nvl_carte.grid(row = 3, column = 2)
    racine.mainloop() 
    score_joueur_1 = score_joueur_1 + nombre_tiré[-1]
    print(score_joueur_1)


    
if score_joueur_1 > 21 :
    racine = tk.Tk() # Création de la fenêtre racine
    racine.title("Blackjack") # ajoute un titre
    label = tk.Label(racine, text= nom_du_joueur +" vous avez perdu", font=("helvetica", "20")) # création du widget
    label.grid() # positionnement du widget
    racine.mainloop() # Lancement de la boucle principale
elif score_joueur_1 == 21 : 
    racine = tk.Tk() # Création de la fenêtre racine
    racine.title("Blackjack") # ajoute un titre
    label = tk.Label(racine, text= nom_du_joueur +" vous avez gagné", font=("helvetica", "20"))  # création du widget
    label.grid() # positionnement du widget
    racine.mainloop() # Lancement de la boucle principale
else :
    print("Le coupier avais pioché un ", str(nombre_tiré[0]), "et un ", str(nombre_tiré[2]))
    while croupier < 17 :
        tirer_une_carte_aléatoire()
        croupier = croupier + nombre_tiré[-1]
        print("croupier vous avez pioché un ",str(nombre_tiré[-1]),"votre score est donc de:", str(croupier))
    while croupier < 21:
        demande = str(input("Croupier voulez-vous tirez une carte?"))
        if demande == "non" :
            break
        else :
            tirer_une_carte_aléatoire()
            croupier = croupier + nombre_tiré[-1]
            print("Croupier vous avez pioché un ",nombre_tiré[-1],"votre score est donc de:", croupier)
            
    if croupier > 21 :
        racine = tk.Tk() # Création de la fenêtre racine
        racine.title("Blackjack") # ajoute un titre
        label = tk.Label(racine, text="le croupier a perdu," + nom_du_joueur + "avez donc gagné", font=("helvetica", "20"))
        label.grid()
        racine.mainloop()
    if croupier == 21 :
        racine = tk.Tk()
        racine.title("Blackjack")
        label = tk.Label(racine, text="le croupier a gagné", font=("helvetica", "20"))
        label.grid()
        racine.mainloop()
    if score_joueur_1 > croupier and score_joueur_1 < 21 :
        racine = tk.Tk()
        racine.title("Blackjack")
        label = tk.Label(racine, text= nom_du_joueur + " a gagné(e)", font=("helvetica", "20"))
        label.grid() 
        racine.mainloop() 
    elif croupier > score_joueur_1 and croupier < 21:
        racine = tk.Tk()
        racine.title("Blackjack")
        label = tk.Label(racine, text="le croupier a gagné", font=("helvetica", "20"))
        label.grid()
        racine.mainloop()
    elif croupier == score_joueur_1 :
        racine = tk.Tk()
        racine.title("Blackjack")
        label = tk.Label(racine, text="vous êtes à égalité", font=("helvetica", "20"))
        label.grid() 
        racine.mainloop()