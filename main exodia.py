import random
from deck import deck, score_exodia
from fonctions import analyse_main_type, analyse_score_exodia

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
#Mise à jour de toutes les variables utilisées

 
NbTirage = 1000
for x in range(NbTirage):
    NbCartes = 6
    main = random.sample(deck, NbCartes)
    NbMonstre, NbMagie, NbPiege, NbExodia = analyse_main_type(main)
    ScorExodia = analyse_score_exodia(main)
    apparition_cartes(main,Compteurs_Cartes_exodia)
    


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
    if 26 < ScorExodia < 38:
        CompteurMeilleurMain += 1
    if ScorExodia >= 38:
        CompteurSuperMain += 1
        
MoyPireMain = (CompteurPireMain / NbTirage) * 100
MoyMain = (CompteurMoyMain / NbTirage) * 100
MoyMeilleurMain = (CompteurMeilleurMain / NbTirage) * 100
MoySuperMain = (CompteurSuperMain / NbTirage) * 100
        
        
# Boucle qui permet 1000 tirage et analyse chaque main pour avoir le nombre total de carte magie, piège et monstre, les score exodia des mains.

print("---------------------Statistique Type de cartes------------------------")
print()
print("Il y a ", TotalMonstre, "monstres.")
print("Il y a ", TotalMagie, "Magie.")
print("Il y a ", TotalPiege, "Piège.")
print()
# Affichage du nombre total de carte magique, de carte piège et de carte monstre tirées au cours des 1000 tirages
print("---------------------Statistique Exodia--------------------------------")
print()
print("Il y a ", TotalExodia, "de morceau d'exodia.")
MoyExodia = TotalExodia / NbTirage
NoteMoyen = ScoreTotalExodia / NbTirage
print("Tu as en moyenne ", MoyExodia, "morceaux d'exodia en main sur", NbTirage, "de tirages.")
print()
#Statistique du nombre de morceaux d'exodia tirés et du nombre moyen de morceaux par main.

print(f"Score moyen de la main {NoteMoyen:.1f} sur {NbTirage} tirages.")
print("Ta meilleur main pour exodia avait", TopMainExodia, "de points.")
print("Il y a eu", CompteurPireMain, "mauvaises mains (score < 22)")
print("Il y a eu", CompteurMoyMain, "mains standard (22 < score < 26)")
print("Il y a eu", CompteurMeilleurMain, "bonnes mains (26 < score < 38)")
print("Il y a eu", CompteurSuperMain, "mains génial ! (score > 38)")
print(
    f"Tu as eu en moyenne {MoyPireMain:.1f}% de mauvaise main, "
    f"{MoyMain:.1f}% de mains standard, "
    f"{MoyMeilleurMain:.1f}% de bonnes mains "
    f"et enfin {MoySuperMain:.1f}% de superbes mains "
    f"sur {NbTirage} tirages.")
print()
print("------------------------Main Exodia------------------------------------")
print()
print("Voici ta meilleure main, qui a eu un score de :", TopMainExodia, "points")

for carte in MeilleurMain :
    PointCarte = 0
    TotalPointCarte = 0
    RoleCarte = carte["role"]
    for role in RoleCarte:
            PointCarte = score_exodia[role]
            TotalPointCarte += PointCarte
    print(f"{carte["nom"]:<40} : {TotalPointCarte:>3} points")
    #Affichage de la meilleur main
print()
print("Voici la pire main, qui a eu un score de :", PireMainExodia, "points")

for carte in PireMain :
    PointCarte = 0
    TotalPointCarte = 0
    RoleCarte = carte["role"]
    for role in RoleCarte:
            PointCarte = score_exodia[role]
            TotalPointCarte += PointCarte
    print(f"{carte["nom"]:<40} : {TotalPointCarte:>3} points")
print()
print("-------------------------------Statistique sortie de carte----------------------------------")
print()

for Nom_Carte,CompteurQuantite in sorted(Compteurs_Cartes_exodia.items(),key=lambda element: element[1],reverse = True):
    print(f"{Nom_Carte:<40} : {CompteurQuantite:>3} fois")
# affichage des résultat

