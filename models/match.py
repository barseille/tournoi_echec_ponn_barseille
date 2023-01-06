

import json
import random

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
      

    def __str__(self):
        return f"{self.joueur1['prenom']} {self.joueur1['nom']} VS {self.joueur2['prenom']} {self.joueur2['nom']}"
   
       
    def recuperer_paire(self):
        return self.joueur1, self.joueur2   
       
       
       
       
       
       
       
       
       
       
       
        
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

    # def serialiser(self):
    #     """Sérialise les données du match"""
    #     match_data = {
    #         'joueur1': self.joueur1,
    #         'joueur2': self.joueur2,
           
    #     }
        
    #     with open('match.json', 'w') as f:
    #         json.dump(match_data, f, indent=4)
    
    # def stocker_un_match(self):
    #     """ 
    #     tuple contenant deux listes, chacune contenant deux éléments : 
    #     un joueur et un score 
    #     """
        
    #     pass
    
    # def stocker_liste_de_matchs(self):
    #     """ matchs doivent être stockés sous forme de liste"""
    #     pass
    #     # match = ([self.joueur1["nom"], self.joueur1["score"]], [self.joueur2["nom"], self.joueur2["score"]])
    #     # matchs.append(match)
    






