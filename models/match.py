import random
from views.base_views import BaseViews

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueurs = []
        self.paires_de_joueurs = []
        self.score = 0
        self.matchs_joues = []
        self.paires_precedentes = []
    
        
    def melanger_joueurs(self, joueurs):
        random.shuffle(joueurs)
 
        
    def generer_paire(self, joueurs):
        paires = []
        for i in range(0, len(joueurs), 2):
            joueur1 = joueurs[i]
            joueur2 = joueurs[i + 1]
            paires.append((joueur1, joueur2))
        return paires
   
    
    def faire_match(self, joueurs):
        
        paire = self.generer_paire(joueurs)
        self.melanger_joueurs(joueurs)
        
        while paire and paire in self.paires_precedentes:
            self.melanger_joueurs(joueurs)
            paire = self.generer_paire(joueurs)    
            
        self.paires_precedentes.append(paire)
        resultats_match = []
        for i, j in enumerate(paire):
            self.affichage_msg(f"Match n°{i+1} : {j[0]['prenom']} {j[0]['nom']} VS {j[1]['prenom']} {j[1]['nom']}")
            
            while True:     
                choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2 et 3 pour égalité) : ")        
                try:           
                    if choix == "1":
                        j[0]["score"] += 1
                        resultats_joueur1 = [(j[0], j[0]["score"])]
                        resultats_match.extend(resultats_joueur1)
                        # self.joueur1["score"] += 1
                        # resultats_match.append((j[0], j[0]["score"]))
                        self.affichage_msg(f"{j[0]['prenom']} {j[0]['nom']} a gagné\n")
                        break
                    
                    elif choix == "2":
                        self.joueur2["score"] += 1
                        resultats_joueur2 = [(j[1], j[1]["score"])]
                        resultats_match.extend(resultats_joueur2)
                        # resultats_match.append((j[1], j[1]["score"]))
                        self.affichage_msg(f"{j[1]['prenom']} {j[1]['nom']} a gagné\n")
                        break
                    
                    elif choix == "3":
                        self.joueur1["score"] += 0.5
                        self.joueur2["score"] += 0.5
                        resultats_match.append((j[0], j[0]["score"]))
                        resultats_match.append((j[1], j[1]["score"]))
                        self.affichage_msg("Match nul !\n")
                        break
                    
                    else:
                        self.affichage_msg("Choix invalide. Veuillez taper 1, 2, 3")          
                except ValueError:
                    self.affichage_msg("Choix invalide. Veuillez taper 1, 2, 3")
                    
        # Réinitialiser la liste "matchs" du tournoi
        self.liste_de_matchs = []
        
        # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
        for joueur in paire:
            nom = joueur['nom']
            score = joueur['score']
            self.liste_de_matchs.append((nom, score))   
                    
        print(self.liste_de_matchs)
        return resultats_match          
           
    def affichage_msg(self,msg):  
        affiche = BaseViews()
        affiche.afficher_msg(msg)
        
    
       
   
    
            