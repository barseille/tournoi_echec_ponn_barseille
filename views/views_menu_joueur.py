import json
import random

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs',
    'Retour'
)


class ViewsMenuJoueur:
    
    liste_des_joueurs = [] 
       
    def afficher_menu_joueur(self):
        print("-"*60) 
        print("                -- Menu Joueur --")  
        print("-"*60) 

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        print('-'*60)
        print("                -- Création Joueur --")
        print('-'*60)
    
    
    def afficher_des_joueurs(self):
        """ désérialisation la liste des joueurs """
        
        print('-'*60)
        print('               -- Liste des joueurs --')
        print('-'*60)
        
           
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
            
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Genre : {joueur['genre']} - Classement : {joueur['classement']}")
            print(f"                Classement : {joueur['classement']}")
            
            
    def trier_joueurs_par_score(self):
        
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        print('-'*60)
        print('              -- Classement par score -- ') 
        print('-'*60) 
         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
            
 
    def selectionner_participants(self):
    
        with open("data/liste_joueurs.json", "r") as f:                
            joueurs_data = json.load(f)
                
            # Récupérer la liste des joueurs
            liste_joueurs = joueurs_data['liste_joueurs']
            
            for i, joueur in enumerate(liste_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")     
            
            # Demander à l'utilisateur combien de joueurs il souhaite sélectionner
            nombre_joueurs = 8
            print(f"Sélectionnez {nombre_joueurs} joueurs :")
            
            i = 1
            while i <= nombre_joueurs:
                try:
                    choix_joueur = int(input("Choisissez un joueur : "))
                    joueur_selectionne = liste_joueurs[choix_joueur - 1]
                    
                    # Vérifier si le joueur a déjà été sélectionné
                    if joueur_selectionne in self.liste_des_joueurs:
                        print("Ce joueur a déjà été sélectionné. Veuillez en sélectionner un autre.")
                    else:
                        self.liste_des_joueurs.append(joueur_selectionne)
                        print("Joueur ajouté !")
                        i += 1
                except ValueError:
                    print("Veuillez entrer un nombre entier valide")
                    
            print('-'*60)
            print("         -- Liste des joueurs sélectionnés --")
            print('-'*60)
            
            for i, joueur in enumerate(self.liste_des_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")
                
        return self.liste_des_joueurs
    
    
    
    def associer_joueurs(self):
  
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
                
        return self.liste_de_matchs_infos
        
        
        
