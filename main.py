from views.views_menu_joueur import ViewsMenuJoueur
from views.accueil import ViewsAccueil
from views.views_menu_tournoi import ViewsMenuTournoi
from controllers.controllers_joueurs import ControllersJoueurs
from controllers.controllers_tournois import ControllersTournois
# from controllers.controllers_application import ControllersApplication
from controllers.controllers_tournoi_en_cours import ControllersTournoiEnCours
from views.views_rapport_menu import ViewsRapportMenu






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
        creation_tournoi.afficher_les_tournois()
        
        retour = input("Appuyer sur ENTREE pour revenir au menu")
        if retour == '':
            menu_principal_tournoi()
        
            
        
    def lancer_tournoi():
        
        tournoi = ControllersTournoiEnCours()
        tournoi.fusion_tournoi_avec_joueurs()
        tournoi.afficher_tournoi_en_cours()
        tournoi.lancer_tournoi()
        retour = input("Appuyer sur ENTREE pour revenir au menu")
        if retour == '':
            menu_principal_tournoi()
        
       
    # MENU JOUEUR
    def menu_principal_joueur():
        menu_joueur = ViewsMenuJoueur()
        menu_joueur.afficher_menu_joueur()
        entree = int(input("Faites votre choix : "))
        
        # creer un joueur
        if entree == 1:
            creer_joueur()
            retour = input("Appuyer sur ENTREE pour revenir au menu")
            if retour == '':
                menu_principal_joueur()

        # charger joueur existant
        elif entree == 2:
            # afficher la liste des joueurs
            selection_joueurs_pour_tournoi()
            
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
        creation_joueur.afficher_des_joueurs()

    def selection_joueurs_pour_tournoi():
        r = ControllersJoueurs()
        r.afficher_des_joueurs()
        r.selectionner_participants()
    

    def menu_rapport():
        rapport_joueur = ViewsRapportMenu()
        rapport_joueur.afficher_menu_rapport()
        entree = input("Faites votre choix : ")
        if entree == '1':
            rapport_joueur.affichage_joueur()
            retour = input("Appuyer sur ENTREE pour revenir au menu")
            if retour == '':
                accueil_principal()
        elif entree == '2':
            rapport_joueur.affichage_tournoi()
            rapport_joueur.afficher_details_tournoi()
  
    accueil_principal()
if __name__ == "__main__":
    main()
    