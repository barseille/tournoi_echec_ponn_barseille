from views.views_reprise_tournoi import ViewsRepriseTournoi
from views.base_views import BaseViews
from .controllers_base import ControllersBase
from models.match import Match
from database.database import Database
import json


class ControllersReprise(ControllersBase):
    def __init__(self):
        self.views_reprise_tournoi = ViewsRepriseTournoi()
        self.joueur1 = None
        self.joueur2 = None
        self.match = Match(self.joueur1, self.joueur2)
        self.paires_precedentes = []
        self.views_base_views = BaseViews()
        self.match_info = []
        self.resultats_round = {}
       
        
    def recuperation_rounds(self):
        
        self.tournoi = self.views_reprise_tournoi.reprendre_tournoi()
        self.rounds_totals = self.tournoi.get("nombres_de_rounds", [])
        self.rounds_effectues = self.tournoi.get("round_en_cours", [])
        self.rounds_restants = self.rounds_totals - self.rounds_effectues
        
        return self.rounds_restants
        

    def lancer_tournoi(self):
        
        self.tournoi["resultats"] = []
        recup_round = 0
        recup_round = self.rounds_effectues       
        for i in range (self.rounds_restants):
            msg = f"                   -- ROUND {i + 1 + self.rounds_effectues}/{self.rounds_totals} --"
            titre = BaseViews()
            titre.presentation(msg)
            recup_round +=1
            
            # Ajouter le temps de début du round
            debut_round = self.enregistrer_temps_round()
            self.tournoi["joueurs"].sort(key=lambda x: x["score"], reverse=True)
            self.lancer_match(self.tournoi["joueurs"])
            
            # Ajouter le temps de fin du round
            fin_round = self.enregistrer_temps_round() 
            
            # Récuperer les scores dans un tuple par joueur
            self.liste_matchs = self.creer_liste_scores_joueurs(self.tournoi["joueurs"])
            
            
            # Ajouter les résultats du round au dictionnaire resultats_round
            self.resultats_round[f"Round {i+1+self.rounds_effectues}/{self.tournoi['nombres_de_rounds']}"] = {"matchs": self.match_info.copy(),
                                                                                                                "debut": debut_round,
                                                                                                                "fin": fin_round,
                                                                                                                "scores_joueurs": self.liste_matchs.copy()}
            
            # Vider la liste des matchs pour le prochain round
            self.vider_listes_matchs() 
            
            
            # Demander à l'utilisateur s'il veut continuer
            if i + 1  < self.tournoi["nombres_de_rounds"] - 1:
                while True:
                    reponse = input("Voulez_vous continuer le prochain round ? (o/n) : ")
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        
                      
                        self.tournoi["resultats"].append(self.resultats_round)                 
                        self.tournoi["statut"] = "tournoi non termine"
                        self.tournoi["round_en_cours"] = recup_round
                        self.views_base_views.affichage_termine()
                        
                        self.mise_a_jour_classement_joueur(self.tournoi)
                        self.sauvergarde()
                        # self.effacer_tournoi_termine()
                        return
                    else: 
                        self.views_base_views.affichage_erreur_choix() 
                        
        self.tournoi["resultats"].append(self.resultats_round)      
        self.tournoi["statut"] = "tournoi termine" 
        self.tournoi["round_en_cours"] = recup_round
        
        self.mise_a_jour_classement_joueur(self.tournoi)
        self.sauvergarde() 
        self.affichage_tournoi_termine(self.tournoi)
           
  
    def effacer_tournoi_termine(self):
        
        # Supprimer le tournoi terminé de la liste des tournois inachevés
        with open("data/historique_tournois.json") as f:
            data = json.load(f)
            
        # Boucle pour trouver le tournoi
        for i, tournoi in enumerate(data["liste_des_tournois"]):
            if tournoi["id"] == self.tournoi["id"]:
                
                # Supprimer le tournoi de la liste
                del data["liste_des_tournois"][i]
                break

        with open("data/historique_tournois.json", "w") as f:
            json.dump(data, f, indent=4)  
            
        
    def sauvegarde(self):
        sauvegarde = Database()
        sauvegarde.ecrire_database(self.tournoi,self.tournoi["resultats"], chemin_fichier="data/historique_tournois.json")
   
