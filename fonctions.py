def analyse_main_type(main):
    NbMagie = 0
    NbMonstre = 0
    NbPiege = 0
    NbExodia = 0


    for i in main:

        if i["Type"]=="Monstre":
            NbMonstre += 1
            
        if i["Type"]=="Magie":
            NbMagie += 1
       
        if i["Type"]=="Piège":
            NbPiege += 1
        if i["exodia"]==True:
            NbExodia += 1
            
    return NbMonstre, NbMagie, NbPiege, NbExodia
# Fin de la définition de ma fonction, elle renvoie le nombre de monstre, piège et magie dans la main tirer

def analyse_score_exodia(main):
    Exodia = 0
    
    for carte in main:
        RoleCarte = carte["role"]
        for role in RoleCarte:
            PointExodia = score_exodia[role]
            Exodia += PointExodia
        
            
    return Exodia
# Fin de la définition de ma fonction, elle renvoie le score de ma main pour réussir à récuperer exodia

def apparition_cartes(main,Compteurs_Cartes_exodia):
    for carte in main:
        if carte["nom"] in Compteurs_Cartes_exodia:
            Compteurs_Cartes_exodia[carte["nom"]] += 1
            
        else:
            Compteurs_Cartes_exodia[carte["nom"]] = 1
# Fin de la définition de la fonction de compteur de carte
