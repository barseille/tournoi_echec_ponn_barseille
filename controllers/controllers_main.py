from views.views_menu_joueur import ViewsMenuJoueur
from views.accueil import ViewsAccueil
from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_rapport_menu import ViewsRapportMenu
from controllers.controllers_joueurs import ControllersJoueurs
from controllers.controllers_tournois import ControllersTournois
from controllers.controllers_application import ControllersApplication
from controllers.controllers_application_tournoi import ControllersApplicationTournoi
from views.base_views import BaseViews
from controllers.controllers_base import ControllersBase
import sys


class ControllersMain:
    
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
                affiche = BaseViews()
                affiche.affichage_erreur_numero()           
          
        
    # Menu tournoi
    def menu_principal_tournoi(self):
        
        while True:        
            menu_tournoi = ViewsMenuTournoi()
            menu_tournoi.afficher_menu_tournoi()
            entree = input("Faites votre choix : ")

            # Créer tournoi et afficher les tournois
            if entree == "1":            
                creation_tournoi = ControllersTournois()
                creation_tournoi.recuperer_entree_tournoi()
                # afficher_tournois = ViewsMenuTournoi()
                # afficher_tournois.afficher_les_tournois()
            
            # Lancer un tournoi    
            elif entree == "2":             
                tournoi = ControllersBase()
                tournoi.fusion_tournoi_avec_joueurs()
                # tournoi.match()
                # tournoi.jouer_match()
                tournoi.lancer_round()
                
               
            elif entree == "3":              
                tournoi_trouve = ControllersApplicationTournoi()
                tournoi_trouve.recuperation_tournois_existant()
            
            
            elif entree == "4": 
                break         
                
            else:
                affiche = BaseViews()
                affiche.affichage_erreur_numero()  
                           
                
    # Menu joueur
    def menu_principal_joueur(self):
        
        while True:    
            menu_joueur = ViewsMenuJoueur()
            menu_joueur.afficher_menu_joueur()
            
            entree = input("Faites votre choix : ")
            
            # créer un joueur et afficher tous les joueurs
            if entree == "1":          
                creation_joueur = ControllersJoueurs()
                creation_joueur.recuperer_infos_joueur() 
                
   
                self.retour_menu()   
          
                
            # classement des joueurs par score
            elif entree == "2":          
                classement_joueurs = ViewsMenuJoueur()
                classement_joueurs.trier_joueurs_par_score()
                self.retour_menu() 
                
            
                
            # Informations sur les joueurs
            elif entree == "3":
                afficher_joueurs = ViewsMenuJoueur()
                afficher_joueurs.afficher_infos_joueurs()
                
            # retour à l'accueil   
            elif entree == "4":
                break   
                    
            else:
                affiche = BaseViews()
                affiche.affichage_erreur_numero()  
                             
                
    def menu_rapport(self):
        
        while True:  
            rapport = ViewsRapportMenu()
            rapport.afficher_menu_rapport()          
            entree = input("Faites votre choix : ")
            
            # Liste de tous les joueurs par ordre alphabétique
            if entree == "1":                   
                rapport_joueur = ViewsRapportMenu()
                rapport_joueur.affichage_joueur() 
                self.retour_menu()           
           
            
            # Liste de tous les tournois      
            elif entree == "2":            
                rapport_tournoi = ViewsRapportMenu()
                rapport_tournoi.affichage_tournoi()
                self.retour_menu()              
          
            
            # Liste des tournois terminés       
            elif entree == "3":            
                rapport_tournoi_termine = ViewsRapportMenu()
                rapport_tournoi_termine.afficher_details_tournoi()  
                self.retour_menu()          
            
            # Retour        
            elif entree == "4":
                break
                
            else:
                affiche = BaseViews()
                affiche.affichage_erreur_numero()  
     
                
    def retour_menu(self):
        
        retour = BaseViews()
        retour.retour_au_menu()
 

    