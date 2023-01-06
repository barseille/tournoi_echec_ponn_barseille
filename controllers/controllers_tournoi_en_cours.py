from .controllers_tournois import ControllersTournois
from .controllers_joueurs import ControllersJoueurs
import json
import random
from models.match import Match



class ControllersTournoiEnCours:
    
    def fusion_tournoi_avec_joueurs(self):
        "sérialiser les tournois avec ses participants"
        
        print('        -- Liste des tournois -- \n')
        tournoi = ControllersTournois()
        tournoi.selectionner_tournoi()
        self.tournoi_en_cours = tournoi.tournoi_selectionne
        
        print('        -- Liste des joueurs -- \n')
        joueur = ControllersJoueurs()
        joueur.selectionner_participants()
        joueurs_en_cours = joueur.joueurs_selectionnes
        
        # ajouter joueurs dans tournoi
        self.tournoi_en_cours.update({"joueurs": joueurs_en_cours})
        
        
        
    def afficher_tournoi_en_cours(self):
        
        print('-'*60)
        print("             -- Informations du tournoi --")
        print('-'*60)
             
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
        self.recuperation_nb_de_rounds() 
        
        
    def recuperation_nb_de_rounds(self):

        nombres_de_rounds = self.tournoi_en_cours['nombres_de_rounds']
        
        """ Afficher tous les rounds""" 
        for i in range(nombres_de_rounds):
            self.numero_round = i + 1
            print(f"                -- ROUND {i+1}/{nombres_de_rounds} --")
            self.lancer_round_1()
            # self.sauvegarder_match()
            
            if i < nombres_de_rounds -1:     
                choix = input("Voulez vous passer au round suivant ? (o/n) : ")
                if choix != "o":
                    # self.sauvegarder_match()
                    break
  
        print("Le tournoi est terminé ! ")
        
        
    def lancer_round_1(self):
        
        # Mélanger la liste des joueurs
        random.shuffle(self.liste_des_joueurs)
        self.lancer_matchs()
        

    def lancer_matchs(self):
        
        liste_de_matchs = []
       
        # Pour chaque paire de joueurs, lancer un match
        for i in range(0, len(self.liste_des_joueurs), 2):
            self.joueur1 = self.liste_des_joueurs[i]
            self.joueur2 = self.liste_des_joueurs[i + 1]
            paire = (self.joueur1, self.joueur2)
            liste_de_matchs.append(paire)

    
        # Lancer chaque match de la liste
        for i, match in enumerate(liste_de_matchs):
            self.joueur1 = match[0]
            self.joueur2 = match[1]
 
            print('-'*60)
            print(f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :")
            print('-'*60)

            choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

            if choix == "1":
                self.joueur1["score"] += 1
                print(f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !")
     
                  
            elif choix == "2":
                self.joueur2["score"] += 1
       
                
            elif choix == "3":
                self.gagnant = random.choice([self.joueur1, self.joueur2])
                self.gagnant["score"] += 1      
      
                print(f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !")
                  
            else:
                self.joueur1["score"] += 0.5
                self.joueur2["score"] += 0.5
      
                print("Match nul !")

     
            # Réinitialiser la liste "matchs" du tournoi
            self.tournoi_en_cours['matchs'] = []
            
            # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
            for joueur in self.tournoi_en_cours['joueurs']:
                nom = joueur['nom']
                score = joueur['score']
                self.tournoi_en_cours['matchs'].append((nom, score))
                print(f"Joueur {nom} = {score}")
            

    def sauvegarder_round(self):
        pass
        










   
        
    # def creation_paire(self):
        
    #     self.liste_de_matchs = []
       
    #     for i in range(0, len(self.liste_des_joueurs), 2):
    #         self.joueur1 = self.liste_des_joueurs[i]
    #         self.joueur2 = self.liste_des_joueurs[i + 1]
    #         paire = (self.joueur1, self.joueur2)
    #         self.liste_de_matchs.append(paire)

    #     for i, match in enumerate(self.liste_de_matchs):
    #         self.joueur1 = match[0]
    #         self.joueur2 = match[1]
     
       
    
    # def lancer_match(self):
        
    #     """ recuperation de chaque match dans un tuple rangé dans une liste"""
    #     self.resultats = []
             
    #     for i, match in enumerate(self.liste_de_matchs):
    #         self.joueur1 = match[0]
    #         self.joueur2 = match[1]
           
    #         print('-'*60)
    #         print(f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2)")
    #         print('-'*60)

    #         choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

    #         if choix == "1":
    #             self.joueur1["score"] += 1
    #             self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
    #             self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
    #             print(f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !")
                    
    #         elif choix == "2":
    #             self.joueur2["score"] += 1
    #             self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
    #             self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
    #             print(f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !")
                
    #         elif choix == "3":
    #             self.gagnant = random.choice([self.joueur1, self.joueur2])
    #             self.gagnant["score"] += 1     
    #             self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
    #             self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
    #             print(f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !")
                    
    #         else:
    #             self.joueur1["score"] += 0.5
    #             self.joueur2["score"] += 0.5
    #             self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
    #             self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
    #             print("Match nul !")

        
    #         print('-'*60)
    #         print("               -- Résultat du match -- ")
    #         print('-'*60)
            
    #         for joueur in self.resultats:
    #             nom = joueur[0]
    #             score = joueur[1]
    #             print(f"Joueur {nom} = {score}")
                    
        
        
                

                
           


        
 