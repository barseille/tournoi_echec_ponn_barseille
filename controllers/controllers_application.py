from .controllers_tournois import ControllersTournois
from .controllers_joueurs import ControllersJoueurs
import json
import random

class ControllersApplication :
    
    def __init__(self):
        self.numero_round = 0

    
    def fusion_tournoi_avec_joueurs(self):
        "sérialiser les tournois avec ses participants"
        
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
        """ Sérialisation du tournoi choisi avec les joueurs choisis """
        
        with open(dossier, 'r+') as f :
            historique_tournois = json.load(f)
            historique_tournois["liste_des_tournois_en_cours"].append(tournoi_en_cours)
            f.seek(0)
            json.dump(historique_tournois, f, indent=4) 
            
            
            
    def afficher_tournoi_en_cours(self):
        
        print('-'*60)
        print("             -- Informations du tournoi --")
        print('-'*60)
        
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
        
        self.recuperation_nb_de_rounds() 
        
        
    def recuperation_nb_de_rounds(self):

        nombres_de_rounds = self.tournoi_en_cours['nombres_de_rounds']
        
        """ Afficher tous les rounds""" 
        for i in range(nombres_de_rounds):
            self.numero_round = i + 1
            print(f"                -- ROUND {i+1}/{nombres_de_rounds} --")
            self.lancer_round_1()
            self.sauvegarder_match()
            
            if i < nombres_de_rounds -1:     
                choix = input("Voulez vous passer au round suivant ? (o/n) : ")
                if choix != "o":
                    self.sauvegarder_match()
                    break
  
        print("Le tournoi est terminé ! ")
               

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
            
            self.resultats = [] 
            print('-'*60)
            print(f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :")
            print('-'*60)

            # Demander à l'utilisateur de saisir le gagnant du match ou de choisir aléatoirement
            choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

            if choix == "1":
                self.joueur1["score"] += 1
                print(f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !")
                self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
                self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
                  
            elif choix == "2":
                self.joueur2["score"] += 1
                print(f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !")
                self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
                self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
                
            elif choix == "3":
                self.gagnant = random.choice([self.joueur1, self.joueur2])
                self.gagnant["score"] += 1
               
                
                self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
                self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
                print(f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !")
                  
            else:
                self.joueur1["score"] += 0.5
                self.joueur2["score"] += 0.5
                self.resultats.append((self.joueur1['nom'], self.joueur1["score"]))
                self.resultats.append((self.joueur2['nom'], self.joueur2["score"]))
                print("Match nul !")

            
            for joueur in self.resultats:
                nom = joueur[0]
                score = joueur[1]
                print(f"Joueur {nom} = {score}")
                
 
    def lancer_round_1(self):
        
        # Mélanger la liste des joueurs
        melange = random.shuffle(self.liste_des_joueurs)
        melange == self.lancer_matchs()
        

    def sauvegarder_match(self):
        # On crée une liste vide qui va contenir les informations de chaque match
        info_match = []
        
        self.tournoi_en_cours["info_match"] = []

        # On parcourt la liste des joueurs par paire
        for i in range(0, len(self.liste_des_joueurs), 2):
        
            nom1 = self.liste_des_joueurs[i]["prenom"] + " " + self.liste_des_joueurs[i]["nom"]
            score1 = self.liste_des_joueurs[i]["score"]

            
            nom2 = self.liste_des_joueurs[i + 1]["prenom"] + " " + self.liste_des_joueurs[i + 1]["nom"]
            score2 = self.liste_des_joueurs[i + 1]["score"]

           
            info_match.append({
                                "joueur1": nom1,
                                "score1": score1,
                                "joueur2": nom2,
                                "score2": score2})

        # On ajoute la liste des informations de chaque match dans le tournoi en cours
        self.tournoi_en_cours["info_match"].append(info_match)
        self.info_match_data = self.tournoi_en_cours["info_match"]

        # On enregistre le tournoi en cours dans le fichier historique_tournois.json
        self.stocker_match_json(self.info_match_data, "historique_tournois.json")

        # On met à jour le classement et le score des joueurs dans l'historique des tournois
        self.mettre_a_jour_classement_historique_tournoi()
        self.mettre_a_jour_score_historique_tournoi()
        
        return self.tournoi_en_cours["info_match"]



            
    def stocker_match_json(self, r, dossier="historique_tournois.json"):
        " sérialiser chaque match "
            
        with open(dossier, 'r+')as f:
            historique_tournois = json.load(f)
            historique_tournois["liste_des_tournois_en_cours"].append(self.info_match_data)
            f.seek(0)
            json.dump(historique_tournois, f, indent=4)
            


    def mettre_a_jour_score_historique_tournoi(self):
        """
        Met à jour le score d'un joueur dans le fichier historique_tournoi.json
        """

        # Récupérer le tournoi en cours et la liste des joueurs du tournoi
        with open("historique_tournois.json", "r+") as f:
            tournois = json.load(f)
            tournoi_en_cours = tournois["liste_des_tournois_en_cours"][-1]
            joueurs = tournoi_en_cours["joueurs"]

        # Mettre à jour le score du joueur dans la liste des joueurs du tournoi
        for j in joueurs:
            if j["nom"] == self.joueur1["nom"] and j["prenom"] == self.joueur1["prenom"]:
                j["score"] = self.joueur1["score"]
            elif j["nom"] == self.joueur2["nom"] and j["prenom"] == self.joueur2["prenom"]:
                j["score"] = self.joueur2["score"]

        # Enregistrer les modifications dans le fichier JSON
        with open("historique_tournois.json", "w") as f:
            json.dump(tournois, f, indent=4)
       
       
    def mettre_a_jour_classement_historique_tournoi(self):
        # Récupérer le tournoi en cours et la liste des joueurs du tournoi
        with open("historique_tournois.json", "r+") as f:
            tournois = json.load(f)
            self.tournoi_en_cours = tournois["liste_des_tournois_en_cours"][-1]
            joueurs = self.tournoi_en_cours["joueurs"]

        """ 
        fonction lambda est utilisée pour définir une fonction 
        qui prend en paramètre un élément de la liste joueurs et 
        qui renvoie la valeur de la clé "score" de cet élément. 
        Cette fonction est utilisée en tant que key pour le tri de la liste joueurs.
        """
        # Trier la liste des joueurs par score décroissant
        joueurs.sort(key=lambda x: x["score"], reverse=True)

        # Mettre à jour le classement de chaque joueur
        for i, joueur in enumerate(joueurs):
            joueur["classement"] = i + 1

        # Enregistrer les modifications dans le fichier JSON
        with open("historique_tournois.json", "w") as f:
            json.dump(tournois, f, indent=4)