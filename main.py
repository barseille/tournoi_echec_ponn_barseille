from views.views_menu_joueur import ViewsMenuJoueur
from views.accueil import ViewsAccueil
from views.views_menu_tournoi import ViewsMenuTournoi
from controllers.controllers_joueurs import ControllersJoueurs
from controllers.controllers_tournois import ControllersTournois
from views.views_rapport_menu import ViewsRapportMenu
from controllers.controllers_application import ControllersApplication
from controllers.controllers_application_tournoi import ControllersApplicationTournoi
from controllers.controllers_rapport import ControllersRapport
import sys



def main():
    
    # Accueil principal  
    def accueil_principal():
        
        accueil = ViewsAccueil()
        accueil.accueil_principal()
        choix = input("Choisissez (1, 2, 3 ou 'q' pour quitter la partie): ")
        
        try:
            if choix == "1":
                menu_principal_tournoi()
            elif choix == "2":
                menu_principal_joueur()
            elif choix == "3":
                menu_rapport()
            elif choix == "q":
                sys.exit()
            else:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")
                accueil_principal()
        except ValueError:
            print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")
            accueil_principal()
            
        
    # Menu tournoi
    def menu_principal_tournoi():
    
        menu_tournoi = ViewsMenuTournoi()
        menu_tournoi.afficher_menu_tournoi()
        entree = int(input("Faites votre choix : "))
        
        try:
            if entree == 1:
                creer_tournoi()
            elif entree == 2:
                lancer_nouveau_tournoi()   
            elif entree == 3:
                lancer_tournoi_existant() 
            elif entree == 4:
                accueil_principal()     
            else:
                print("Veuillez saisir un chiffre entre 1 et 4")
                menu_principal_tournoi()
        except ValueError:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 4")
                menu_principal_tournoi()
     
            
    def creer_tournoi():
        
        creation_tournoi = ControllersTournois()
        creation_tournoi.recuperer_entree_tournoi()
        creation_tournoi.afficher_les_tournois()
        
        input("Appuyer sur une touche pour revenir au menu")
        menu_principal_tournoi()
        
               
    def lancer_nouveau_tournoi():
        
        tournoi = ControllersApplication()
        tournoi.fusion_tournoi_avec_joueurs()
        tournoi.afficher_tournoi_en_cours()
        tournoi.lancer_nouveau_tournoi()
       
        
        input("Appuyer sur une touche pour revenir au menu")
        menu_principal_tournoi()
            
            
    def lancer_tournoi_existant():
        tournoi_existant = ControllersApplicationTournoi()
        tournoi_existant.recuperation_tournois_existant()
        
        input("Appuyer sur une touche pour revenir au menu")
        menu_principal_tournoi()
            
       
    # Menu joueur
    def menu_principal_joueur():
        menu_joueur = ViewsMenuJoueur()
        menu_joueur.afficher_menu_joueur()
        entree = int(input("Faites votre choix : "))
        
        try:
            # creer un joueur
            if entree == 1:
                creer_joueur()
                input("Appuyer sur une touche pour revenir au menu")
                menu_principal_joueur()

            # Classement des joueurs par score
            elif entree == 2:
                afficher_classement_joueurs()
                input("Appuyer sur une touche pour revenir au menu")
                menu_principal_joueur()
    
            # retour à l'accueil
            elif entree == 3:
                accueil_principal()   
                    
            else:
                print("Veuillez saisir un chiffre entre 1 et 3")
                menu_principal_joueur()
                
        except ValueError:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")
                menu_principal_joueur()
            
            
    def creer_joueur():
        
        creation_joueur = ControllersJoueurs()
        creation_joueur.recuperer_entree_joueur()
        creation_joueur.afficher_des_joueurs()


    def afficher_classement_joueurs():
        
        classement_joueurs = ControllersJoueurs()
        classement_joueurs.trier_joueurs_par_score()
        

    def menu_rapport():
        
        rapport = ViewsRapportMenu()
        rapport.afficher_menu_rapport()
        
        entree = input("Faites votre choix : ")   
        
        # Liste de tous les joueurs par ordre alphabétique
        if entree == '1':    
            rapport_joueur = ControllersRapport()
            rapport_joueur.affichage_joueur()
            
            input("Appuyer sur une touche pour revenir au menu")
            menu_rapport()
         
        # Liste de tous les tournois      
        elif entree == '2':
            rapport_tournoi = ControllersRapport()
            rapport_tournoi.affichage_tournoi()
            
            input("Appuyer sur une touche pour revenir au menu")      
            menu_rapport()
         
        # Liste des tournois terminés       
        elif entree == '3':
            rapport_tournoi_termine = ControllersRapport()
            rapport_tournoi_termine.afficher_details_tournoi()
            
            input("Appuyer sur une touche pour revenir au menu")
            menu_rapport()
        
        # Retour        
        elif entree == '4':
            accueil_principal()
            
  
  
    accueil_principal()
if __name__ == "__main__":
    main()
    