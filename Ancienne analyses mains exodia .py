import random

deck = [
        {"nom" : "Left Arm of the Forbidden One","Type" : "Monstre","exodia" : True,"role" : ["exodia"]},# score exodia = 8
        
        {"nom" : "Right Leg of the Forbidden One","Type" : "Monstre","exodia" : True,"role" : ["exodia"]},# score exodia = 8
        
        {"nom" : "Left Leg of the Forbidden One","Type" : "Monstre","exodia" : True,"role" : ["exodia"]},# score exodia = 8
        
        {"nom" : "Right Arm of the Forbidden One","Type" : "Monstre","exodia" : True,"role" : ["exodia"]},# score exodia = 8
        
        {"nom" : "Tragoedia","Type" : "Monstre","exodia" : False,"role" : ["survie","finisher","protection"]},# score exodia = 3
        
        {"nom" : "Chaos Witch","Type" : "Monstre","exodia" : False,"role" : ["survie"]}, # score exodia = 1
        
        {"nom" : "Exodia the Forbidden One","Type" : "Monstre","exodia" : True,"role" : ["exodia"]},# score exodia = 8
        
        {"nom" : "Sangan","Type" : "Monstre","exodia" : False,"role" : ["recherche_deck","survie"]},# score exodia = 8
        
        {"nom" : "Sangan","Type" : "Monstre","exodia" : False,"role" : ["recherche_deck","survie"]}, # score exodia = 8
        
        {"nom" : "Electromagnetic turtle","Type" : "Monstre","exodia" : False,"role" : ["survie"]}, # score exodia = 1
        
        {"nom" : "Marshmallon","Type" : "Monstre","exodia" : False,"role" : ["survie"]}, # score exodia = 1
        
        {"nom" : "Mask of Darkness","Type" : "Monstre", "exodia" : False,"role" : ["recherche_cimetiere","survie"]},# score exodia = 8
        
        {"nom" : "Blizzed, Defender of the Ice Barrier","Type" : "Monstre","exodia" : False,"role" : ["pioche","survie"]}, # score exodia = 7
        
        {"nom" : "Blizzed, Defender of the Ice Barrier","Type" : "Monstre","exodia" : False,"role" : ["pioche","survie"]}, # score exodia = 7
        
        {"nom" : "Magician of Faith","Type" : "Monstre","exodia" : False,"role" : ["recherche_cimetiere","survie"]},# score exodia = 6
        
        {"nom" : "Magician of Faith","Type" : "Monstre","exodia" : False,"role" : ["recherche_cimetiere","survie"]},# score exodia = 6
        
        {"nom" : "Cyber Valley","Type" : "Monstre","exodia" : False,"role" : ["pioche","survie"]},# score exodia = 7
        
        {"nom" : "Cyber Valley","Type" : "Monstre","exodia" : False,"role" : ["pioche","survie"]},# score exodia = 7
        
        {"nom" : "Double Spell","Type" : "Magie","exodia" : False,"role" : ["preparation"]},# score exodia = 4
        
        {"nom" : "Card Advance","Type" : "Magie","exodia" : False,"role" : ["preparation"]},# score exodia = 4
        
        {"nom" : "Dark Hole","Type" : "Magie","exodia" : False,"role" : ["survie","controle"]},# score exodia = 4
        
        {"nom" : "Pot of Greed","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Pot of Avarice","Type" : "Magie","exodia" : False,"role" : ["recherche_cimetiere","pioche"]}, # score exodia = 4
        
        {"nom" : "Upstart Goblin","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Upstart Goblin","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Gold Sarcophagus","Type" : "Magie","exodia" : False,"role" : ["recherche_deck"]}, # score exodia = 7
        
        {"nom" : "Monster Reborn","Type" : "Magie","exodia" : False,"role" : ["protection","survie"]}, # score exodia = 3
        
        {"nom" : "Mystical Space Typhoon","Type" : "Magie","exodia" : False,"role" : ["controle","survie"]}, # score exodia = 4
        
        {"nom" : "Supply Squad","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Supply Squad","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Wave-Motion Cannon","Type" : "Magie","exodia" : False,"role" : ["finisher"]}, # score exodia = 1
        
        {"nom" : "Liberty At Last!","Type" : "Piège","exodia" : False,"role" : ["controle"]}, # score exodia = 3
        
        {"nom" : "Time Machine","Type" : "Piège","exodia" : False,"role" : ["protection"]}, # score exodia = 2
        
        {"nom" : "Jar of Greed","Type" : "Piège","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Scrap-Iron Scarecrow","Type" : "Piège","exodia" : False,"role" : ["survie"]}, # score exodia = 1
        
        {"nom" : "Jar of Avarice","Type" : "Piège","exodia" : False,"role" : ["recherche_cimetiere"]}, # score exodia = 5
        
        {"nom" : "Nightmare Wheel","Type" : "Piège","exodia" : False,"role" : ["controle"]}, # score exodia = 3
        
        {"nom" : "Gravity Bind","Type" : "Piège","exodia" : False,"role" : ["survie"]}, # score exodia = 1
        
        {"nom" : "Call of the Haunted","Type" : "Piège","exodia" : False,"role" : ["preparation"]}, # score exodia = 4
        
        {"nom" : "Magic Drain","Type" : "Piège","exodia" : False,"role" : ["protection"]}, # score exodia = 2
]
# Définition des carte qui compose le deck initial

score_exodia = {"exodia" : 8,
                "recherche_deck" : 7,
                "pioche" : 6,
                "recherche_cimetiere" : 5,
                "preparation" : 4,
                "controle" : 3,
                "protection" : 2,
                "survie" : 1,
                "finisher" : 1
                }
# Définition du poids des rôles dans mon deck

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
    
TotalMonstre = 0 
TotalMagie = 0
TotalPiege = 0
TotalExodia = 0
ScorExodia = 0
ScoreTotalExodia = 0
TopMainExodia = 0
MeilleurMain = 0
PireMainExodia = 50
PireMain = 0
CompteurPireMain = 0
CompteurMoyMain = 0
CompteurMeilleurMain = 0
CompteurSuperMain = 0
#Mise à jour de toutes les variables

 
NbTirage = 1000
for x in range(NbTirage):
    NbCartes = 6
    main = random.sample(deck, NbCartes)
    NbMonstre, NbMagie, NbPiege, NbExodia = analyse_main_type(main)
    ScorExodia = analyse_score_exodia(main)


    TotalMonstre += NbMonstre
    TotalMagie += NbMagie
    TotalPiege += NbPiege
    TotalExodia += NbExodia
    ScoreTotalExodia += ScorExodia
    if TopMainExodia < ScorExodia :
        TopMainExodia = ScorExodia
        MeilleurMain = main.copy()
    
    if PireMainExodia > ScorExodia :
        PireMainExodia = ScorExodia
        PireMain = main.copy()
    if ScorExodia <= 22:
        CompteurPireMain += 1
    if 22 < ScorExodia <= 26:
        CompteurMoyMain += 1
    if ScorExodia > 26:
        CompteurMeilleurMain += 1
    if ScorExodia > 38:
        CompteurSuperMain += 1
        
MoyPireMain = (CompteurPireMain / NbTirage) * 100
MoyMain = (CompteurMoyMain / NbTirage) * 100
MoyMeilleurMain = (CompteurMeilleurMain / NbTirage) * 100
MoySuperMain = (CompteurSuperMain / NbTirage) * 100
        
# Boucle qui permet 1000 tirage et analyse chaque main pour avoir le nombre total de carte magie, piège et monstre ainsi que les score exodia des mains

print("---------------------Statistique Type de cartes------------------------")
print()
print("Il y a ", TotalMonstre, "monstres.")
print("Il y a ", TotalMagie, "Magie.")
print("Il y a ", TotalPiege, "Piège.")
print()
print("---------------------Statistique Exodia--------------------------------")
print()
print("Il y a ", TotalExodia, "de morceau d'exodia.")
MoyExodia = TotalExodia / NbTirage
NoteMoyen = ScoreTotalExodia / NbTirage

print("Tu as en moyenne ", MoyExodia, "morceaux d'exodia en main sur", NbTirage, "de tirages.")
print("Score moyen de la main", NoteMoyen, "sur", NbTirage, "tirages.")
print("Ta meilleur main pour exodia avait", TopMainExodia, "de points.")
print("Il y a eu", CompteurPireMain, "mauvaises mains (score < 22)")
print("Il y a eu", CompteurMoyMain, "mains standard (22 < score < 26)")
print("Il y a eu", CompteurMeilleurMain, "bonnes mains (score < 26)")
print("Il y a eu", CompteurSuperMain, "mains génial ! (score < 38)")
print(
    f"Tu as eu en moyenne {MoyPireMain:.1f}% de mauvaise main, "
    f"{MoyMain:.1f}% de mains standard, "
    f"{MoyMeilleurMain:.1f}% de bonnes mains "
    f"et enfin {MoySuperMain:.1f}% de superbes mains "
    f"sur {NbTirage} tirages.")
print()
print("------------------------Main Exodia------------------------------------")
print()
print("Voici ta meilleurs main : "),
for nom in MeilleurMain :
    print()
    print(nom["nom"])
    #Affichage de la meilleur main
print("Voici la pire main : ")
for nom in PireMain :
    print()
    print(nom["nom"])
# affichage des résultat
