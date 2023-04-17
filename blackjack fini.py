import random               #importer le dictionnaire random
import tkinter as tk        #importer le dictionnaire tkinter en tant que tk



carte_tirée = []            #définition de la variable carte tirée
nombre_tiré =[]             #définition de la variable nombre tiré
croupier = 0                #définition de la variable du score du croupier
joueur_1 = 0                #définition de la variable du score du joueur
nombre_ale = 0              #définition de la variable nombre aléatoire
stop = False                #définition de la variable de stop 
stop_croupier = False       #définition de la variable de stop du croupier




def fonction_nom() :
    global nomString
    nomString = nomString.get()
    nomString = str(nomString)
    return nomString

racine_nom = tk.Tk()                                                                                        #Création de la fenêtre racine
racine_nom.title("Blackjack")                                                                               #ajoute un titre
racine_nom.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                       #définition de l'image de fond
img = img.zoom(3,3)                                                                                         #redimension de l'image de fond
labelimage = tk.Label(racine_nom, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                               #placement de l'image
labelmise = tk.Label(racine_nom, fg="red", text = "Quel est votre nom ",font=("roadstore","20"))            #création du label pour demander le nom
labelmise.grid(column=0, row=3, padx= 250, pady=200)
nomString = tk.StringVar()  
entrynom = tk.Entry(racine_nom, textvariable=nomString, fg="red", font=("roadstore","20"))                  #création de la cellule d'écriture
entrynom.grid(column=1, row=3, padx=0, pady=200)     
ok_mise = tk.Button(racine_nom, fg = "red", text="ok",font=("roadstore","20"), command = fonction_nom)   #création du bouton valider
ok_mise.grid(column = 2, row = 3, padx=50, pady=200)                                                                                                                                    
valider_mise = tk.Button(racine_nom, fg = "red", text="valider",font=("roadstore","20"), command = racine_nom.destroy)   #création du bouton valider
valider_mise.grid(column = 3, row = 3, padx=50, pady=200)                                                    #placement du label pour demender le nom #placement de la cellule d'ecrit
racine_nom.mainloop()                                                                                                                                                                #lancement de la boucle racine



def fonction_mise() :
    global miseString
    miseString = miseString.get()
    miseString = int(miseString)
    miseString = miseString*2
    return miseString



racine_mise = tk.Tk()                                                                                        #Création de la fenêtre racine
racine_mise.title("Blackjack")                                                                               #ajoute un titre
racine_mise.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                        #définition de l'image de fond
img = img.zoom(3,3)                                                                                          #redimension de l'image de fond
labelimage = tk.Label(racine_mise, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                                #placement de l'image
labelmise = tk.Label(racine_mise, fg="red", text = "Quel est votre mise ",font=("roadstore","20"))           #création du label pour demander le nom
labelmise.grid(column=0, row=3, padx= 250, pady=200)
miseString = tk.StringVar()  
entrynom = tk.Entry(racine_mise, textvariable=miseString, fg="red", font=("georgia","20"))                   #création de la cellule d'écriture
entrynom.grid(column=1, row=3, padx=0, pady=200)     
ok_mise = tk.Button(racine_mise, fg = "red", text="ok",font=("roadstore","20"), command = fonction_mise)     #création du bouton valider
ok_mise.grid(column = 2, row = 3, padx=50, pady=200)                                                                                                                                    
valider_mise = tk.Button(racine_mise, fg = "red", text="valider",font=("roadstore","20"), command = racine_mise.destroy)   #création du bouton valider
valider_mise.grid(column = 3, row = 3, padx=50, pady=200)                                                    #placement du label pour demender le nom #placement de la cellule d'ecrit
racine_mise.mainloop()                                                                          #lancement de la boucle racine




def associer_as_un():                               #associer le score de 1 à un as 
    nombre_tiré.append(1)                           #ajouter 1 à la liste des nombres tirés
    racine.mainloop                                 #lancement de la boucle racine


def associer_as_onze():                              #associer le score de 11 à un as 
    nombre_tiré.append(11)                           #ajouter 11 à la liste des nombres tirés
    racine.mainloop                                  #lancement de la boucle racine


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
        elif nombre_ale == 1 :                       #si la carte est un as on demande au joueur ce qu'il préfère entre un 1 et un 11    
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
    elif carte in carte_tirée:                     #si la carte a déjà été pioché on repioche
        carte = tirer_une_carte_aléatoire()        
    
for i in range (4):                                #boucle qui permet de tirer quatre carte (2 pour le joueur et 2 pour le croupier)
    tirer_une_carte_aléatoire()


croupier = nombre_tiré[0] + nombre_tiré[2]         #associer la premiere et la troisieme carte au coupier
joueur_1 = nombre_tiré[1] + nombre_tiré[3]         #associer la deuxieme et quartrieme carte au joueur




racine = tk.Tk()                                                                                        #Création de la fenêtre racine
racine.title("Blackjack")                                                                               #ajoute un titre
racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
labelimage = tk.Label(racine, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                           #placement du label image 
label_main_croupier = tk.Label (racine, fg="red", text= "croupier vous avez un"+ carte_tirée[0], font=("georgia", "20")) #création du label qui donne la carte pioché par le croupier
label_main_croupier.grid(row=0, column=0, padx= 350, pady=150)                                          #placement du label du score du croupier
label_main_joueur = tk.Label(racine, fg="red", text= str(nomString) + " vous avez un" + carte_tirée[1] + " et un" + carte_tirée[3] + " vous avez donc un score de " + str(joueur_1), font=("georgia", "20")) #création du label qui donne la carte pioché par le joueur
label_main_joueur.grid(row=2, column=0, padx= 200, pady=300)                                            #placement du label du score du joueur
valider_main = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = racine.destroy)   #création du bouton valider
valider_main.grid(row = 1, column = 1, pady=0)                                                          #placement du bouton valider
racine.mainloop()                                                                                       #lancement de la fenetre racine



def tirer_une_carte_alé_deux_plus_joueur(joueur):    #définition de la fonction qui permet au joueur de tirer une carte
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
    if carte not in carte_tirée:                     #vérifier que chaque n'est tirée qu'une seule fois
        carte_tirée.append(carte)                    #ajouter la nouvelle carte à la liste des cartes tirées
        if  nombre_ale > 1 and nombre_ale < 10 :     #si la carte est un nombre entre 2 et 10 on l'ajoute à la liste des nombres tiré
            nombre_tiré.append(nombre_ale)           #ajouter le nombre tiré à la liste des nombres tirés
            joueur = joueur + nombre_tiré[-1]        #ajouter le nouveau nombre au score du joueur
        elif nombre_ale >= 10:                       #si la carte est une tête on lui assoice la valeur de 10
            nombre_ale = 10                          #associer le score de 10 aux têtes
            nombre_tiré.append(nombre_ale)           #ajouter le nombre tiré à la liste des nombres tirés   
            joueur = joueur + nombre_tiré[-1]        #ajouter le nouveau nombre au score du joueur
        elif nombre_ale == 1 :                       #si la carte est un as
            racine = tk.Tk()                                                                                        #Création de la fenêtre racine
            racine.title("Blackjack")                                                                               #ajoute un titre
            racine.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
            img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                       #définition de l'image de fond
            img = img.zoom(3,3)                                                                                         #redimension de l'image de fond
            labelimage = tk.Label(racine_mise, image = img)                                                              #création du label image
            labelimage.place(x=-200,y=-3)                                                                               #placement de l'image                                                                                                                                                                                                                 #verfier que la carte soit  un as 
            label_as_onze = tk.Label(racine,fg="red", text="Vous avez pioché un as, vous voulez qu'il compte pour un ou pour onze ?", font=("roadstore", "20")) # demander au joueur s'il veut que son as compte comme un 1 ou un 11
            label_as_onze.grid(row = 0, column = 1, columnspan = 2)                                                                                             #placer le label qui demande au joueur s'il veut que ca compte pour un 1 ou un 11
            as_un = tk.Button(racine,fg="red", text="un",font=("roadstore","20"), command = associer_as_un)                                                     #crée le bouton qui associe le as au 1
            as_un.grid(row = 1, column = 0, columnspan = 2, ipadx = 50, ipady=50)                                                                               #placer le bouton qui associe le as au 1
            as_onze = tk.Button(racine,fg="red", text="onze",font=("roadstore","20"), command = associer_as_onze)                                               #crée le bouton qui associe le as au 11
            as_onze.grid(row = 1, column = 2, ipadx = 50, ipady=50)                                                                                             #placer le bouton qui associe le as au 11
            valider_nom = tk.Button(racine,fg="red", text="valider",font=("roadstore","20"), command = racine.destroy)                                          #crée la bouton valider
            valider_nom.grid(row = 2, column = 1, ipadx=50)                                                                                                     #placer le bouton valider
            joueur = joueur + nombre_tiré[-1]                                                                                                                   #ajouter le nouveau nombre au score du joueur
    elif carte in carte_tirée:
        carte = tirer_une_carte_alé_deux_plus_joueur
    return joueur                                                                                                                                               #retourner le scrore du joueur

                                                                                                                            





#def arreter_boucle():                 #définir la fonction qui permet d'arreter la boucle 
#    stop = True                       #la variable devient True
#    return stop                       #retourner la valeur stop




 

#def afficher_nouveau_score(joueur):                                           #fonction qui permet d'afficher 
#    racine.destroy                                                            #destruction de la fenfetre racine
#    joueur = tirer_une_carte_alé_deux_plus_joueur(joueur)                     #le score du joueur correspond au score une fois qu'il est passé dans la fonction qui permet de tirer une carte
#    racine_affichage = tk.Tk()                                                #Création de la fenêtre racine_affichage
#    racine_affichage.title("Blackjack")                                       #ajoute un titre
#    racine_affichage.attributes("-fullscreen", True)                          #dimension de la fenetre
#    racine_affichage.configure(bg="green")                                    #placement du label image 
#    label_joueur = tk.Label(racine_affichage, fg="red", text= str(nomString) + " vous avez pioché un" + str(nombre_tiré[-1])   + " vous avez maintenant un score de " + str(joueur), font=("helvetica", "20")) #label qui donne le score du joueur
#    label_joueur.grid(row=0, column=0, padx= 150)                             #placement du label qui donne le nom du score
#    valider_main = tk.Button(racine_affichage, fg = "red", text="valider",font=("roadstore","20"), command = racine_affichage.destroy)   #création du bouton valider
#    valider_main.grid(row = 0, column = 1, padx=50, pady=200)                 #placement du bouton valider 
#    racine_affichage.mainloop()                                               #lancement 
#    return joueur                                                             #retourner le score du joueur







#while joueur_1 < 21:                                                                                                                     #tant que le score du joueur est inférieur à 21
#    if stop == False :                                                                                                                   #si stop est égale à False continuer
#        racine = tk.Tk()                                                                                                                 #Création de la fenêtre racine
#        racine.title("Blackjack")                                                                                                        #ajoute un titre
#        racine.attributes("-fullscreen", True)                                                                                           #dimension de la fenetre
#        img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                   #définition de l'image de fond
#        img = img.zoom(3,3)                                                                                     #redimension de l'image de fond
#        labelimage = tk.Label(racine, image = img)                                                              #création du label image
#        labelimage.place(x=-200,y=-3)                                                                           #placement du label image
#        label_carte = tk.Label(racine, fg="red", text="Voulez-vous pioché une carte ", font=("roadstore", "20"))                         #réation du label carte
#        label_carte.pack(pady= 100)                                                                                                               #placement du label carte
#        non_nvl_carte = tk.Button(racine, fg = "red", text="non",font=("roadstore","20"), command = arreter_boucle)                      #création du bouton non
#        non_nvl_carte.pack()                                                                                                             #placement du bouton non
#        valider_nvl_carte = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = racine.destroy)              #création du bouton valider
#        valider_nvl_carte.pack(pady=100)                                                                                                         #placement du bouton valider
#        abandonner = tk.Button(racine, fg = "red", text="abandonner",font=("roadstore","20"), command = quit)                            #création du bouton abandonner
#        abandonner.pack()                                                                                                                #placement du bouton abandonner
#        oui_nvl_carte_2 = tk.Button(racine, fg = "red", text="oui",font=("roadstore","20"), command= afficher_nouveau_score(joueur_1))   #création du bouton oui
#        oui_nvl_carte_2.pack(pady=100)                                                                                                           #placement du bouton oui
#        joueur_1 = joueur_1 + nombre_tiré[-1]                                                                                            #ajouter le nombre tiré au score du joueur
#        racine.mainloop()                                                                                                                #lancer la fenetre racine 
#    elif stop == True:                                                                                                                   #si stop est égale à True
#        pass                                                                                                                             #sortir de la boucle




#def arreter_boucle_croupier():                 #définir la fonction qui permet d'arreter la boucle pour le croupier
#    stop_croupier = True                       #la variable devient True
#    return stop_croupier                       #retourner la valeur stop




#racine = tk.Tk()                                    #Création de la fenêtre racine
#racine.title("Un premier exemple")                  #ajoute un titre
#racine.attributes("-fullscreen", True)              #dimension de la fenetre
#img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                            #définition de l'image de fond
#img = img.zoom(3,3)                                                                                              #redimension de l'image de fond
#labelimage = tk.Label(racine, image = img)                                                              #création du label image
#labelimage.place(x=-200,y=-3)     
#label = tk.Label(racine, fg="red", text= " Croupier vous aviez pioché un"+ str(carte_tirée[0])+" et un"+ str(carte_tirée[2]), font=("georgia", "20"))  # création du widget qui indique les cartes que le croupier à pioché
#label.grid()                                        #positionnement du widget
#valider_nom = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = racine.destroy)   #création du bouton valider
#valider_nom.grid(column = 2, row = 3, padx=50, pady=200) #placement du bouton valider
#racine.mainloop                                     #lancement de la fenetre
#while croupier < 17 :
#    racine = tk.Tk()                                    #Création de la fenêtre racine
#    racine.title("Un premier exemple")                  #ajoute un titre
#    racine.attributes("-fullscreen", True)              #dimension de la fenetre
#    racine.configure(bg="green")  
#    tirer_une_carte_aléatoire()
#    croupier = croupier + nombre_tiré[-1]
#    label_croupier = tk.Label(racine, fg="red", text= " Croupier vous avez pioché un"+ str(carte_tirée[-1]), font=("roadstore", "20"))  #création du widget
#    label_croupier.grid()                                                                                                               #placement du label croupier
#    valider_nom = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = racine.destroy)                       #création du bouton valider
#    valider_nom.grid(column = 2, row = 3, padx=50, pady=200) 
#    racine.mainloop                                     
#while croupier < 21:
#    if stop_croupier == False :
#        racine = tk.Tk()                                                                                                                 #Création de la fenêtre racine
#        racine.title("Blackjack")                                                                                                        #ajoute un titre
#        racine.attributes("-fullscreen", True)                                                                                           #dimension de la fenetre
#        img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                                            #définition de l'image de fond
#        img = img.zoom(3,3)                                                                                                              #redimension de l'image de fond
#        labelimage = tk.Label(racine_mise, image = img)                                                                                  #création du label image
#        labelimage.place(x=-200,y=-3)                                                                                                    #placement de l'image 
#        label_carte = tk.Label(racine, fg="red", text=" Croupier voulez-vous pioché une carte ", font=("roadstore", "20"))               #création du label carte
#        label_carte.pack()                                                                                                               #placement du label carte
#        non_nvl_carte = tk.Button(racine, fg = "red", text="non",font=("roadstore","20"), command = arreter_boucle)                      #création du bouton non
#        non_nvl_carte.pack()                                                                                                             #placement du bouton non
#        valider_nvl_carte = tk.Button(racine, fg = "red", text="valider",font=("roadstore","20"), command = racine.destroy)              #création du bouton valider
#        valider_nvl_carte.pack()                                                                                                         #placement du bouton valider
#        oui_nvl_carte_2 = tk.Button(racine, fg = "red", text="oui",font=("roadstore","20"), command= afficher_nouveau_score(croupier))   #création du bouton oui
#        oui_nvl_carte_2.pack()                                                                                                           #placement du bouton oui
#        croupier = croupier + nombre_tiré[-1]                                                                                            #ajouter le nombre tiré au score du joueur
#        racine.mainloop()                                                                                                                #lancement de la fenetre racine
#    elif stop_croupier == True:
#        pass                                                                                                       
        

print(joueur_1, croupier)
racine_resultat = tk.Tk()                                                                                        #Création de la fenêtre racine
racine_resultat.title("Blackjack")                                                                               #ajoute un titre
racine_resultat.attributes("-fullscreen", True)                                                                  #dimension de la fenetre
img = tk.PhotoImage(file = "projets\photo du tapis de blackjack.png")                                            #définition de l'image de fond
img = img.zoom(3,3)                                                                                              #redimension de l'image de fond
labelimage = tk.Label(racine_resultat, image = img)                                                              #création du label image
labelimage.place(x=-200,y=-3)                                                                               
if (joueur_1 > 21 and croupier > 21) or (joueur_1 == 21 and croupier == 21) or (joueur_1 < 21 and croupier < 21 and croupier == joueur_1):
    print(joueur_1)
    label_resultat = tk.Label(racine_resultat, fg="red", text = " Vous êtes à égalité ",font=("roadstore","20"))      #création du label pour demander le nom
    label_resultat.grid(column=0, row=3, padx= 250, pady=200)                                                         #placement du label pour demender le nom                                                 #placemenet du bouton valider
    racine_resultat.mainloop()                                                                                             #lancement de la boucle racine
elif (croupier > 21 and joueur_1 <= 21) or (croupier < 21 and joueur_1 == 21 ) or (croupier<21 and joueur_1<21 and croupier<joueur_1):
    print(joueur_1)
    label_resultat = tk.Label(racine_resultat, fg="red", text = str(nomString) + " vous avez gagné, vous avez remporté  " + str(miseString),font=("georgia","20"))             #création du label pour demander le nom
    label_resultat.grid(column=0, row=3, padx= 250, pady=200)                                                         #placement du label pour demender le nom                                                 #placemenet du bouton valider
    racine_resultat.mainloop()    
elif (croupier <= 21 and joueur_1 > 21) or (croupier == 21 and joueur_1 < 21) or (croupier<21 and joueur_1<21 and croupier>joueur_1):
    print(joueur_1)
    label_resultat = tk.Label(racine_resultat, fg="red", text = " le croupier a gagné ",font=("roadstore","20"))      #création du label pour demander le nom
    label_resultat.grid(column=0, row=3, padx= 250, pady=200)                                                         #placement du label pour demender le nom                                                 #placemenet du bouton valider
    racine_resultat.mainloop()    







