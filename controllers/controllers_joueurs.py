import views.views_entree_joueur as entree_joueur
from views.views_menu_joueur import ViewsMenuJoueur
from models.joueur import Joueur
import json
from views.base_views import BaseViews

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
            self.classement = entree_joueur.creation_joueur_classement()
            self.id = entree_joueur.ajout_identifiant()

            joueur = Joueur(self.nom,
                            self.prenom,
                            self.date_de_naissance,
                            self.classement,
                            self.id)


            # Sérialise les informations du joueur
            joueur_serialiser = joueur.serialiser()
            self.ecrire_json(joueur_serialiser, "data/liste_joueurs.json") 

            # Demande si l'utilisateur souhaite créer un autre joueur
            autre_joueur = ""
            while True:
                autre_joueur = input("Souhaitez vous créer un autre joueur ? (o/n) : ")
                if autre_joueur in ["o", "n"]:
                    break
                else:
                    msg_erreur = BaseViews()
                    msg_erreur.affichage_erreur()

            # Quitte la boucle si l'utilisateur ne souhaite pas créer un autre joueur
            if autre_joueur == "n":
                titre = "Joueur créé avec succès !"
                affiche = BaseViews()
                affiche.afficher_msg(titre)
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
    
            

     
 
 
 
 
 
 
 
 
 
 
 
 
        

        
        


        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






