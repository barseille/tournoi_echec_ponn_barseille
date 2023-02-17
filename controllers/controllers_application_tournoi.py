from views.views_tournoi_existant import ViewsTournoiExistant
import json
import random
from datetime import datetime
from views.base_views import BaseViews



class ControllersApplicationTournoi():
    
    def recuperation_tournois_existant(self):

        while True:
                      
            tournoi = ViewsTournoiExistant()
            tournoi.chercher_tournois_existant()
            if not tournoi.tournoi_selectionne:
                break
            self.tournoi_selectionne = tournoi.tournoi_selectionne 
           
            self.liste_des_joueurs = []
            
            for joueur in self.tournoi_selectionne["joueurs"]:
                self.liste_des_joueurs.append(joueur)
                
            self.nb_rounds_effectues = len(self.tournoi_selectionne["liste_de_rounds"])         
            self.nombre_de_rounds_restants = self.tournoi_selectionne["nombres_de_rounds"] - self.nb_rounds_effectues

            while True:
                try:
                    choix = input("Souhaitez-vous continuer ce tournoi (o/n) ? ")
                    if choix == "o":    
                        self.continuer_tournoi()
                        break
                    elif choix == "n":
                        return
                    else:
                        affiche = BaseViews()
                        affiche.affichage_erreur()
                    
                    
                except IndexError:
                    affiche = BaseViews()
                    affiche.affichage_erreur_numero()
            break
             
                
       
       
    def trier_les_joueurs_par_score(self):
        
        self.liste_des_joueurs.sort(key=lambda x: x["score"], reverse=True)
   
           
    def continuer_tournoi(self):
        
        for i in range(self.nombre_de_rounds_restants):
            affiche_round = f"         -- ROUND {i + 1 + self.nb_rounds_effectues}/{self.tournoi_selectionne['nombres_de_rounds']} --"
            affiche = BaseViews()
            affiche.afficher_msg(affiche_round)
            
            # lancer = ControllersApplication()
            # lancer.lancer_matchs()
            self.lancer_matchs()
            
            date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            date_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            self.liste_de_rounds = {
                    "numero_round": i + 1+ self.nb_rounds_effectues,
                    "date_debut": date_debut,
                    "date_fin": date_fin,
                    "matchs": self.liste_de_matchs_infos,
                    "points": self.liste_de_matchs
                    }
    
            self.tournoi_selectionne['liste_de_rounds'].append(self.liste_de_rounds)
            if i + 1 != self.nombre_de_rounds_restants:
                
                choix = input("Voulez vous passer au round suivant ? o(oui) ou taper une touche pour quitter : ")
                
                if choix != "o":

                    with open("data/tournois_inacheves.json", "r+") as f:
                        tournoi_selectionne = json.load(f)
                        tournoi_selectionne["tournois_inacheves"].append(self.tournoi_selectionne)
                        f.seek(0)
                        json.dump(tournoi_selectionne, f, indent=4)
                        
                    self.effacer_tournoi_termine()
                    break
                
        else:
            
            with open("data/historique_tournois.json", "r+") as f:
                tournoi_fini = json.load(f)
                tournoi_fini["liste_des_tournois_en_cours"].append(self.tournoi_selectionne)
                f.seek(0)
                json.dump(tournoi_fini, f, indent=4)
 
            self.effacer_tournoi_termine()

        
        termine = BaseViews()
        termine.affichage_tournoi_termine()
           
        
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
            
            
            joueur1_gagne = f"Résultat du match : {self.joueur1['prenom']} {self.joueur1['nom']} a gagné !"
            joueur2_gagne = f"Résultat du match : {self.joueur2['prenom']} {self.joueur2['nom']} a gagné !"         
            match_nul = "Match nul !"
            
    
        # Lancer chaque match de la liste
        for i, match in enumerate(self.liste_de_paire):
            self.joueur1 = match[0]
            self.joueur2 = match[1]
                
            affichage = f"Match n°{i + 1} : {self.joueur1['prenom']} {self.joueur1['nom']} (J1) VS {self.joueur2['prenom']} {self.joueur2['nom']} (J2) :"
            affichage_joueur = BaseViews()
            affichage_joueur.presentation(affichage)

            choix = input("Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité ou 3 pour aléatoire) : ") 

            if choix == "1":
                self.joueur1["score"] += 1
                affiche = BaseViews()
                affiche.afficher_msg(joueur1_gagne)
                
                # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)
                
            elif choix == "2":
                self.joueur2["score"] += 1
                affiche = BaseViews()
                affiche.afficher_msg(joueur2_gagne)
                
                # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)
    
                
            elif choix == "3":
                self.gagnant = random.choice([self.joueur1, self.joueur2])
                self.gagnant["score"] += 1  
                joueur_aleatoire = f"Résultat du match : {self.gagnant['prenom']} {self.gagnant['nom']} a gagné aléatoirement !"
      
                affiche = BaseViews()
                affiche.afficher_msg(joueur_aleatoire)  
                
                # Ajouter les informations sur le match à la liste de matchs
                match_dict = {'joueur1': self.joueur1['nom'], 'joueur2': self.joueur2['nom'], 'score': f"{self.joueur1['score']} - {self.joueur2['score']}"}
                self.liste_de_matchs_infos.append(match_dict)               
                        
                
            else:
                self.joueur1["score"] += 0.5
                self.joueur2["score"] += 0.5
                affiche = BaseViews()
                affiche.afficher_msg(match_nul)  
                
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
            msg = f"Joueur {nom} = {score}"
            affichage_score = BaseViews()
            affichage_score.afficher_msg(msg)
                
                
    def effacer_tournoi_termine(self):
        
        # Supprimer le tournoi terminé de la liste des tournois inachevés
        with open("data/tournois_inacheves.json") as f:
            data = json.load(f)
            
        # Boucle pour trouver le tournoi
        for i, tournoi in enumerate(data["tournois_inacheves"]):
            if tournoi["nom"] == self.tournoi_selectionne["nom"]:
                
                # Supprimer le tournoi de la liste
                del data["tournois_inacheves"][i]
                break

        with open("data/tournois_inacheves.json", "w") as f:
            json.dump(data, f, indent=4)
            
            
