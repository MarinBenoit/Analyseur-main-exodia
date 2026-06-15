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
        
        {"nom" : "Pot of extravagence","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 4
        
        {"nom" : "Upstart Goblin","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Upstart Goblin","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Gold Sarcophagus","Type" : "Magie","exodia" : False,"role" : ["recherche_deck"]}, # score exodia = 7
        
        {"nom" : "Monster Reborn","Type" : "Magie","exodia" : False,"role" : ["protection","survie"]}, # score exodia = 3
        
        {"nom" : "Mystical Space Typhoon","Type" : "Magie","exodia" : False,"role" : ["controle","survie"]}, # score exodia = 4
        
        {"nom" : "Supply Squad","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Supply Squad","Type" : "Magie","exodia" : False,"role" : ["pioche"]}, # score exodia = 6
        
        {"nom" : "Wave-Motion Cannon","Type" : "Magie","exodia" : False,"role" : ["finisher"]}, # score exodia = 1
        
        {"nom" : "Change of heart","Type" : "Magie","exodia" : False,"role" : ["preparation"]}, # score exodia = 4
        
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
