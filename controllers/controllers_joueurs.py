from views.views_entree_joueur import ViewsEntreeJoueur
from views.views_menu_joueur import ViewsMenuJoueur
from database.database import Database

class ControllersJoueurs:
    
    def __init__(self):      
        self.views_entree_joueur = ViewsEntreeJoueur()
        self.views_menu_joueur = ViewsMenuJoueur()
    
    
    def recuperer_infos_joueur(self):
        """ Récupère les entrées utilisateur pour créer un nouveau joueur """

        # Affiche le menu de création de joueur
        self.views_menu_joueur.affichage_creation_joueur()

        # Récupération de la création joueur
        self.joueur = self.views_entree_joueur.infos_joueur()
        
        # sauvegarder les informations du joueur(données, clé, chemin)
        self.sauvergarde()
        
        # Demande à l'utilisateur s'il veut créer un autre joueur
        choix = ""
        while True:
            choix = input("Souhaitez-vous créer un autre joueur ? (o/n) : ")
            if choix in ["o", "n"]:
                break
            else:
                self.views_menu_joueur.affichage_erreur_creation()
                
        if choix == "o":
            self.recuperer_infos_joueur()
        elif choix == "n":
            self.views_menu_joueur.affichage_joueur_cree()
        
                    
    def sauvergarde(self):
        data = Database()
        data.ecrire_database(self.joueur, "liste_joueurs", chemin_fichier='data/liste_joueurs.json')
        


  