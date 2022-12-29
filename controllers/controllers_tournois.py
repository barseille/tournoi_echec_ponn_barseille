import  views.views_entree_tournoi as entree_tournoi
from models.tournoi import Tournoi
import json


class ControllersTournois:   

    def recuperer_entree_tournoi(self):
        """ sérialiser les données du tournoi"""
        
        print('-'*50)
        print("              -- Création Tournoi --")
        print('-'*50)
        
        liste_des_tournois = []
        
        while True:    
            self.nom = entree_tournoi.demander_nom_tournoi()
            self.lieu = entree_tournoi.demander_lieu_tournoi()
            self.dates = entree_tournoi.demander_dates_tournoi()  
            self.nombres_de_rounds = entree_tournoi.demander_rounds()
            self.description = entree_tournoi.demander_description()
            self.mode_de_jeu = entree_tournoi.demander_mode_de_jeu()
            
           
            tournoi = Tournoi(self.nom,
                              self.lieu,
                              self.dates,             
                              self.nombres_de_rounds,
                              self.description,
                              self.mode_de_jeu)  
            
            tournoi_serialiser = tournoi.serialiser()
            liste_des_tournois.append(tournoi_serialiser)      
                    
            autre_tournoi = input("Souhaitez_vous créer un autre tournoi ? (o/n) : ")
            if autre_tournoi == "o":
                print('Tournoi sauvegarder avec succès !')
                
            elif autre_tournoi == "n":
                print('Tournoi sauvegarder avec succès !')
                break
            
        with open("liste_tournois.json", "w") as f:
            json.dump(liste_des_tournois, f, indent=4)
            
        


    def afficher_les_tournois(self):
        """deserialiser la liste des tournois"""
        
        
        print('Voici la liste des tournois : ')
        
           
        
        with open ("liste_tournois.json", "r") as f:
            self.tournoi_data = json.load(f)
            
            for i, tournoi in enumerate(self.tournoi_data):
                print( i,'-' 
                      , 'Nom : ', tournoi['nom'], '|', 'Lieu : ', tournoi['lieu'], '|'
                      , 'Date(s) : ', tournoi['dates'], '|', 'Nombre de rounds : ', tournoi['nombres_de_rounds'], '|'
                      , 'Description : ', tournoi['description'], '|', 'Mode de jeu : ', tournoi['mode_de_jeu'])
                
        return self.tournoi_data
    
    
    def selectionner_tournoi(self):
        """ afficher la liste des tournois"""
        
        self.liste_des_tournois = []
        
        with open('liste_tournois.json', 'r') as f:
            self.tournoi_data = json.load(f)
            
        print('-'*50)
        print('         -- Sélectionnez votre tournoi -- ')
        print('-'*50)
        print(' - Sélectionner votre tournoi : ')
        print(' ')

        while True:


            if not self.tournoi_data:
                print("Il n'y a plus de tournoi à sélectionner")
                break
            
            for i, tournoi in enumerate(self.tournoi_data):
                print( ' ', i,'-' 
                      , 'Nom : ', tournoi['nom'], '|', 'Lieu : ', tournoi['lieu'], '|'
                      , 'Date(s) : ', tournoi['dates'], '|', 'Nombre de rounds : ', tournoi['nombres_de_rounds'], '|'
                      , 'Description : ', tournoi['description'], '|', 'Mode de jeu : ', tournoi['mode_de_jeu'])
             
            selection = input(' - Sélectionnez un tournoi (entrez "q" pour quitter): ')

            # Si l'utilisateur a saisi "q", quittez la boucle
            if selection == 'q':
                break

            # Convertir la sélection en entier
            try:
                selection = int(selection)
            except ValueError:
                print("Entrez un chiffre valide s'il vous plaît")
                continue
             
            # Vérifiez si l'index est valide
            if selection >= 0 and selection < len(self.tournoi_data):
                
                # Sélectionnez le dictionnaire correspondant
                tournoi_selectionner = self.tournoi_data[selection]
               
                print(f'Vous avez sélectionné  le tournoi : {tournoi_selectionner["nom"]} | lieu : {tournoi_selectionner["lieu"]}')
                self.liste_des_tournois.append(tournoi_selectionner)
                
                # Retirez le dictionnaire de la liste
                self.tournoi_data.pop(selection)
                break
                
            else:
                print("Entrez un chiffre valide s'il vous plaît")
               
        return self.liste_des_tournois
    
  











