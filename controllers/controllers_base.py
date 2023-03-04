from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_menu_joueur import ViewsMenuJoueur
from views.base_views import BaseViews
from .controllers_joueurs import ControllersJoueurs
from .controllers_tournois import ControllersTournois
from models.match import Match
from database.database import Database
from datetime import datetime
import random
import uuid



class ControllersBase():
    
    def __init__(self):
        self.joueur1 = None
        self.joueur2 = None
        self.controllers_joueurs = ControllersJoueurs()
        self.controllers_tournois = ControllersTournois()
        self.views_menu_joueur = ViewsMenuJoueur()
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.base_views = BaseViews()
        self.paires_precedentes = []
        self.match = Match(self.joueur1, self.joueur2)
        self.match_info = []
        self.resultats_round = {}
        self.liste_matchs = []
        self.rounds_restants = 0
        self.tournoi_inacheve = {}
       
        
    def fusion_tournoi_avec_joueurs(self):
        # Générer un identifiant unique pour le tournoi
        id_tournoi = str(uuid.uuid4())

        # Demander à l'utilisateur de sélectionner un tournoi
        views_tournoi = self.views_menu_tournoi
        tournoi_selectionne = views_tournoi.afficher_les_tournois()

        # Demander à l'utilisateur de sélectionner les joueurs
        views_joueurs = self.views_menu_joueur
        joueurs_selectionnes = views_joueurs.selectionner_participants()
        
        # Ajouter l'identifiant unique au tournoi sélectionné
        tournoi_selectionne["id"] = id_tournoi

        # Ajouter les joueurs sélectionnés au tournoi sélectionné
        tournoi_selectionne["joueurs"] = joueurs_selectionnes

        # Enregistrer le tournoi mis à jour dans la variable self.tournoi
        self.tournoi = tournoi_selectionne
        
        
    def enregistrer_temps_round(self):
        temps_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return temps_round

   
       

    def lancer_round(self):
        
        self.tournoi["resultats"] = []
        self.recup_round = 0
        for i in range(self.tournoi["nombres_de_rounds"]):
            msg = f"                   -- ROUND {i + 1}/{self.tournoi['nombres_de_rounds']} --"
            titre = BaseViews()
            titre.presentation(msg)
            self.recup_round +=1
   
            # # Ajouter le temps de début du round
            debut_round = self.enregistrer_temps_round()
            
            # Mélanger les joueurs pour le premier round
            if i == 0: 
                random.shuffle(self.tournoi["joueurs"])
            # Trier les joueurs par score et par ordre alphabétique
            else:  
                self.tournoi["joueurs"].sort(key=lambda x: x["score"], reverse=True)
           

            
            # Lancer les matchs pour le round    
            self.lancer_match(self.tournoi["joueurs"])
            
            # Ajouter le temps de fin du round
            fin_round = self.enregistrer_temps_round()
            
            self.liste_matchs = self.creer_liste_scores_joueurs(self.tournoi["joueurs"])
            self.tournoi["resultats"] = []
            
            # # Ajouter les résultats du round au dictionnaire resultats_round
            self.resultats_round[f"Round {i+1}/{self.tournoi['nombres_de_rounds']}"] = {"matchs": self.match_info.copy(),
                                                                                        "debut": debut_round,
                                                                                        "fin": fin_round,
                                                                                        "scores_joueurs": self.liste_matchs.copy()}
            
           
           
            # Vider la liste des matchs pour le prochain round
            self.vider_listes_matchs()   
            
            # Demander à l'utilisateur s'il veut continuer
            if i < self.tournoi["nombres_de_rounds"] - 1:
                while True:
                    reponse = input("Voulez_vous continuer le prochain round ? (o/n) : ")
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        self.recup_tournoi_inacheve()
                        return
                    else: 
                        self.base_views.affichage_erreur_choix()              
                        
        self.tournoi["resultats"].append(self.resultats_round)      
        self.tournoi["statut"] = "tournoi termine" 
        self.tournoi["round_termine"] = self.recup_round
        
        # self.mise_a_jour_classement_joueur(self.tournoi)
        self.sauvergarde()
        
        self.affichage_tournoi_termine(self.tournoi)
        
        return self.resultats_round
   
        
    def affichage_tournoi_termine(self,tournoi):  
        
        if tournoi["nombres_de_rounds"] :  
            self.base_views.affichage_termine()
        

    def lancer_match(self, joueurs):
  
        paire = self.match.generer_paire(joueurs)
        self.match.melanger_joueurs(joueurs)
        
        while paire and paire in self.paires_precedentes:
            self.match.melanger_joueurs(joueurs)
            paire = self.match.generer_paire(joueurs)    
            
        self.paires_precedentes.append(paire)
     
        for i, j in enumerate(paire):
            match_joueurs = f"Match {i+1} : {j[0]['prenom']} {j[0]['nom']} VS {j[1]['prenom']} {j[1]['nom']}"
            self.base_views.afficher_msg(match_joueurs)
            
            while True:     
                choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2 et 3 pour égalité) : ")        
                try:           
                    if choix == "1":
                        j[0]["score"] += 1
                        self.base_views.afficher_msg(f"{j[0]['prenom']} {j[0]['nom']} a gagné\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    elif choix == "2":
                        j[1]["score"] += 1
                        self.base_views.afficher_msg(f"{j[1]['prenom']} {j[1]['nom']} a gagné\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    elif choix == "3":
                        j[0]["score"] += 0.5
                        j[1]["score"] += 0.5    
                        self.base_views.afficher_msg("Match nul !\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    else:
                        self.base_views.afficher_msg("Choix invalide. Veuillez taper 1, 2, 3")        
                except ValueError:
                    self.base_views.afficher_msg("Choix invalide. Veuillez taper 1, 2, 3")
       

    def creer_liste_scores_joueurs(self, joueurs):
        liste_scores_joueurs = []
        for joueur in joueurs:
            nom = joueur['nom']
            score = joueur['score']
            liste_scores_joueurs.append((nom, score))
        return liste_scores_joueurs
       

    def affichage_msg(self, msg):  
               
        # Afficher un message 
        affiche = BaseViews()
        affiche.afficher_msg(msg)  
        self.base_views.afficher_msg(msg)
 
       
    def sauvergarde(self):
        
        data = Database()
        data.ecrire_database(self.tournoi, "liste_des_tournois", chemin_fichier="data/historique_tournois.json")

      
    def mise_a_jour_classement_joueur(self, tournoi):
        
        tournoi["joueurs"].sort(key=lambda x: (x["score"], x["nom"]), reverse=True)
        for i, joueur in enumerate(tournoi["joueurs"]):
            joueur["classement"] = i + 1


    def vider_listes_matchs(self):
        
        self.match_info.clear()
        self.liste_matchs.clear()
        
    def recup_tournoi_inacheve(self):
                     
        self.tournoi_inacheve = {"nom": self.tournoi['nom'], 
                                "lieu": self.tournoi['lieu'], 
                                "dates": self.tournoi['dates'], 
                                "nombres_de_rounds": self.tournoi['nombres_de_rounds'], 
                                "description": self.tournoi['description'], 
                                "mode_de_jeu": self.tournoi['mode_de_jeu'], 
                                "id": self.tournoi['id'], 
                                "joueurs": self.tournoi['joueurs'], 
                                "resultats": self.resultats_round,
                                "statut":"tournoi non termine",
                                "round_termine":self.recup_round}
        
        data = Database()
        data.ecrire_database(self.tournoi_inacheve, "non_termines", chemin_fichier="data/non_termines.json")
   
        return self.tournoi_inacheve
    
    





 