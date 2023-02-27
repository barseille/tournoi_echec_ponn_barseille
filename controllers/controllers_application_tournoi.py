# from views.views_reprise_tournoi import ViewsRepriseTournoi
# import json
# import random
# from datetime import datetime
# from views.base_views import BaseViews
# from .controllers_base import ControllersBase
# from views.views_reprise_tournoi import ViewsRepriseTournoi
# from views.base_views import BaseViews
# from .controllers_base import ControllersBase
# from models.match import Match
# from database.database import Database
# import json



# class ControllersApplicationTournoi(ControllersBase):
#     def __init__(self):
#         self.views_reprise_tournoi = ViewsRepriseTournoi()
#         self.joueur1 = None
#         self.joueur2 = None
#         self.match = Match(self.joueur1, self.joueur2)
#         self.paires_precedentes = []
#         self.views_base_views = BaseViews()
#         self.match_info = []
#         self.resultats_round = {}
    
#     def recuperation_tournois_existant(self):
        
#         self.tournoi = self.views_reprise_tournoi.reprendre_tournoi()
#         self.rounds_totals = self.tournoi.get("nombres_de_rounds", [])
#         self.rounds_effectues = self.tournoi.get("round_en_cours", [])
#         self.rounds_restants = self.rounds_totals - self.rounds_effectues
        

#         while True:
                      
#             tournoi = ViewsRepriseTournoi()
#             tournoi.reprendre_tournoi()
           
#             self.liste_des_joueurs = []
            
#             for joueur in self.tournoi["joueurs"]:
#                 self.liste_des_joueurs.append(joueur)
                
#             while True:
#                 try:
#                     choix = input("Souhaitez-vous continuer ce tournoi (o/n) ? ")
#                     if choix == "o":    
#                         self.continuer_tournoi()
#                         break
#                     elif choix == "n":
#                         return
#                     else:
#                         self.views_base_views.affichage_erreur_choix()
                    
                    
#                 except IndexError:
#                     affiche = BaseViews()
#                     affiche.affichage_erreur_numero()
#             break
             
                
       
       
#     def trier_les_joueurs_par_score(self):
        
#         self.liste_des_joueurs.sort(key=lambda x: x["score"], reverse=True)
   
           
#     def continuer_tournoi(self):
        
#         for i in range(self.rounds_restants):
#             affiche_round = f"         -- ROUND {i + 1 + self.rounds_effectues}/{self.tournoi['resultats']} --"
#             affiche = BaseViews()
#             affiche.afficher_msg(affiche_round)
            
       
#             self.lancer_match(self.tournoi["joueurs"])
            
#             date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#             date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#                       # Récuperer les scores dans un tuple par joueur
#             self.liste_matchs = self.creer_liste_scores_joueurs(self.tournoi["joueurs"])
            
            
#             self.liste_de_rounds = {
#                     "numero_round": i + 1+ self.rounds_effectues,
#                     "date_debut": date_debut,
#                     "date_fin": date_fin,
#                     "matchs": self.match_info,
#                     "points": self.liste_matchs
#                     }
    
#             self.tournoi['resultats'].append(self.liste_de_rounds)
#             if i + 1 != self.rounds_restants:
                
#                 choix = input("Voulez vous passer au round suivant ? o(oui) ou taper une touche pour quitter : ")
                
#                 if choix != "o":

#                     with open("data/historique_tournois.json", "r+") as f:
#                         data = json.load(f)
#                         data["historique_tournois"].append(self.tournoi)
#                         f.seek(0)
#                         json.dump(data, f, indent=4)
                        
#                     self.effacer_tournoi_termine()
#                     break
                
#         else:
            
#             with open("data/historique_tournois.json", "r+") as f:
#                 tournoi_fini = json.load(f)
#                 tournoi_fini["liste_des_tournois"].append(self.tournoi)
#                 f.seek(0)
#                 json.dump(tournoi_fini, f, indent=4)
 
#             self.effacer_tournoi_termine()


#         self.affichage_tournoi_termine(self.tournoi)  
        
#     # def lancer_matchs(self):
        
 
#     #     self.trier_les_joueurs_par_score()   
      
#     #     self.liste_de_paire = []
#     #     self.match_info = []

       
#     #     # Pour chaque paire de joueurs, lancer un match
#     #     for i in range(0, len(self.liste_des_joueurs), 2):
#     #         self.joueur1 = self.liste_des_joueurs[i]
#     #         self.joueur2 = self.liste_des_joueurs[i + 1]
#     #         paire = (self.joueur1, self.joueur2)
#     #         self.liste_de_paire.append(paire)
            
            
#     #         joueur1_gagne = f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !"
#     #         joueur2_gagne = f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !"         
#     #         match_nul = "Match nul !"
            
    
#     #     # Lancer chaque match de la liste
#     #     for i, match in enumerate(self.liste_de_paire):
#     #         self.joueur1 = match[0]
#     #         self.joueur2 = match[1]
                
#     #         affichage = f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :"
#     #         affichage_joueur = BaseViews()
#     #         affichage_joueur.presentation(affichage)

#     #         choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

#     #         if choix == "1":
#     #             self.joueur1["score"] += 1
#     #             affiche = BaseViews()
#     #             affiche.afficher_msg(joueur1_gagne)
                
#     #             # Ajouter les informations sur le match à la liste de matchs
#     #             match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#     #             self.match_info.append(match_dict)
                
#     #         elif choix == "2":
#     #             self.joueur2["score"] += 1
#     #             affiche = BaseViews()
#     #             affiche.afficher_msg(joueur2_gagne)
                
#     #             # Ajouter les informations sur le match à la liste de matchs
#     #             match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#     #             self.match_info.append(match_dict)
    
                
#     #         elif choix == "3":
#     #             self.gagnant = random.choice([self.joueur1, self.joueur2])
#     #             self.gagnant["score"] += 1  
#     #             joueur_aleatoire = f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !"
      
#     #             affiche = BaseViews()
#     #             affiche.afficher_msg(joueur_aleatoire)  
                
#     #             # Ajouter les informations sur le match à la liste de matchs
#     #             match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#     #             self.match_info.append(match_dict)               
                        
                
#     #         else:
#     #             self.joueur1["score"] += 0.5
#     #             self.joueur2["score"] += 0.5
#     #             affiche = BaseViews()
#     #             affiche.afficher_msg(match_nul)  
                
#     #             # Ajouter les informations sur le match à la liste de matchs
#     #             match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#     #             self.match_info.append(match_dict)
        
        
#     #     # Réinitialiser la liste "matchs" du tournoi
#     #     self.liste_matchs = []
        
#     #     # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
#     #     for joueur in self.tournoi['joueurs']:
#     #         nom = joueur['nom']
#     #         score = joueur['score']
#     #         self.liste_matchs.append((nom, score))
#     #         msg = f"Joueur {nom} = {score}"
#     #         affichage_score = BaseViews()
#     #         affichage_score.afficher_msg(msg)
                
                
#     def effacer_tournoi_termine(self):
        
#         # Supprimer le tournoi terminé de la liste des tournois inachevés
#         with open("data/historique_tournois.json") as f:
#             data = json.load(f)
            
#         # Boucle pour trouver le tournoi
#         for i, tournoi in enumerate(data["historique_tournois"]):
#             if tournoi["nom"] == self.tournoi["nom"]:
                
#                 # Supprimer le tournoi de la liste
#                 del data["historique_tournois"][i]
#                 break

#         with open("data/historique_tournois.json", "w") as f:
#             json.dump(data, f, indent=4)
            
            
