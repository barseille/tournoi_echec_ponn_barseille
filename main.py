import controllers.controllers_menu_joueur as controllers_menu_joueur
from views.views_menu_joueur import ViewsMenuJoueur
from views.accueil import ViewsAccueil


def main():
    # ACCUEI TOURNOI
    accueil = ViewsAccueil()
    accueil.accueil_principal()
    choix = int(input("Choisissez : "))
    
    # MENU TOURNOI
    if choix == 1:
        pass
    
    # MENU JOUEUR
    elif choix == 2:
       
        menu_joueur = ViewsMenuJoueur()
        menu_joueur.afficher_menu_joueur()
        entree = int(input("Faite votre choix : "))
        
        # creer un joueur
        if entree == 1:
            controllers_menu_joueur.sauvegarder()
            controllers_menu_joueur.creation_autre_joueur()
        # mise à jour classement joueur
        elif entree == 2:
            pass
        # retour à l'accueil
        elif entree == 3:
            accueil.accueil_principal()
        else:
            print("Veuillez saisir un chiffre entre 1 et 3")
            
    # MENU RAPPORT 
    elif choix == 3:
       
        pass

if __name__ == "__main__":
    main()
    