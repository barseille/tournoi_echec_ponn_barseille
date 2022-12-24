from views.views_menu_joueur import ViewsMenuJoueur
from views.accueil import ViewsAccueil
from views.views_menu_tournoi import ViewsMenuTournoi
from controllers.controllers_joueurs import ControllersJoueurs
from controllers.controllers_tournois import ControllersTournois
from controllers.controllers_application import ControllersApplication




def main():
    
    # ACCUEIL TOURNOI  
    def accueil_principal():
        
        accueil = ViewsAccueil()
        accueil.accueil_principal()
        choix = int(input("Choisissez : "))
        
        if choix == 1:
            menu_principal_tournoi()
        elif choix == 2:
            menu_principal_joueur()
        elif choix == 3:
            menu_rapport()
        else:
            print("Veuillez saisir un chiffre entre 1 et 3")
            accueil_principal()
            
        
        
        
    # MENU TOURNOI
    def menu_principal_tournoi():
    
        menu_tournoi = ViewsMenuTournoi()
        menu_tournoi.afficher_menu_tournoi()
        entree = int(input("Faite votre choix : "))
        
         # création tournoi
        if entree == 1:
            creer_tournoi()
        elif entree == 2:
            lancer_tournoi()         
        else:
            print("Veuillez saisir un chiffre entre 1 et 3")
            accueil_principal()
            
    def creer_tournoi():
        
        creation_tournoi = ControllersTournois()
        creation_tournoi.recuperer_entree_tournoi()
        creation_tournoi.serialiser()
        creation_tournoi.deserialiser()
        # creation_tournoi.afficher_les_tournois()
        
        autre_tournoi = input("Voulez-vous créer un autre tournoi ? o(oui) / n(non) ")
        if autre_tournoi == "o":
            creer_tournoi()
        elif autre_tournoi == "n":
            accueil_principal()
        else:
            print("Veuillez saisir un chiffre entre 1 et 3")
            creer_tournoi()
            
    """----------------------------------------------------"""        
    def lancer_tournoi():
        
        selectionner_tournoi = ControllersApplication()
        selectionner_tournoi.selectionner_tournoi()
        

    """----------------------------------------------------"""
        # MENU JOUEUR
    def menu_principal_joueur():
      
        
        menu_joueur = ViewsMenuJoueur()
        menu_joueur.afficher_menu_joueur()
        entree = int(input("Faites votre choix : "))
        
        # creer un joueur
        if entree == 1:
            creer_joueur()

        # charger joueur existant
        elif entree == 2:
            selectionner_joueur_existant()
         # mise à jour classement joueur
        elif entree == 3:
            pass
            
        # retour à l'accueil
        elif entree == 4:
            accueil_principal()
        else:
            print("Veuillez saisir un chiffre entre 1 et 3")
            menu_principal_joueur()
            
    def creer_joueur():
        
        creation_joueur = ControllersJoueurs()
        creation_joueur.recuperer_entree_joueur()
        creation_joueur.deserialiser()

    def selectionner_joueur_existant():
        selection_joueur = ControllersJoueurs()
        selection_joueur.deserialiser()
        selection_joueur.selectionner_joueur()
                    

    def menu_rapport():
        # MENU RAPPORT 
       
        pass


    accueil_principal()
if __name__ == "__main__":
    main()
    