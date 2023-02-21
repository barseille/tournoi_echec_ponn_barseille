from views.views_entree_joueur import ViewsEntreeJoueur
from views.views_menu_joueur import ViewsMenuJoueur
from views.base_views import BaseViews
from database.database import Database

class ControllersJoueurs:
    def __init__(self):
        self.views_joueur = ViewsEntreeJoueur()
    
    def recuperer_infos_joueur(self):
        """ Récupère les entrées utilisateur pour créer un nouveau joueur """

        # Affiche le menu de création de joueur
        creer_joueur = ViewsMenuJoueur()
        creer_joueur.affichage_creation_joueur()

        # Récupération de la création joueur
        self.joueur = self.views_joueur.infos_joueur()
        
        # sauvegarder les informations du joueur(données, clé, chemin)
        self.sauvergarde()
        
        # Demande à l'utilisateur s'il veut créer un autre joueur
        while True:
            choix = input("Souhaitez-vous créer un autre joueur ? (o/n) : ")
            if choix == "o":
                self.joueur_infos = self.recuperer_infos_joueur()
            elif choix == "n":
                affiche = ViewsMenuJoueur()
                affiche.affichage_joueur_creer()
                break
            else:
                msg_erreur = BaseViews()
                msg_erreur.affichage_erreur()
            break
        
                    
    def sauvergarde(self):
        data = Database()
        data.ecrire_database(self.joueur, "liste_joueurs", chemin_fichier='data/liste_joueurs.json')
        

        

    
            

     
 
 
 
 
 
 
 
 
 
 
 
 
        

        
        


        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






