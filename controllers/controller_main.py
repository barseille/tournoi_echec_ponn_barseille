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


class ControllerMain:
    
    
    def accueil_principal(self):
        
        while True:
            accueil = ViewsAccueil()
            accueil.accueil_principal()
            choix = input("Choisissez (1, 2, 3 ou 'q' pour quitter la partie): ")

            if choix == "1":
                self.menu_principal_tournoi()
            elif choix == "2":
                self.menu_principal_joueur()
            elif choix == "3":
                self.menu_rapport()
            elif choix == "q":
                sys.exit()
            else:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")

            
        
    # Menu tournoi
    def menu_principal_tournoi(self):
        
        while True:
            menu_tournoi = ViewsMenuTournoi()
            menu_tournoi.afficher_menu_tournoi()
            entree = input("Faites votre choix : ")

            if entree == "1":
                self.creer_tournoi()
            elif entree == "2":
                self.lancer_nouveau_tournoi()
            elif entree == "3":
                self.lancer_tournoi_existant()
            elif entree == "4":
                self.accueil_principal()
            else:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 4") 
                
                
                
    # Menu joueur
    def menu_principal_joueur(self):
        
        while True:
            menu_joueur = ViewsMenuJoueur()
            menu_joueur.afficher_menu_joueur()
            
            entree = input("Faites votre choix : ")
            
            # créer un joueur
            if entree == "1":
                self.creer_joueur()
                input("Appuyez sur une touche pour revenir au menu")
                
            # classement des joueurs par score
            elif entree == "2":
                self.afficher_classement_joueurs()
                input("Appuyez sur une touche pour revenir au menu")
                
            # retour à l'accueil
            elif entree == "3":
                break           
            else:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")
                
                
                
    def menu_rapport(self):
        
        while True:
        
            rapport = ViewsRapportMenu()
            rapport.afficher_menu_rapport()
            
            entree = input("Faites votre choix : ")   
            
            # Liste de tous les joueurs par ordre alphabétique
            if entree == "1":    
                rapport_joueur = ControllersRapport()
                rapport_joueur.affichage_joueur()
                
                input("Appuyer sur une touche pour revenir au menu")
                self.menu_rapport()
            
            # Liste de tous les tournois      
            elif entree == "2":
                rapport_tournoi = ControllersRapport()
                rapport_tournoi.affichage_tournoi()
                
                input("Appuyer sur une touche pour revenir au menu")      
                self.menu_rapport()
            
            # Liste des tournois terminés       
            elif entree == "3":
                rapport_tournoi_termine = ControllersRapport()
                rapport_tournoi_termine.afficher_details_tournoi()
                
                input("Appuyer sur une touche pour revenir au menu")
                self.menu_rapport()
            
            # Retour        
            elif entree == "4":
                self.accueil_principal()
                
            else:
                print("Erreur ! Veuillez saisir un chiffre entre 1 et 4")
 
            
    def creer_tournoi(self):
        
        creation_tournoi = ControllersTournois()
        creation_tournoi.recuperer_entree_tournoi()
        creation_tournoi.afficher_les_tournois()
        

    def lancer_nouveau_tournoi(self):
        
        tournoi = ControllersApplication()
        tournoi.fusion_tournoi_avec_joueurs()
        tournoi.afficher_tournoi_en_cours()
        tournoi.lancer_nouveau_tournoi()
       
            
    def lancer_tournoi_existant(self):
        
        tournoi_existant = ControllersApplicationTournoi()
        tournoi_existant.recuperation_tournois_existant()
        
    
    def creer_joueur(self):
        
        creation_joueur = ControllersJoueurs()
        creation_joueur.recuperer_entree_joueur()
        creation_joueur.afficher_des_joueurs()


    def afficher_classement_joueurs(self):
        
        classement_joueurs = ControllersJoueurs()
        classement_joueurs.trier_joueurs_par_score()
          

    
    
    