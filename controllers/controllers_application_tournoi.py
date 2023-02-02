from .controllers_application import ControllersApplication
import json
import random
from datetime import datetime

class ControllersApplicationTournoi:

    def recuperation_tournois_existant(self):
        
        self.liste_des_joueurs = []
        
        with open("tournois_inacheves.json", "r") as f:
            data = json.load(f)
            i = 1
            for i, tournoi in enumerate(data["tournois_inacheves"]):
                print(f'{i + 1}. Nom du tournoi: {tournoi["nom"]} - Dates: {tournoi["dates"]}')
                i += 1

        while True:
                
            choix_tournoi = int(input("Quel tournoi souhaitez-vous continuer (numéro index) ? ")) 
            self.tournoi_selectionne = data["tournois_inacheves"][choix_tournoi-1]
            
            print('-'*60)
            print("            -- Informations du tournoi --")
            print('-'*60)   
            print(f'Nom du tournoi : {self.tournoi_selectionne["nom"]}')
            print(f'Lieu : {self.tournoi_selectionne["lieu"]}')
            print(f'Dates : {self.tournoi_selectionne["dates"]}')
            print(f'Description : {self.tournoi_selectionne["description"]}')
            print(f'Mode de jeu : {self.tournoi_selectionne["mode_de_jeu"]}')     
            print('-'*60)
            print("                   -- Joueurs --")
            print('-'*60)
            
            for joueur in self.tournoi_selectionne["joueurs"]:
                print(f'{joueur["prenom"]} {joueur["nom"]}')
                self.liste_des_joueurs.append(joueur)
                
            self.nb_rounds_effectues = len(self.tournoi_selectionne["liste_de_rounds"]) 
            print(f"Nombre de rounds effectués : {self.nb_rounds_effectues} Round(s)")
            
            self.nombre_de_rounds_restants = self.tournoi_selectionne["nombres_de_rounds"] - self.nb_rounds_effectues
            print(f"Nombre de rounds restants : {self.nombre_de_rounds_restants} Round(s)")
            
            choix = input("Souhaitez-vous continuer ce tournoi (o/n) ? ")
            if choix == "o":
                self.continuer_tournoi()
                # print(self.tournoi_selectionne)
 
                break
            elif choix == "n":
                # code pour retourner à l'accueil
                break
            else:
                print("Veuillez entrer 'oui' ou 'non'")
            break
       
       
    def trier_les_joueurs_par_score(self):
        
        self.liste_des_joueurs.sort(key=lambda x: x["score"], reverse=True)
   
       
        
    def continuer_tournoi(self):
        
        self.liste_de_rounds = []
        
        for i in range(self.nombre_de_rounds_restants):
            print(f"         -- ROUND {i + 1 + self.nb_rounds_effectues}/{self.tournoi_selectionne['nombres_de_rounds']} --")
            
            self.recuperer_match_termines()
            date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            round_info = {
                    "numero_round": i + 1+ self.nb_rounds_effectues,
                    "date_debut": date_debut,
                    "date_fin": date_fin,
                    "matchs": self.liste_de_matchs_infos,
                    "points": self.liste_de_matchs
                    }
    
            self.liste_de_rounds.append(round_info)
            # tournoi_dict = {"liste_de_rounds": self.liste_de_rounds}
            
            if i + 1 != self.nombre_de_rounds_restants:
                
                choix = input("Voulez vous passer au round suivant ? (o/n) : ")
                
                if choix != "o":
                    
                    self.tournoi_selectionne['liste_de_rounds'].append(self.liste_de_rounds)
                    
                    with open("tournois_inacheves.json", "r+") as f:
                        tournoi_en_cours = json.load(f)
                        tournoi_en_cours["tournois_inacheves"].append(self.tournoi_selectionne)
                        f.seek(0)
                        json.dump(tournoi_en_cours, f, indent=4)
                        

                    self.effacer_tournoi_termine()
                    break
                
        else:
            
            self.tournoi_selectionne['liste_de_rounds'].append(self.liste_de_rounds)
            
            with open("historique_tournois.json", "r+") as f:
                tournoi_fini = json.load(f)
                tournoi_fini["liste_des_tournois_en_cours"].append(self.tournoi_selectionne)
                f.seek(0)
                json.dump(tournoi_fini, f, indent=4)
            
            # self.tournoi_selectionne.update(self.liste_de_rounds)
            # tournoi_en_cours = self.tournoi_selectionne 
            # sauvegarde= ControllersApplication()           
            # sauvegarde.ecrire_json(tournoi_en_cours, "historique_tournois.json")
            self.effacer_tournoi_termine()
            
            print('-'*60)
            print("                -- Tournoi terminé -- ")
            print('-'*60)
            
            
            
            
            
    def recuperer_match_termines(self):
                
 
        # liste_de_matchs_finis = []
        # paires_jouees = []
        # joueurs_disponibles = []
        
        # # Récupérer les matchs finis
        # for round in self.tournoi_selectionne['liste_de_rounds']:
        #     liste_de_matchs_finis.append(round["matchs"])
        
        # # Enregistrer les paires de joueurs qui ont déjà joué    
        # for match in liste_de_matchs_finis[0]:
        #     self.joueur1 = match['joueur1']
        #     self.joueur2 = match['joueur2']
        #     paires_jouees.append((self.joueur1, self.joueur2))
        
        # # Trouver les paires de joueurs disponibles
        # for self.joueur1 in self.liste_des_joueurs:
        #     for self.joueur2 in self.liste_des_joueurs:
        #         if (self.joueur1, self.joueur2) not in paires_jouees and (self.joueur2, self.joueur1) not in paires_jouees:
        #             joueurs_disponibles.append((self.joueur1, self.joueur2))
        
        # # Choisir aléatoirement une paire de joueurs disponibles et lancer un match  
        # self.joueur1, self.joueur2 = random.choice(joueurs_disponibles)
        self.lancer_matchs()
        
        
    def lancer_matchs(self):
        
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
            for joueur in self.tournoi_selectionne['joueurs']:
                nom = joueur['nom']
                score = joueur['score']
                self.liste_de_matchs.append((nom, score))
                print(f"Joueur {nom} = {score}")
                
                
    def effacer_tournoi_termine(self):
        
        # Supprimer le tournoi terminé de la liste des tournois inachevés
        with open("tournois_inacheves.json") as f:
            data = json.load(f)
            
        # Boucle pour trouver le tournoi
        for i, tournoi in enumerate(data["tournois_inacheves"]):
            if tournoi["nom"] == self.tournoi_selectionne["nom"]:
                
                # Supprimer le tournoi de la liste
                del data["tournois_inacheves"][i]
                break

        with open("tournois_inacheves.json", "w") as f:
            json.dump(data, f, indent=4)
            
            
            
    def sauvegarde_round_termine(self, tournoi_inacheve, dossier="tournois_inacheves.json"):
        """ Sérialisation du tournoi inachevé """
        
        with open(dossier, 'r+') as f :
            tournois_inacheves = json.load(f)
            tournois_inacheves["tournois_inacheves"].append(tournoi_inacheve)
            f.seek(0)
            json.dump(tournois_inacheves, f, indent=4) 
        