from .controllers_tournois import ControllersTournois
from .controllers_joueurs import ControllersJoueurs
import json
import random

class ControllersApplication :

    
    def fusion_tournoi_avec_joueurs(self):
        "sérialiser les tournois complets"
        
        print('        -- Liste des tournois -- \n')
        tournoi = ControllersTournois()
        tournoi.selectionner_tournoi()
        tournoi_en_cours = tournoi.tournoi_selectionne
        
        print('        -- Liste des joueurs -- \n')
        joueur = ControllersJoueurs()
        joueur.selectionner_participants()
        joueurs_en_cours = joueur.joueurs_selectionnes
        
        # ajouter joueurs dans tournoi
        tournoi_en_cours.update({"joueurs": joueurs_en_cours})
        
        self.ecrire_json(tournoi_en_cours, "historique_tournois.json")

        
    def ecrire_json(self, tournoi_en_cours, dossier="historique_tournois.json"):
        """ sérialisation du tournoi choisi pour le joueur"""
        
        with open(dossier, 'r+') as f :
            historique_tournois = json.load(f)
            historique_tournois["liste_des_tournois_en_cours"].append(tournoi_en_cours)
            f.seek(0)
            json.dump(historique_tournois, f, indent=4) 
            
            
            
    def afficher_tournoi_en_cours(self):
        
        print("       -- Informations du tournoi --\n")
        
        with open("historique_tournois.json", "r") as f:
            tournois = json.load(f)
            self.tournoi_en_cours = tournois["liste_des_tournois_en_cours"][-1]
            
        # Afficher les informations du tournoi
        print(f"Nom du tournoi : {self.tournoi_en_cours['nom']}")
        print(f"Lieu du tournoi : {self.tournoi_en_cours['lieu']}")
        print(f"Dates du tournoi : {self.tournoi_en_cours['dates']}")
        print(f"Nombre de rounds : {self.tournoi_en_cours['nombres_de_rounds']}")
        print(f"Description : {self.tournoi_en_cours['description']}")
        print(f"Mode de jeu : {self.tournoi_en_cours['mode_de_jeu']}\n")
        

        self.liste_des_joueurs = []
        # Afficher la liste des joueurs du tournoi
        print("Liste des joueurs :")
        for joueur in self.tournoi_en_cours["joueurs"]:
            print(f" - {joueur['prenom']} {joueur['nom']}")
            self.liste_des_joueurs.append(joueur)
            

    def lancer_tournoi(self):
        
        choix = input("Voulez_vous commencer le tournoi ? (o/n) : ")
        if choix != "o":
            return 

        nombres_de_rounds = self.tournoi_en_cours['nombres_de_rounds']
      
        """ Afficher tous les rounds""" 
        for i in range(nombres_de_rounds):
            print(f"            -- Round {i+1}/{nombres_de_rounds} --")
            self.lancer_round()

    def lancer_round(self):
        # Mélanger la liste des joueurs
        random.shuffle(self.liste_des_joueurs)
        
        liste_de_matchs = []

        # Pour chaque paire de joueurs, lancer un match
        for i in range(0, len(self.liste_des_joueurs), 2):
            self.joueur1 = self.liste_des_joueurs[i]
            self.joueur2 = self.liste_des_joueurs[i + 1]
            paire = (self.joueur1, self.joueur2)
            liste_de_matchs.append(paire)
            
        # Lancer chaque match de la liste
        for match in liste_de_matchs:
            self.joueur1 = match[0]
            self.joueur2 = match[1]
            self.choisir_gagnant()
         

    def choisir_gagnant(self):
        """
        Demande à l'utilisateur de choisir le gagnant d'un match 
        entre deux joueurs ou de choisir aléatoirement.
        """

        # self.resultats = []
        
        # Afficher les informations des joueurs
        print(f"       -- {self.joueur1['prenom']} {self.joueur1['nom']} VS {self.joueur2['prenom']} {self.joueur2['nom']} --\n")
        print(f"Joueur 1: {self.joueur1['prenom']} {self.joueur1['nom']}")
        print(f"Joueur 2: {self.joueur2['prenom']} {self.joueur2['nom']}")

        # Demander à l'utilisateur de saisir le gagnant du match ou de choisir aléatoirement
        choix = input("Choisissez le gagnant du match (1 pour joueur 1, 2 pour joueur 2 ou 3 pour aléatoire) : ") 

        if choix == "1":
            self.joueur1["score"] += 1
            print(f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !\n")
            self.mettre_a_jour_score_json(self.joueur1)
            # self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
            # self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
            
    
        elif choix == "2":
            self.joueur2["score"] += 1
            print(f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !\n")
            self.mettre_a_jour_score_json(self.joueur2)
            # self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
            # self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
          
            
            
        elif choix == "3":
            self.gagnant = random.choice([self.joueur1, self.joueur2])
            self.gagnant["score"] += 1
            print(f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !\n")
            self.mettre_a_jour_score_json(self.gagnant)
            # self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
            # self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
           
            
        else:
            self.joueur1["score"] += 0.5
            self.joueur2["score"] += 0.5
            self.mettre_a_jour_score_json(self.joueur1)
            self.mettre_a_jour_score_json(self.joueur2)
            print("Match nul !")
            # self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
            # self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
            
        print("Score des joueurs : ")   
        # for joueur in self.resultats:
        #     nom, score = joueur
        #     print(f"joueur {nom} = {score}")
 
        for i, joueur in enumerate(self.liste_des_joueurs):    
            print(f"Joueur {i+1} : {joueur['nom']} - Score : {joueur['score']}")
   
            

    def mettre_a_jour_score_json(self, joueur):
        """
        Met à jour le score d'un joueur dans le fichier JSON.
        """
        # Récupérer le tournoi en cours et la liste des joueurs du tournoi
        with open("historique_tournois.json", "r") as f:
            tournois = json.load(f)
            tournoi_en_cours = tournois["liste_des_tournois_en_cours"][-1]
            joueurs = tournoi_en_cours["joueurs"]
        
        # Mettre à jour le score du joueur dans la liste des joueurs du tournoi
        for j in joueurs:
            if j["nom"] == joueur["nom"] and j["prenom"] == joueur["prenom"]:
                j["score"] = joueur["score"]
                break
        
        # Enregistrer les modifications dans le fichier JSON
        with open("historique_tournois.json", "w") as f:
            json.dump(tournois, f, indent=4)
 