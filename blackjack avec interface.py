import random
import tkinter as tk



carte_tirée = []            #définition de la variable carte tirée
nombre_tiré =[]             #définition de la variable nombre tiré
croupier = 0                #définition de la variable du score du croupier
joueur_1 = 0                #définition de la variable du score du joueur
nombre_ale = 0              #définition de la variable nombre aléatoire
stop = False                #définition de la variable de stop 
stop_croupier = False       #définition de la variable de stop du croupier





def sup_widget_nom():             #définition de la fonction qui supprime les widgets qui demnde le nom du joueur
    racine.destroy()              #détruire la fenetre qui demande le nom

    


racine = tk.Tk()                                                                                        #Création de la fenêtre racine
racine.title("Blackjack")                                                                               #ajoute un titre
racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
labelimage = tk.Label(racine, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                           #placement du label image
labelnom = tk.Label(racine, fg="red", text = "Quel est votre nom ",font=("roadstore","20"))             #création du label pour demander le nom
labelnom.grid(column=0, row=3, padx= 250, pady=200)                                                     #placement du label pour demender le nom
nomString = tk.StringVar()                                                                              #création de la variable pour le nom du joueur
entrynom = tk.Entry(racine, textvariable=nomString, fg="red", font=("roadstore","20"))                  #création de la cellule d'écriture
entrynom.grid(column=1, row=3, padx=0, pady=200)                                                        #placement de la cellule d'ecriture
valider_nom = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = sup_widget_nom)   #création du bouton valider
valider_nom.grid(column = 2, row = 3, padx=50, pady=200)                                                #placemenet du bouton valider
racine.mainloop()                                                                                       #lancement de la boucle racine





def associer_as_un():              #associer le score de 1 à un as 
    nombre_tiré.append(1)          #ajouter 1 à la liste des nombres tirés
    racine.mainloop                #lancement de la boucle racine


def associer_as_onze():            #associer le score de 11 à un as 
    nombre_tiré.append(11)         #ajouter 11 à la liste des nombres tirés
    racine.mainloop                #lancement de la boucle racine


def tirer_une_carte_aléatoire ():                    #definition de la fonction qui permet de tirer les première carte
    nom_nombre_ale = ""                              #définition de la variable du nom de la carte
    nombre_ale = random.randint(1,13)                #associer un nombre aléatoire entre 1 et 13 à la variable nombre_ale
    couleur_ale = random.randint(1,4)                #associer un nombre aléatoire entre 1 et 4 à la variable couleur_ale
    if couleur_ale == 1 :                            #associer la couleur_ale 1 au coeur
        couleur_ale = " de coeur"
    elif couleur_ale == 2 :                          #associer la couleur_ale 2 au pique
        couleur_ale = " de pique"
    elif couleur_ale == 3 :                          #associer la couleur_ale 3 au carreau
        couleur_ale = " de carreau"
    elif couleur_ale == 4 :                          #associer la couleur_ale 4 au trèfle
        couleur_ale = " de trèfle"
    if nombre_ale < 11 :                             #associer les nombres à la variable nom_nombre_ale
        nom_nombre_ale = " " + str(nombre_ale)
    elif nombre_ale >= 11:
        if nombre_ale == 11:                         #associer le mot valet au nombre 11
            nom_nombre_ale = " valet"
        elif nombre_ale == 12:                       #associer le mot dame au nombre 12
            nom_nombre_ale = "e dame"
        elif nombre_ale == 13:                       #associer le mot roi au nombre 13
            nom_nombre_ale = " roi"
    carte = str(nom_nombre_ale)+str(couleur_ale)     #définir la carte comme le nom de la couleur et de la carte
    if carte not in carte_tirée:                     #vérifier que chaque n'est tirée qu'une seule fois
        carte_tirée.append(carte)                    #ajouter la nouvelle carte à la liste des cartes tirées
        if  nombre_ale > 1 and nombre_ale < 10 :     #si la carte est un nombre entre 2 et 10 on l'ajoute à la liste des nombres tiré
            nombre_tiré.append(nombre_ale)
        elif nombre_ale >= 10:                       #si la carte est une tête on lui assoice la valeur de 10
            nombre_ale = 10
            nombre_tiré.append(nombre_ale)
        elif nombre_ale == 1 :                      #si la carte est un as on demande au joueur ce qu'il préfère entre un 1 et un 11    
            racine = tk.Tk()                                                                                        #Création de la fenêtre racine
            racine.title("Blackjack")                                                                               #ajoute un titre
            racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
            img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
            img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
            labelimage = tk.Label(racine, image = img)                                                              #création du label image
            labelimage.place(x=-200,y=-3)                                                                           #placement du label image
            label_as_onze = tk.Label(racine, text="Vous avez pioché un as, vous voulez qu'il compte pour un ou pour onze ?", font=("roadstore", "20")) # demander au joueur s'il veut que son as compte comme un 1 ou un 11
            label_as_onze.grid(row = 0, column = 1, columnspan = 2)                                                 #placement du label as_onze
            as_un = tk.Button(racine, fg="red", text="un",font=("roadstore","20"), command = associer_as_un)        #création du bouton pour associer l'as au 1
            as_un.grid(row = 1, column = 0, columnspan = 2, ipadx = 50, ipady=50)                                   #placement du bouton pour associer l'as au 1
            as_onze = tk.Button(racine, fg="red", text="onze",font=("roadstore","20"), command = associer_as_onze)  #création du bouton pour associer l'as au 11
            as_onze.grid(row = 1, column = 2, ipadx = 50, ipady=50)                                                 #placement du bouton pour associer l'as au 11
            def sup_widget_as():                                                                                    #dénition de la fonction qui permet de détruire la fenetre de demande 1 ou 11 
               label_as_onze.destroy()                                                                              #destruction du label as_onze
               as_onze.destroy()                                                                                    #destruction du bouton as_onze
               as_un.destroy()                                                                                      #destruction du bouton as_un
               valider_as.destroy()                                                                                 #destruction du bouton valider
            valider_as = tk.Button(racine, fg="red", text="valider",font=("roadstore","20"), command = sup_widget_as) #creation du bouton valider 
            valider_as.grid(row = 2, column = 1, ipadx=50)                                                          #placement du bouton valider
            racine.mainloop                                                                                         #lancement de la boucle racine
            
    
for i in range (4):                                     #boucle qui permet de tirer quatre carte (2 pour le joueur et deux pour le croupier)
    tirer_une_carte_aléatoire()


croupier = nombre_tiré[0] + nombre_tiré[2]              #associer la premiere et la troisieme carte au coupier
joueur_1 = nombre_tiré[1] + nombre_tiré[3]              #associer la deuxieme et quartrieme carte au joueur




def sup_widget_main():                                   #définition de la fonction qui supprime les widgets qui demnde le nom du joueur
    label_main_croupier.destroy()                        #suppression du widget qui pose la question
    label_main_joueur.destroy()                          #suppression du widget ou l'utilisateur entre son prénom
    valider_main.grid_forget()                           #cacher le bouton valider
    racine.destroy()                                     #lancement de la boucle racine





print("le score du joueur 1 est ",joueur_1)
racine = tk.Tk()                                                                                        #Création de la fenêtre racine
racine.title("Blackjack")                                                                               #ajoute un titre
racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
labelimage = tk.Label(racine, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                           #placement du label image 
label_main_croupier = tk.Label (racine, fg="red", text= "croupier vous avez un"+ carte_tirée[0], font=("georgia", "20"))
label_main_croupier.grid(row=0, column=0, padx= 350, pady=150)
label_main_joueur = tk.Label(racine, fg="red", text= str(nomString) + " vous avez un" + carte_tirée[1] + " et un" + carte_tirée[3] + " vous avez donc un score de " + str(joueur_1), font=("georgia", "20"))
label_main_joueur.grid(row=2, column=0, padx= 200, pady=300)
valider_main = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = sup_widget_main)   #création du bouton valider
valider_main.grid(row = 1, column = 1, pady=0)  
racine.mainloop()



def tirer_une_carte_alé_deux_plus_joueur(joueur):  #définition de la fonction qui permet au joueur de tirer une carte
    nom_nombre_ale = ""                              #définition de la variable du nom de la carte
    nombre_ale = random.randint(1,13)                #associer un nombre aléatoire entre 1 et 13 à la variable nombre_ale
    print("le nombre aleatoire est", nombre_ale)
    couleur_ale = random.randint(1,4)                #associer un nombre aléatoire entre 1 et 4 à la variable couleur_ale
    print("la couleur aleatoire est", couleur_ale)
    if couleur_ale == 1 :                            #associer la couleur_ale 1 au coeur
        couleur_ale = " de coeur"
    elif couleur_ale == 2 :                          #associer la couleur_ale 2 au pique
        couleur_ale = " de pique"
    elif couleur_ale == 3 :                          #associer la couleur_ale 3 au carreau
        couleur_ale = " de carreau"
    elif couleur_ale == 4 :                          #associer la couleur_ale 4 au trèfle
        couleur_ale = " de trèfle"
    if nombre_ale < 11 :                             #associer les nombres à la variable nom_nombre_ale
        nom_nombre_ale = " " + str(nombre_ale)
    elif nombre_ale >= 11:
        if nombre_ale == 11:                         #associer le mot valet au nombre 11
            nom_nombre_ale = " valet"
        elif nombre_ale == 12:                       #associer le mot dame au nombre 12
            nom_nombre_ale = "e dame"
        elif nombre_ale == 13:                       #associer le mot roi au nombre 13
            nom_nombre_ale = " roi"
    carte = str(nom_nombre_ale)+str(couleur_ale)     #définir la carte comme le nom de la couleur et de la carte
    print(carte)
    if carte not in carte_tirée:                     #vérifier que chaque n'est tirée qu'une seule fois
        carte_tirée.append(carte)                    #ajouter la nouvelle carte à la liste des cartes tirées
        print(carte_tirée)
        if  nombre_ale > 1 and nombre_ale < 10 :     #si la carte est un nombre entre 2 et 10 on l'ajoute à la liste des nombres tiré
            nombre_tiré.append(nombre_ale)           #ajouter le nombre tiré à la liste des nombres tirés
            joueur = joueur + nombre_tiré[-1]        #ajouter le nouveau nombre au score du joueur
            print("le score du joueur est", joueur)
        elif nombre_ale >= 10:                       #si la carte est une tête on lui assoice la valeur de 10
            nombre_ale = 10                          #associer le score de 10 aux têtes
            nombre_tiré.append(nombre_ale)           #ajouter le nombre tiré à la liste des nombres tirés   
            joueur = joueur + nombre_tiré[-1]        #ajouter le nouveau nombre au score du joueur
            print("le score du joueur est de ", joueur)
        elif nombre_ale == 1 :                                                                                                                         #verfier que la carte soit  un as 
            label_as_onze = tk.Label(racine, text="Vous avez pioché un as, vous voulez qu'il compte pour un ou pour onze ?", font=("roadstore", "20")) # demander au joueur s'il veut que son as compte comme un 1 ou un 11
            label_as_onze.grid(row = 0, column = 1, columnspan = 2)                                                                                    #placer le label qui demande au joueur s'il veut que ca compte pour un 1 ou un 11
            as_un = tk.Button(racine, text="un",font=("roadstore","20"), command = associer_as_un)                                                     #crée le bouton qui associe le as au 1
            as_un.grid(row = 1, column = 0, columnspan = 2, ipadx = 50, ipady=50)                                                                      #placer le bouton qui associe le as au 1
            as_onze = tk.Button(racine, text="onze",font=("roadstore","20"), command = associer_as_onze)                                               #crée le bouton qui associe le as au 11
            as_onze.grid(row = 1, column = 2, ipadx = 50, ipady=50)                                                                                    #placer le bouton qui associe le as au 11
            valider_nom = tk.Button(racine, text="valider",font=("roadstore","20"), command = racine.destroy)                                          #crée la bouton valider
            valider_nom.grid(row = 2, column = 1, ipadx=50)                                                                                            #placer le bouton valider
            joueur = joueur + nombre_tiré[-1]    
            print("le score du joueur est de :", joueur)  
    return joueur
#ajouter le nouveau nombre au score du joueur
                                                                                                                             #placer le label qui affiche la carte tirée





def arreter_boucle():                 #définir la fonction qui permet d'arreter la boucle 
    stop = True                       #la variable devient Vrai
    return stop



def sup_widget_tirer_carte():         #définir la fonction qui supprime la fentre racine
    racine.destroy                    #détruire la fenetre racine

 

def afficher_nouveau_score(joueur):
    racine = tk.Tk()                                                                                        #Création de la fenêtre racine
    racine.title("Blackjack")                                                                               #ajoute un titre
    racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
    img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
    img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
    labelimage = tk.Label(racine, image = img)                                                              #création du label image
    labelimage.place(x=-200,y=-3)                                                                           #placement du label image 
    label_joueur = tk.Label(racine, fg="red", text= str(nomString) + " vous avez pioché un " + str(nombre_tiré[-1])   + " vous avez maintenant un score de " + str(joueur), font=("helvetica", "20"))
    label_joueur.grid(row=2, column=0, padx= 250, pady=300)
    valider_main = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = sup_widget_main)   #création du bouton valider
    valider_main.grid(row = 1, column = 1, padx=50, pady=0)  
    racine.mainloop()





print(joueur_1)
while joueur_1 < 21:
    if stop == False :
        joueur_1 = tirer_une_carte_alé_deux_plus_joueur(joueur_1)
        racine = tk.Tk()                                                                                        #Création de la fenêtre racine
        racine.title("Blackjack")                                                                               #ajoute un titre
        racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
        img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
        img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
        labelimage = tk.Label(racine, image = img)                                                              #création du label image
        labelimage.place(x=-200,y=-3)                                                                           #placement du label image
        label_score = tk.Label(racine, text = "Vous avez un score de" + str(joueur_1) )                         #création du label score
        label_score.grid(row = 0, column = 1, columnspan = 2)                                                   #placement du label score
        label_carte = tk.Label(racine, text="Voulez-vous pioché une carte ", font=("roadstore", "20"))          #création du label carte
        label_carte.grid(row = 0, column = 1, columnspan = 2)                                                   #placement du label carte
        oui_nvl_carte = tk.Button(racine, fg="red", text="oui",font=("roadstore","20"), command = afficher_nouveau_score(joueur_1))
        oui_nvl_carte.grid(row = 2, column = 0, columnspan = 2, ipadx = 50)
        non_nvl_carte = tk.Button(racine, fg="red", text="non",font=("roadstore","20"), command = arreter_boucle)
        non_nvl_carte.grid(row = 2, column = 2, ipadx = 50)
        valider_nvl_carte = tk.Button(racine, fg="red", text="valider",font=("roadstore","20"), command = sup_widget_tirer_carte)
        valider_nvl_carte.grid(row = 3, column = 2)
        joueur_1 = joueur_1 + nombre_tiré[-1]
        racine.mainloop



def arreter_boucle_croupier():
    global stop
    stop_croupier = True

#faire le copier colle de la fonction


if joueur_1 > 21 :
    racine = tk.Tk()                                                                                        # Création de la fenêtre racine
    racine.title("Un premier exemple")                                                                      # ajoute un titre
    racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
    img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
    img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
    labelimage = tk.Label(racine, image = img)                                                              #création du label image
    labelimage.place(x=-200,y=-3)
    label = tk.Label(racine, fg="red", text= str(nomString) +" vous avez perdu", font=("roadstore", "20")) # création du widget
    label.grid() # positionnement du widget
    racine.mainloop
elif joueur_1 == 21 : 
    racine = tk.Tk()                                                                                        # Création de la fenêtre racine
    racine.title("Un premier exemple")                                                                      # ajoute un titre
    racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
    img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
    img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
    labelimage = tk.Label(racine, image = img)                                                              #création du label image
    labelimage.place(x=-200,y=-3)
    label = tk.Label(racine, fg="red", text= str(nomString) +" vous avez gagné", font=("roadstore", "20"))  # création du widget
    label.grid() # positionnement du widget
    racine.mainloop
else :
    racine = tk.Tk()                                                                                        # Création de la fenêtre racine
    racine.title("Un premier exemple")                                                                      # ajoute un titre
    racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
    img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
    img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
    labelimage = tk.Label(racine, image = img)                                                              #création du label image
    labelimage.place(x=-200,y=-3)
    label = tk.Label(racine, fg="red", text= " Croupier vous aviez pioché un"+ str(carte_tirée[0])+" et un"+ str(carte_tirée[2]), font=("roadstore", "20"))  # création du widget
    label.grid() # positionnement du widget
    racine.mainloop
    while croupier < 17 :
        tirer_une_carte_aléatoire()
        croupier = croupier + nombre_tiré[-1]
        label_croupier = tk.Label(racine, fg="red", text= " Croupier vous avez pioché un"+ str(carte_tirée[-1]), font=("roadstore", "20"))  # création du widget
        label_croupier.grid()
    while joueur_1 < 21:
        if stop_croupier == False :
            joueur= croupier
            label_score = tk.Label(racine, text = "Vous avez un score de" + str(joueur_1) )
            label_carte = tk.Label(racine, text="Voulez-vous pioché une carte ?", font=("roadstore", "20")) 
            label_carte.grid(row = 0, column = 1, columnspan = 2)
            oui_nvl_carte = tk.Button(racine, fg="red", text="oui",font=("roadstore","20"), command = tirer_une_carte_alé_deux_plus_joueur(croupier))
            oui_nvl_carte.grid(row = 2, column = 0, columnspan = 2, ipadx = 50)
            non_nvl_carte = tk.Button(racine, fg="red", text="non",font=("roadstore","20"), command = arreter_boucle_croupier)
            non_nvl_carte.grid(row = 2, column = 2, ipadx = 50)
            valider_nvl_carte = tk.Button(racine, fg="red", text="valider",font=("roadstore","20"), command = sup_widget_tirer_carte)
            valider_nvl_carte.grid(row = 3, column = 2)
            score_joueur_1 = joueur_1 + nombre_tiré[-1]
        





            
    if croupier > 21 :
        print("Croupier vous avez", croupier, "vous avez donc perdu,", nomString,"vous avez gagné")
    if croupier == 21 :
            print("le croupier à gagné")
    if joueur_1 > croupier and joueur_1 < 21 :
         print(nomString, "vous avez gagné")
    elif croupier > joueur_1 and croupier < 21:
        print("le croupier à gagné")
    elif croupier == joueur_1 :
        print("vous etes à égalité")


