from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_menu_joueur import ViewsMenuJoueur
from .controllers_joueurs import ControllersJoueurs
from .controllers_tournois import ControllersTournois
from models.tournoi import Tournoi
from models.round import Round
from models.match import Match
from database.database import Database

import random
import uuid
import json
from datetime import datetime
from views.base_views import BaseViews


class ControllersBase():
    
    def __init__(self):
        self.joueur1 = None
        self.joueur2 = None
        self.controllers_joueurs = ControllersJoueurs()
        self.controllers_tournois = ControllersTournois()
        self.views_menu_joueur = ViewsMenuJoueur()
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.paires_precedentes = []
        self.match = Match(self.joueur1, self.joueur2)
        self.match_info = []
        self.resultats_round = {}
        self.liste_matchs = []
        
       
        
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
        
        # self.joueur1 = self.tournoi["joueurs"][0]
        # self.joueur2 = self.tournoi["joueurs"][1]

  
    def lancer_round(self):
        
        self.tournoi["resultats"] = []
        
        for i in range(self.tournoi["nombres_de_rounds"]):
            msg = f"                   -- ROUND {i + 1}/{self.tournoi['nombres_de_rounds']} --"
            titre = BaseViews()
            titre.presentation(msg)

            # Ajouter le temps de début du round
            debut_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Mélanger les joueurs pour le premier round
            if i == 0: 
                random.shuffle(self.tournoi["joueurs"])
            # Trier les joueurs par score et par ordre alphabétique
            else:    
                self.tournoi["joueurs"].sort(key=lambda x: x["score"], reverse=True)
            
            # Lancer les matchs pour le round    
            self.lancer_match(self.tournoi["joueurs"])
            
            # Ajouter le temps de fin du round
            fin_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Ajouter les résultats du round au dictionnaire resultats_round
            self.resultats_round[f"Round {i+1}"] = {"matchs": self.match_info.copy(),
                                                    "debut": debut_round,
                                                    "fin": fin_round,
                                                    "scores_joueurs": self.liste_matchs.copy()}
            
            # Vider la liste des matchs pour le prochain round
            self.match_info.clear()
            self.liste_matchs.clear()
            
            # Demander à l'utilisateur s'il veut continuer
            if i < self.tournoi["nombres_de_rounds"] - 1:
                while True:
                    reponse = input("Voulez_vous continuer le prochain round ? (o/n) : ")
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        self.tournoi["resultats"].append(self.resultats_round)
                        self.tournoi["statut"] = "tournoi non termine"
                  
                        terminer = BaseViews()
                        terminer.affichage_termine() 
                        self.sauvergarde()
                        return
                    else:
                        erreur = BaseViews()
                        erreur.affichage_erreur_choix()                
                        
        self.tournoi["resultats"].append(self.resultats_round)    
        self.tournoi["statut"] = "tournoi termine" 
        self.sauvergarde()
        terminer = BaseViews()
        terminer.affichage_termine()  
        

    def lancer_match(self, joueurs):
  
        paire = self.match.generer_paire(joueurs)
        self.match.melanger_joueurs(joueurs)
        
        while paire and paire in self.paires_precedentes:
            self.match.melanger_joueurs(joueurs)
            paire = self.match.generer_paire(joueurs)    
            
        self.paires_precedentes.append(paire)
     
        for i, j in enumerate(paire):
            match_joueurs = f"Match {i+1} : {j[0]['prenom']} {j[0]['nom']} VS {j[1]['prenom']} {j[1]['nom']}"
            self.affichage_msg(match_joueurs)
            
            while True:     
                choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2 et 3 pour égalité) : ")        
                try:           
                    if choix == "1":
                        j[0]["score"] += 1
                        self.affichage_msg(f"{j[0]['prenom']} {j[0]['nom']} a gagné\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    elif choix == "2":
                        j[1]["score"] += 1
                        self.affichage_msg(f"{j[1]['prenom']} {j[1]['nom']} a gagné\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    elif choix == "3":
                        j[0]["score"] += 0.5
                        j[1]["score"] += 0.5
             
                        self.affichage_msg("Match nul !\n")
                        match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(match_joueurs)
                        break
                    
                    else:
                        self.affichage_msg("Choix invalide. Veuillez taper 1, 2, 3")          
                except ValueError:
                    self.affichage_msg("Choix invalide. Veuillez taper 1, 2, 3")
                    
        # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
        for joueur in self.tournoi["joueurs"]:
            nom = joueur['nom']
            score = joueur['score']
            self.liste_matchs.append((nom, score))          
        

    def affichage_msg(self,msg):         
        # Afficher un message 
        affiche = BaseViews()
        affiche.afficher_msg(msg)  
        
    def sauvergarde(self):
        data = Database()
        data.ecrire_database(self.tournoi, "liste_des_tournois", chemin_fichier='data/historique_tournois.json')
        

          














       
        
#     def lancer_nouveau_tournoi(self):
        
#         choix = input("Voulez-vous commencer le tournoi ? (o/n) : ")
#         if choix != "o":
#             return 
#         self.recuperation_nb_de_rounds() 
        
        
#     def recuperation_nb_de_rounds(self):
        
#         nombres_de_rounds = self.tournoi['nombres_de_rounds']
#         self.liste_de_rounds = []
        
#         """ Afficher tous les rounds""" 
#         for i in range(nombres_de_rounds):
            
#             self.numero_round = i + 1
#             msg = f"                -- ROUND {i+1}/{nombres_de_rounds} --"
#             affiche = BaseViews()
#             affiche.afficher_msg(msg)   
            
#             # Mélanger la liste des joueurs
#             if self.numero_round == 1:
#                 random.shuffle(self.liste_des_joueurs)
#             else:
#                 self.trier_les_joueurs_par_score()
                

 
#             self.lancer_matchs()
            
#             date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#             date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            
#             round_info = {"numero_round": i + 1,
#                           "date_debut": date_debut,
#                           "date_fin": date_fin,
#                           "matchs": self.liste_matchs_infos,
#                           "points": self.liste_matchs}
            
#             self.liste_de_rounds.append(round_info)
#             tournoi_dict = {"liste_de_rounds": self.liste_de_rounds}
            
#             if i+1 != nombres_de_rounds:
#                 choix = input("Voulez vous passer au round suivant ? (o/n) : ")
#                 if choix != "o":
#                     self.tournois_inacheves()
#                     break
            
#         else:
            
#             self.tournoi.update(tournoi_dict)  
#             tournoi_en_cours = self.tournoi            
#             self.ecrire_json(tournoi_en_cours, "data/historique_tournois.json")           
#             self.mettre_a_jour_classement_historique_tournoi()
#             self.mettre_a_jour_classement_score_liste_joueurs()
        
#         tournoi_terminé = BaseViews()
#         tournoi_terminé.affichage_tournoi_termine()
            
#     def trier_les_joueurs_par_score(self):
        
#         self.liste_des_joueurs.sort(key=lambda x: x["score"], reverse=True)
        

#     def lancer_matchs(self):
        
#         self.liste_de_paires = []
#         self.liste_matchs_infos = []
#         self.rencontres = {}
               
#         # Pour chaque paire de joueurs, lancer un match
#         for i in range(0, len(self.liste_des_joueurs), 2):
#             self.joueur1 = self.liste_des_joueurs[i]      
#             self.joueur2 = self.liste_des_joueurs[i + 1]
#             paire = (self.joueur1, self.joueur2)
#             self.liste_de_paires.append(paire)
   
#         # Lancer chaque match de la liste
#         for i, match in enumerate(self.liste_de_paires):
#             self.joueur1 = match[0]
#             self.joueur2 = match[1] 
#             id_joueur1 = self.joueur1["id"]
#             id_joueur2 = self.joueur2["id"] 
#             self.rencontres[id_joueur1] = []
#             self.rencontres[id_joueur2] = []     
#             self.rencontres[id_joueur1].append(id_joueur2)
#             self.rencontres[id_joueur2].append(id_joueur1)
            
#             joueur1_gagne = f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !"
#             joueur2_gagne = f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !"         
#             match_nul = "Match nul !"
            
  
#             affichage = f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :"
#             affichage_joueur = BaseViews()
#             affichage_joueur.presentation(affichage)

#             choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

#             if choix == "1":
#                 self.joueur1["score"] += 1
#                 affiche = BaseViews()
#                 affiche.afficher_msg(joueur1_gagne)
                
#                 # Ajouter les informations sur le match à la liste de matchs
#                 match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#                 self.liste_matchs_infos.append(match_dict)
                
                
#             elif choix == "2":
#                 self.joueur2["score"] += 1
#                 affiche = BaseViews()
#                 affiche.afficher_msg(joueur2_gagne)
                
#                 # Ajouter les informations sur le match à la liste de matchs
#                 match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#                 self.liste_matchs_infos.append(match_dict)
    
                
#             elif choix == "3":
#                 self.gagnant = random.choice([self.joueur1, self.joueur2])
#                 self.gagnant["score"] += 1 
#                 joueur_aleatoire = f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !"
                
#                 affiche = BaseViews()
#                 affiche.afficher_msg(joueur_aleatoire)       
           

#                 # Ajouter les informations sur le match à la liste de matchs
#                 match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#                 self.liste_matchs_infos.append(match_dict)               
                                    
#             else:
#                 self.joueur1["score"] += 0.5
#                 self.joueur2["score"] += 0.5
#                 affiche = BaseViews()
#                 affiche.afficher_msg(match_nul)  
                
#                 # Ajouter les informations sur le match à la liste de matchs
#                 match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
#                 self.liste_matchs_infos.append(match_dict)

#         # Réinitialiser la liste "matchs" du tournoi
#         self.liste_matchs = []
        
#         # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
#         for joueur in self.tournoi['joueurs']:
#             nom = joueur['nom']
#             score = joueur['score']
#             self.liste_matchs.append((nom, score))
#             msg = f"Joueur {nom} = {score}"
#             affichage_score = BaseViews()
#             affichage_score.afficher_msg(msg)
            
                
#     def tournois_inacheves(self):
                       
#         self.tournoi_inacheve = {"nom": self.tournoi['nom'], 
#                                 "lieu": self.tournoi['lieu'], 
#                                 "dates": self.tournoi['dates'], 
#                                 "nombres_de_rounds": self.tournoi['nombres_de_rounds'], 
#                                 "description": self.tournoi['description'], 
#                                 "mode_de_jeu": self.tournoi['mode_de_jeu'], 
#                                 "id": self.tournoi['id'], 
#                                 "joueurs": self.tournoi['joueurs'], 
#                                 "liste_de_rounds": self.liste_de_rounds}
    
#         tournoi_inacheve = self.tournoi_inacheve
#         self.sauvegarde_tournois_inacheves(tournoi_inacheve, "data/tournois_inacheves.json")
                    
                      
#     def sauvegarde_tournois_inacheves(self, tournoi_inacheve, dossier="data/tournois_inacheves.json"):
#         """ Sérialisation du tournoi inachevé """
        
#         with open(dossier, 'r+') as f :
#             tournois_inacheves = json.load(f)
#             tournois_inacheves["tournois_inacheves"].append(tournoi_inacheve)
#             f.seek(0)
#             json.dump(tournois_inacheves, f, indent=4) 

        

#     def ecrire_json(self, tournoi_en_cours, dossier="data/historique_tournois.json"):
#         """ Sérialisation du tournoi choisi avec les joueurs choisis """
        
#         with open(dossier, 'r+') as f :
#             historique_tournois = json.load(f)
#             historique_tournois["liste_des_tournois_en_cours"].append(tournoi_en_cours)
#             f.seek(0)
#             json.dump(historique_tournois, f, indent=4) 
            
            
            
#     def mettre_a_jour_classement_historique_tournoi(self):
    
#         with open("data/historique_tournois.json", "r+") as f:
#             tournois = json.load(f)
#             self.tournoi = tournois["liste_des_tournois_en_cours"][-1]
#             joueurs = self.tournoi["joueurs"]

#         """ 
#         fonction lambda est utilisée pour définir une fonction 
#         qui prend en paramètre un élément de la liste joueurs et 
#         qui renvoie la valeur de la clé "score" de cet élément. 
#         Cette fonction est utilisée en tant que key pour le tri de la liste joueurs.
#         """
#         # Trier la liste des joueurs par score décroissant
#         joueurs.sort(key=lambda x: x["score"], reverse=True)

#         # Mettre à jour le classement de chaque joueur
#         for i, joueur in enumerate(joueurs):
#             joueur["classement"] = i + 1

#         # Enregistrer les modifications dans le fichier JSON
#         with open("data/historique_tournois.json", "w") as f:
#             json.dump(tournois, f, indent=4)
            
            
            
#     def mettre_a_jour_classement_score_liste_joueurs(self):
        
#         with open("data/historique_tournois.json", "r") as f:
#             historique_tournois = json.load(f)
#         with open("data/liste_joueurs.json", "r") as f:
#             liste_joueurs = json.load(f)

#         for tournoi in historique_tournois["liste_des_tournois_en_cours"]:
#             for joueur_tournoi in tournoi["joueurs"]:
#                 for joueur_liste in liste_joueurs["liste_joueurs"]:
#                     if joueur_tournoi["nom"] == joueur_liste["nom"] and joueur_tournoi["prenom"] == joueur_liste["prenom"]:
#                         joueur_liste["classement"] = joueur_tournoi["classement"]
#                         # joueur_liste["score"] = joueur_tournoi["score"]

#         with open("data/liste_joueurs.json", "w") as f:
#             json.dump(liste_joueurs, f, indent=4)  
            
            
# import json

# def charger_et_ecrire_json(objet_json, chemin_fichier):
#     """ Chargement d'un objet JSON depuis un fichier, modification de l'objet,
#         puis écriture de l'objet modifié dans le même fichier """
#     try:
#         with open(chemin_fichier, 'r+') as f:
#             contenu_fichier = json.load(f)
            
#     except FileNotFoundError:
#         # Si le fichier n'existe pas, on crée un objet JSON vide
#         contenu_fichier = {}

#     contenu_fichier.update(objet_json)

#     try:
#         with open(chemin_fichier, 'w') as f:
#             json.dump(contenu_fichier, f, indent=4)
#     except:
#         print("Erreur lors de l'écriture du fichier JSON")

#     return contenu_fichier
            
            
            
