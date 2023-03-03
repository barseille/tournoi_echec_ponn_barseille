import random
from views.base_views import BaseViews
from .joueur import Joueur
from dataclasses import dataclass

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueurs = []
        self.paires_de_joueurs = []
        self.score = 0
        self.matchs_joues = []
        self.paires_precedentes = []


# class joueurScore:
#     """ Représente le joueur avec son score """

#     def __init__(self, joueur: Joueur, score: int = 0) -> None:
#         self.joueur = joueur
#         self.score = score

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value: int):
#         self._score = value
#         self.joueur.score += value

#     def __str__(self) -> str:
#         return f"Joueur : {self.joueur.nom}, score : {self.score}"

#     def __lt__(self, autre_joueur: "joueurScore"):
#         return self.score < autre_joueur.score


   
# # match = ([P1, score], [P2, score])
# @dataclass
# class Match:
#     """Represente un match entre 2 joueurs"""

#     joueur1: joueurScore
#     joueur_score2: joueurScore

#     @property
#     def j1_nom_complet(self):
#         """Retourne nom et prenom du joueur 1"""
#         return self.joueur1.joueur.nom_complet

#     @property
#     def j2_nom_complet(self):
#         """Retourne nom et prenom du joueur 2"""
#         return self.joueur_score2.joueur.nom_complet

#     def __str__(self) -> str:
#         msg = f"{self.j1_nom_complet} : {self.joueur1.score} VS {self.j2_nom_complet} : {self.joueur_score2.score}"
#         return msg

#     def serialize(self) -> list[tuple, tuple]:
#         """Retourne une liste de tuple avec l'id et le score pour le joueur."""
#         # [(idjoueur1, 0), (idjoueur2, 0)]
#         joueur1 = (self.joueur1.joueur.id, self.joueur1.score)
#         joueur_score2 = (self.joueur_score2.joueur.id, self.joueur_score2.score)
#         return [joueur1, joueur_score2]
#         # [(1, 0.5), (2, 0.5)]

#     @classmethod
#     def create_from_document(cls, data: list) -> "Match":
#         """Return a Match object from a list"""

#         matches: list[Match] = []
#         # chaque élément de data est une liste de 2 list : [[1, 1], [5, 0]]
#         # le premier élément de chaque liste est l'identifiant du joueur, le second le score.
#         for element in data:
#             # First: Get the joueur
#             id1 = element[0][0]
#             id2 = element[1][0]
#             joueur1 = Joueur.get_from_cache(id=id1)
#             joueur2 = Joueur.get_from_cache(id=id2)

#             # Second: Create the joueurScore
#             score_p1 = element[0][1]
#             score_p2 = element[1][1]
#             ps1 = joueurScore(joueur1, score_p1)
#             ps2 = joueurScore(joueur2, score_p2)

#             # create the Match object and add it to the list
#             matches.append(cls(ps1, ps2))

        # return matches

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
        
    
       
   
    
            