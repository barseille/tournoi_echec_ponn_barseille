import views.views_entree_joueur as entree_joueur
from views.views_menu_joueur import ViewsMenuJoueur
from models.joueur import Joueur
import json

class ControllersJoueurs:
    
    def recuperer_entree_joueur(self):
        """ Récupère les entrées utilisateur pour créer un nouveau joueur """

        # Affiche le menu de création de joueur
        creer_joueur = ViewsMenuJoueur()
        creer_joueur.affichage_creation_joueur()

        while True:

            # Récupère les informations du joueur
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

            # Récupère la liste des joueurs existants
            try:
                with open("data/liste_joueurs.json", "r") as f:
                    joueurs = json.load(f)["liste_joueurs"]
            except FileNotFoundError:
                joueurs = []

            """ 
            On choisit la valeur de la clé identifiant du dernier joueur
            et on convertit en entier pour 'incrémenter de 1
            """
            if joueurs:
                dernier_identifiant = int(joueurs[-1]["id"][1:])
                self.identifiant_joueur = f"j{dernier_identifiant + 1}"
            else:
                # S'il n'y a pas de joueurs enregistrés, alors l'id du 1er joueur sera j1.
                self.identifiant_joueur = "j1"

            # Sérialise les informations du joueur
            joueur_serialiser = joueur.serialiser()
            joueur_serialiser["id"] = self.identifiant_joueur
            self.ecrire_json(joueur_serialiser, "data/liste_joueurs.json") 

            # Demande si l'utilisateur souhaite créer un autre joueur
            autre_joueur = ""
            while True:
                autre_joueur = input("Souhaitez vous créer un autre joueur ? (o/n) : ")
                if autre_joueur in ["o", "n"]:
                    break
                else:
                    msg_erreur = ViewsMenuJoueur()
                    msg_erreur.affichage_erreur_creation()

            # Quitte la boucle si l'utilisateur ne souhaite pas créer un autre joueur
            if autre_joueur == "n":
                joueur_cree = ViewsMenuJoueur()
                joueur_cree.affichage_creation_joueur_reussi()
                break

 
    def ecrire_json(self, joueur_serialiser, dossier = 'data/liste_joueurs.json'):

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
 
 
        
    def selectionner_participants(self):
  
        with open("data/liste_joueurs.json", "r") as f:                
            joueurs_data = json.load(f)
                
            # Récupérer la liste des joueurs
            liste_joueurs = joueurs_data['liste_joueurs']
            
            for i, joueur in enumerate(liste_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")
            
            self.joueurs_selectionnes = []       
            
            # Demander à l'utilisateur combien de joueurs il souhaite sélectionner
            while True:
                try:
                    nombre_joueurs = int(input("Combien de joueurs souhaitez-vous sélectionner (8 joueurs minimum) : "))
                    if nombre_joueurs < 8 or nombre_joueurs > len(liste_joueurs):
                        print(f"Veuillez choisir un joueur entre 8 et {len(liste_joueurs)} : ")
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
        
        


        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






