import views.views_entree_joueur as entree_joueur
from models.joueur import Joueur
import json

class ControllersJoueurs:
    

    def recuperer_entree_joueur(self):
        """ sérialiser les entrées joueurs"""
        
        print('-'*50)
        print("              -- Création Joueur --")
        print('-'*50)
        
        self.joueurs_data = []
        
        while True:                    
            self.nom = entree_joueur.creation_joueur_nom()
            self.prenom = entree_joueur.creation_joueur_prenom()
            self.date_de_naissance = entree_joueur.creation_joueur_date_de_naissance()
            self.genre = entree_joueur.creation_joueur_genre()
            self.classement = entree_joueur.creation_joueur_classement()
            
            joueur = Joueur(self.nom,
                            self.prenom,
                            self.date_de_naissance,
                            self.genre,
                            self.classement)
            
            joueur_serialiser = joueur.serialiser()         
            self.joueurs_data.append(joueur_serialiser)
            
            autre_joueur = input("Souhaitez_vous créer un autre joueur ? (o/n) : ")
            if autre_joueur == "o":
                print('Joueur sauvegarder avec succès !')
            if autre_joueur == "n":
                print('Tournoi sauvegarder avec succès !')
                break
            
        with open("liste_joueurs.json", "w") as f:
            json.dump(self.joueurs_data, f, indent=4)
    
 
    def afficher_des_joueurs(self):
        """ désérialisation la liste des joueurs """
        
        print('Voici la liste des joueurs : ')
           
        with open("liste_joueurs.json", "r") as f:        
            self.joueurs_data = json.load(f)
            
            for i, joueur in enumerate(self.joueurs_data):
                print(i,
                      '-' , joueur['prenom'], joueur['nom'],
                      ':',
                      ' Née le ', joueur['date_de_naissance'],
                      '|',
                      ' Genre : ', joueur['genre'],
                      '|',
                      'Classement : ', joueur['classement'])
                
        return self.joueurs_data

            
    def selectionner_participants(self):
            
            self.liste_des_participants = []
            
            # Chargez les données de joueurs.json
            with open('liste_joueurs.json', 'r') as f:
                joueur_data = json.load(f)
                
            print('-'*50)
            print('            -- Sélectionnez des joueurs -- ')
            print('-'*50)

            while True:
                # Affichez la liste des joueurs

                print(' - Sélectionnez un joueur : ')
                print(' ')
                if not joueur_data:
                    print("Il n'y a pas de joueur à sélectionner")
                    break
                
                for i, joueur in enumerate(joueur_data):
                    print(f' {i} - {joueur["prenom"]} {joueur["nom"]}')

                selection = input(' - Sélectionnez un joueur (entrez "q" pour quitter): ')

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
                if selection >= 0 and selection < len(joueur_data):
                    
                    # Sélectionnez le dictionnaire correspondant
                    joueur_selectionner = joueur_data[selection]
                    print(f'Vous avez sélectionné : {joueur_selectionner["prenom"]} {joueur_selectionner["nom"]}')
                    self.liste_des_participants.append(joueur_selectionner)

                    # Retirez le dictionnaire de la liste
                    joueur_data.pop(selection)
            
                else:
                    print("Entrez un chiffre valide s'il vous plaît")
 
            return self.liste_des_participants

    
                
           

        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






