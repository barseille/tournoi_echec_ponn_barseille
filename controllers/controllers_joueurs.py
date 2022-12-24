import views.views_entree_joueur as entree_joueur
import json

class ControllersJoueurs:

    def recuperer_entree_joueur(self):
        """ sérialiser les entrées joueurs"""
        
        print('-'*50)
        print("              -- Création Joueur --")
        print('-'*50)
        
        liste_des_joueurs = []
        
        while True:
                            
            self.nom = entree_joueur.creation_joueur_nom()
            self.prenom = entree_joueur.creation_joueur_prenom()
            self.date_de_naissance = entree_joueur.creation_joueur_date_de_naissance()
            self.genre = entree_joueur.creation_joueur_genre()
            self.classement = entree_joueur.creation_joueur_classement()
            
            joueur = {"nom": self.nom,
                      "prenom": self.prenom,
                      "date_de_naissance": self.date_de_naissance,
                      "genre": self.genre,
                      "classement": self.classement}
            
            liste_des_joueurs.append(joueur)
            
            autre_joueur = input("Souhaitez_vous créer un autre joueur ? (o/n) : ")
            if autre_joueur == "n":
                break
            
        with open("liste_joueurs.json", "w") as f:
            json.dump(liste_des_joueurs, f, indent=4)
    
 
    def deserialiser(self):
        """ désérialisation la liste des joueurs """
        
        print('-'*50)
        print('              -- Liste des joueurs --')
        print('-'*50)
           
        with open("liste_joueurs.json", "r") as f:        
            self.joueur_deserialiser = json.load(f)
            
            for i, joueur in enumerate(self.joueur_deserialiser):
                print(i,
                      '-' , joueur['prenom'], joueur['nom'],
                      ':',
                      ' née le ', joueur['date_de_naissance'],
                      '/',
                      ' genre : ', joueur['genre'],
                      '/',
                      'classement : ', joueur['classement'])
                
        return self.joueur_deserialiser

            
    def selectionner_joueur(self):
        
        liste_joueurs_pour_tournoi = []

        # Demander à l'utilisateur de saisir l'index du joueur à sélectionner       
        selectionner = int(input('Sélectionnez un joueur : '))
        
        # Initialisez le joueur sélectionné à None
        selection_joueur = None
        
        # Vérifiez si l'index saisi est valide
        if selectionner >= 0 and selectionner < len(self.joueur_deserialiser):

            selection_joueur = self.joueur_deserialiser[selectionner]
            liste_joueurs_pour_tournoi.append(selection_joueur)
            print("vous avec selectionner : ")
            print(selection_joueur["prenom"], selection_joueur["nom"])
            
        print(liste_joueurs_pour_tournoi)
        
        
            
                
    

    
    
    
    
    
   
   

        
    






