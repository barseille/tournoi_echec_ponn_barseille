from .controllers_tournois import ControllersTournois
from .controllers_joueurs import ControllersJoueurs
from models.match import Match
import random
import uuid
import json
from datetime import datetime




class ControllersApplication:
    
    def fusion_tournoi_avec_joueurs(self):
        "sérialiser les tournois avec ses participants"
        
        
        # génération d'un identifiant unique
        id_tournoi = str(uuid.uuid4())
        
        print('        -- Liste des tournois -- \n')
        tournoi = ControllersTournois()
        tournoi.selectionner_tournoi()
        self.tournoi_en_cours = tournoi.tournoi_selectionne
        
        
        
        print('        -- Liste des joueurs -- \n')
        joueur = ControllersJoueurs()
        joueur.selectionner_participants()
        joueurs_en_cours = joueur.joueurs_selectionnes
        
        # ajouter joueurs dans tournoi
        self.tournoi_en_cours.update({ "id": id_tournoi, "joueurs": joueurs_en_cours})
        
        
        
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
        
    def lancer_nouveau_tournoi(self):
        
        choix = input("Voulez_vous commencer le tournoi ? (o/n) : ")
        if choix != "o":
            return 
        self.recuperation_nb_de_rounds() 
        
        
    def recuperation_nb_de_rounds(self):

        nombres_de_rounds = self.tournoi_en_cours['nombres_de_rounds']
        self.liste_de_rounds = []
        
        """ Afficher tous les rounds""" 
        for i in range(nombres_de_rounds):
            self.numero_round = i + 1
            print(f"                -- ROUND {i+1}/{nombres_de_rounds} --")

    
            self.lancer_matchs()
            date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            round_info = {
                          "numero_round": i + 1,
                          "date_debut": date_debut,
                          "date_fin": date_fin,
                          "matchs": self.liste_de_matchs_infos,
                          "points": self.liste_de_matchs
                          }
            
            self.liste_de_rounds.append(round_info)
            tournoi_dict = {"liste_de_rounds": self.liste_de_rounds}
            
            if i+1 != nombres_de_rounds:
                choix = input("Voulez vous passer au round suivant ? (o/n) : ")
                if choix != "o":
                    self.tournois_inacheves()
                    break
            
        else:
            
            self.tournoi_en_cours.update(tournoi_dict)  
            tournoi_en_cours = self.tournoi_en_cours            
            self.ecrire_json(tournoi_en_cours, "historique_tournois.json")           
            self.mettre_a_jour_classement_historique_tournoi()
            self.mettre_a_jour_classement_liste_joueurs()
        
            print('-'*60)
            print("           -- Tournoi terminé -- ")
            print('-'*60)

            
    def tournois_inacheves(self):
                
            self.tournoi_inacheve = {"nom": self.tournoi_en_cours['nom'], 
                                    "lieu": self.tournoi_en_cours['lieu'], 
                                    "dates": self.tournoi_en_cours['dates'], 
                                    "nombres_de_rounds": self.tournoi_en_cours['nombres_de_rounds'], 
                                    "description": self.tournoi_en_cours['description'], 
                                    "mode_de_jeu": self.tournoi_en_cours['mode_de_jeu'], 
                                    "id": self.tournoi_en_cours['id'], 
                                    "joueurs": self.tournoi_en_cours['joueurs'], 
                                    "liste_de_rounds": self.liste_de_rounds}
        
            tournoi_inacheve = self.tournoi_inacheve
            self.sauvegarde_tournois_inacheves(tournoi_inacheve, "tournois_inacheves.json")
                    
                      
    def sauvegarde_tournois_inacheves(self, tournoi_inacheve, dossier="tournois_inacheves.json"):
        """ Sérialisation du tournoi inachevé """
        
        with open(dossier, 'r+') as f :
            tournois_inacheves = json.load(f)
            tournois_inacheves["tournois_inacheves"].append(tournoi_inacheve)
            f.seek(0)
            json.dump(tournois_inacheves, f, indent=4) 
    

    def trier_les_joueurs_par_score(self):
        self.liste_des_joueurs.sort(key=lambda x: x["score"], reverse=True)


    def lancer_matchs(self):
           
        # Mélanger la liste des joueurs
        if self.numero_round == 1:
            random.shuffle(self.liste_des_joueurs)
        else:
            self.trier_les_joueurs_par_score()
        
        self.liste_de_paire = []
        self.liste_de_matchs_infos = []
       
        # Pour chaque paire de joueurs, lancer un match
        for i in range(0, len(self.liste_des_joueurs), 2):
            self.joueur1 = self.liste_des_joueurs[i]
            self.joueur2 = self.liste_des_joueurs[i + 1]
            paire = (self.joueur1, self.joueur2)
            self.liste_de_paire.append(paire)
            
    
        # Lancer chaque match de la liste
        for i, match in enumerate(self.liste_de_paire):
            self.joueur1 = match[0]
            self.joueur2 = match[1]
                
            print('-'*60)
            print(f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :")
            print('-'*60)

            choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

            if choix == "1":
                self.joueur1["score"] += 1
                print(f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !")
                
                # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)
                  
            elif choix == "2":
                self.joueur2["score"] += 1
                print(f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !")
                
                 # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)
       
                
            elif choix == "3":
                self.gagnant = random.choice([self.joueur1, self.joueur2])
                self.gagnant["score"] += 1        
                print(f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !")

                 # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)               
                        
                  
            else:
                self.joueur1["score"] += 0.5
                self.joueur2["score"] += 0.5
                print("Match nul !")
                
                 # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)
        
           
            # Réinitialiser la liste "matchs" du tournoi
            self.liste_de_matchs = []
            
            # Pour chaque joueur du tournoi, ajouter ses informations dans la liste "matchs"
            for joueur in self.tournoi_en_cours['joueurs']:
                nom = joueur['nom']
                score = joueur['score']
                self.liste_de_matchs.append((nom, score))
                print(f"Joueur {nom} = {score}")
                
           

    def ecrire_json(self, tournoi_en_cours, dossier="historique_tournois.json"):
        """ Sérialisation du tournoi choisi avec les joueurs choisis """
        
        with open(dossier, 'r+') as f :
            historique_tournois = json.load(f)
            historique_tournois["liste_des_tournois_en_cours"].append(tournoi_en_cours)
            f.seek(0)
            json.dump(historique_tournois, f, indent=2) 
            
            
            
    def mettre_a_jour_classement_historique_tournoi(self):
    
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
            
            
            
    def mettre_a_jour_classement_liste_joueurs(self):
        
        with open("historique_tournois.json", "r") as f:
            historique_tournois = json.load(f)
        with open("liste_joueurs.json", "r") as f:
            liste_joueurs = json.load(f)

        for tournoi in historique_tournois["liste_des_tournois_en_cours"]:
            for joueur_tournoi in tournoi["joueurs"]:
                for joueur_liste in liste_joueurs["liste_joueurs"]:
                    if joueur_tournoi["nom"] == joueur_liste["nom"] and joueur_tournoi["prenom"] == joueur_liste["prenom"]:
                        joueur_liste["classement"] = joueur_tournoi["classement"]

        with open("liste_joueurs.json", "w") as f:
            json.dump(liste_joueurs, f, indent=4)  