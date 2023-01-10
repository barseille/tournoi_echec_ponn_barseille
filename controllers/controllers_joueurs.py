import views.views_entree_joueur as entree_joueur
from models.joueur import Joueur
import json

class ControllersJoueurs:
    

    def recuperer_entree_joueur(self):
        """ sérialiser les entrées joueurs"""
        
        print('-'*50)
        print("              -- Création Joueur --")
        print('-'*50)
        
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
            self.ecrire_json(joueur_serialiser, "liste_joueurs.json")  
                   
 
            autre_joueur = input("Souhaitez vous créer un autre joueur ? (o/n) : ")
            if autre_joueur == "o":
                print('Créer un nouveau joueur : ')
            if autre_joueur == "n":
                print('Tournoi sauvegarder avec succès !')
                break
 
 
    def ecrire_json(self, joueur_serialiser, dossier = 'liste_joueurs.json'):

        """
        La méthode prend en premier argument un dictionnaire (tournoi_serialiser) 
        et en second argument (optionnel) le fichier JSON où enregistrer les données du tournoi.
        Elle ouvre le fichier JSON en mode lecture/écriture ('r+').
        Elle charge les données du fichier JSON dans un dictionnaire (liste_tournois).
        Elle ajoute tournoi_serialiser à liste_tournois.
        Elle remet le curseur de fichier au début (f.seek(0)) 
        et écrit le dictionnaire modifié dans le fichier JSON en utilisant la fonction json.dump.

        """
        
        with open(dossier, 'r+') as f:
            liste_joueurs = json.load(f)
            liste_joueurs["liste_joueurs"].append(joueur_serialiser)
            f.seek(0)
            json.dump(liste_joueurs, f, indent=4)       
 
 
    def afficher_des_joueurs(self):
        """ désérialisation la liste des joueurs """
        
        print('-'*50)
        print('   -- Liste des joueurs --')
        print('-'*50)
        
           
        with open("liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
            
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']} | Genre : {joueur['genre']} | Classement : {joueur['classement']}")
            
        
    def selectionner_participants(self):
  
        with open("liste_joueurs.json", "r") as f:                
            joueurs_data = json.load(f)
                
            # Récupérer la liste des joueurs
            liste_joueurs = joueurs_data['liste_joueurs']
            
            for i, joueur in enumerate(liste_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")
            
            self.joueurs_selectionnes = []       
            
            # Demander à l'utilisateur combien de joueurs il souhaite sélectionner
            while True:
                try:
                    nombre_joueurs = int(input("Combien de joueurs souhaitez-vous sélectionner : "))
                    if nombre_joueurs < 2 or nombre_joueurs > len(liste_joueurs):
                        print(f"Veuillez choisir un joueur entre 2 et {len(liste_joueurs)} : ")
                    else:
                        break
                except ValueError:
                    print("Veuillez entrer un nombre entier valide")
            
            # Demander à l'utilisateur de choisir les joueurs par leur index
            print(f"Sélectionnez {nombre_joueurs} joueurs :")
            i = 1
            while i <= nombre_joueurs:
                try:
                    choix_joueur = int(input("Choisissez un joueur : "))
                    joueur_selectionne = liste_joueurs[choix_joueur - 1]
                    
                    # Vérifier si le joueur a déjà été sélectionné
                    if joueur_selectionne in self.joueurs_selectionnes:
                        print("Ce joueur a déjà été sélectionné. Veuillez en sélectionner un autre.")
                    else:
                        self.joueurs_selectionnes.append(joueur_selectionne)
                        print("Joueur ajouté !")
                    i += 1
                except ValueError:
                    print("Veuillez entrer un nombre entier valide")
    
            return self.joueurs_selectionnes
        


        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






