import random
import tkinter as tk
nombre_joueur = 1
carte_tirée = []
liste_carte=[]
nombre_tiré =[]
croupier = 0
joueur_1 = 0
nombre_ale = 0
nom_du_joueur=str(input("Quel est votre nom ?"))

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
            carte = "as" +str(couleur_ale)
            carte_tirée.append(carte)
            as_onze= str(input("Voulez-vous que ce soit un as ou un onze?"))
            if as_onze == "as" :
                nombre_ale = 1
                nombre_tiré.append(nombre_ale)
            elif as_onze == "onze" :
                nombre_ale = 11
                nombre_tiré.append(nombre_ale)

            
    
for i in range (4):
    tirer_une_carte_aléatoire()
    
croupier = nombre_tiré[0] + nombre_tiré[2]
joueur_1 = nombre_tiré[1] + nombre_tiré[3]
print("le croupier a pioché un",carte_tirée[0])   
print(nom_du_joueur,"a pioché un",carte_tirée[1],"et un",carte_tirée[3],",vous avez donc un score de", joueur_1)   

while joueur_1 < 21:
    demande = str(input("Voulez-vous tirez une carte?"))
    if demande == "non" :
        break
    else :
        tirer_une_carte_aléatoire()
        joueur_1 = joueur_1 + nombre_tiré[-1]
        print(nom_du_joueur,"vous avez pioché un ", carte_tirée[-1],"votre score est donc de:", joueur_1)
        
    
if joueur_1 > 21 :
    print(nom_du_joueur, "vous avez perdu")
elif joueur_1 == 21 : 
    print(nom_du_joueur, "vous avez gagné")
else :
    print("Le coupier avais pioché un ", carte_tirée[0], "et un ", carte_tirée[2])
    while croupier < 17 :
        tirer_une_carte_aléatoire()
        croupier = croupier + nombre_tiré[-1]
        print("croupier vous avez pioché un ",carte_tirée[-1],"votre score est donc de:", croupier)
    while croupier < 21:
        demande = str(input("Croupier voulez-vous tirez une carte?"))
        if demande == "non" :
            break
        else :
            tirer_une_carte_aléatoire()
            croupier = croupier + nombre_tiré[-1]
            print("Croupier vous avez pioché un ",carte_tirée[-1],"votre score est donc de:", croupier)
            
    if croupier > 21 :
        print("Croupier vous avez", croupier, "vous avez donc perdu,", nom_du_joueur,"vous avez gagné")
    if croupier == 21 :
            print("le croupier à gagné")
    if joueur_1 > croupier and joueur_1 < 21 :
         print(nom_du_joueur, "vous avez gagné")
    elif croupier > joueur_1 and croupier < 21:
        print("le croupier à gagné")
    elif croupier == joueur_1 :
        print("vous etes à égalité")


