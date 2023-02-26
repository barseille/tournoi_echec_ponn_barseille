from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_menu_joueur import ViewsMenuJoueur
from views.views_reprise_tournoi import ViewsRepriseTournoi
from views.base_views import BaseViews

from .controllers_joueurs import ControllersJoueurs
from .controllers_tournois import ControllersTournois

from models.match import Match

from database.database import Database
from datetime import datetime

import random
import uuid
import json


class ControllersReprise():
    
    def __init__(self):
        self.joueur1 = None
        self.joueur2 = None
        self.controllers_joueurs = ControllersJoueurs()
        self.controllers_tournois = ControllersTournois()
        self.views_menu_joueur = ViewsMenuJoueur()
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.views_reprise_tournoi = ViewsRepriseTournoi()
        self.paires_precedentes = []
        self.match = Match(self.joueur1, self.joueur2)
        self.match_info = []
        self.resultats_round = {}
        self.liste_matchs = []
        self.rounds_restants = 0
       
        
    def recuperation_rounds(self):
        
        # Récupération des rounds du tournoi inachevé
        
        self.tournoi_non_termine = self.views_reprise_tournoi.reprendre_tournoi()
        
        if self.tournoi_non_termine:
            self.lancer_tournoi_inacheve()
        
        
        # self.rounds_totals = self.tournoi_non_termine["nombres_de_rounds"]
        # self.rounds_termines = self.tournoi_non_termine["rounds_effectues"] 
        # self.rounds_restants = self.rounds_totals - self.rounds_termines
    
        # return self.rounds_restants
    
    def lancer_tournoi_inacheve(self):
        
        self.rounds_totals = int(self.tournoi_non_termine["nombres_de_rounds"])
        self.rounds_termines = int(self.tournoi_non_termine["rounds_effectues"]) 
        self.rounds_restants = int(self.rounds_totals) - int(self.rounds_termines)
       
        
        rounds_effectues = 0
        for i in range (self.rounds_restants):
            msg = f"                   -- ROUND {i + 1 + self.rounds_termines}/{self.rounds_totals} --"
            titre = BaseViews()
            titre.presentation(msg)
            rounds_effectues  = f"{i + 1 + self.rounds_termines}/{self.rounds_totals}"
            
            # Ajouter le temps de début du round
            debut_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Mélanger les joueurs pour le premier round
            if i == 0: 
                random.shuffle(self.tournoi_non_termine["joueurs"])
            # Trier les joueurs par score et par ordre alphabétique
            else:    
                self.tournoi_non_termine["joueurs"].sort(key=lambda x: x["score"], reverse=True)
                
            # Lancer les matchs pour le round    
            self.lancer_match(self.tournoi_non_termine["joueurs"])
            
            # Ajouter le temps de fin du round
            fin_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            self.liste_matchs = self.creer_liste_scores_joueurs(self.tournoi_non_termine["joueurs"])
            
            # Ajouter les résultats du round au dictionnaire resultats_round
            self.resultats_round[f"Round {i+1+ self.rounds_termines}"] = {"matchs": self.match_info.copy(),
                                                                            "debut": debut_round,
                                                                            "fin": fin_round,
                                                                            "scores_joueurs": self.liste_matchs.copy()}
            
            # Vider la liste des matchs pour le prochain round
            self.match_info.clear()
            self.liste_matchs.clear() 
            
            # Demander à l'utilisateur s'il veut continuer
            if i < self.tournoi_non_termine["nombres_de_rounds"] - 1:
                while True:
                    reponse = input("Voulez_vous continuer le prochain round ? (o/n) : ")
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        self.tournoi_non_termine["resultats"].append(self.resultats_round)
                        self.tournoi_non_termine["rounds_effectues"] = rounds_effectues
                        self.tournoi_non_termine["statut"] = "tournoi non termine"
                  
                        terminer = BaseViews()
                        terminer.affichage_termine() 
                        
                        self.mise_a_jour_classement_joueur(self.tournoi_non_termine)
                        # self.sauvegarde(self.tournoi_non_termine)
                        sauvegarde = Database()
                        sauvegarde.ecrire_database(self.tournoi_non_termine, "liste_des_tournois", chemin_fichier="data/historique_tournois.json")
                        self.effacer_tournoi_termine()
                        return
                    else:
                        erreur = BaseViews()
                        erreur.affichage_erreur_choix()                
                        
        self.tournoi_non_termine["resultats"].append(self.resultats_round)  
        self.tournoi_non_termine["rounds_effectues"] = rounds_effectues
        self.tournoi_non_termine["statut"] = "tournoi termine"
        self.affichage_round_complet(self.tournoi) 

        self.mise_a_jour_classement_joueur(self.tournoi_non_termine)
        sauvegarde = Database()
        sauvegarde.ecrire_database(self.tournoi_non_termine, "liste_des_tournois", chemin_fichier="data/historique_tournois.json")
        self.effacer_tournoi_termine()
        
        # terminer = BaseViews()
        # terminer.affichage_termine() 
        
        
    def effacer_tournoi_termine(self):
        
        # Supprimer le tournoi terminé de la liste des tournois inachevés
        with open("data/historique_tournois.json") as f:
            data = json.load(f)
            
        # Boucle pour trouver le tournoi
        for i, tournoi in enumerate(data["liste_des_tournois"]):
            if tournoi["id"] == self.tournoi_non_termine["id"]:
                
                # Supprimer le tournoi de la liste
                del data["liste_des_tournois"][i]
                break

        with open("data/historique_tournois.json", "w") as f:
            json.dump(data, f, indent=4)  
            
        
    # def effacer_tournoi_termine(self):
        
    #     # Supprimer le tournoi terminé de la liste des tournois inachevés
    #     with open("data/historique_tournois.json") as f:
    #         data = json.load(f)
            
    #     # Boucle pour trouver le tournoi
    #     for i, tournoi in enumerate(data["liste_des_tournois"]):
    #         if tournoi["id"] == self.tournoi_non_termine["id"]:
                
    #             # Supprimer le tournoi de la liste
    #             del data["liste_des_tournois"][i]
    #             break

    #     with open("data/historique_tournois.json", "w") as f:
    #         json.dump(data, f, indent=4) 