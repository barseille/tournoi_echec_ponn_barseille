import json
from .views_menu_tournoi import ViewsMenuTournoi
from .base_views import BaseViews
from database.database import Database
from .views_menu_tournoi import ViewsMenuTournoi

RAPPORT_OPTIONS = ("Liste de tous les joueurs par ordre alphabétique", 
                   "Liste de tous les tournois crées",
                   "Liste des tournois terminés",
                   "Retour")


class ViewsRapportMenu:
    
    def __init__(self):
        self.base_views = BaseViews()
        self.database = Database()
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.joueurs = []
    
    def afficher_menu_rapport(self):

        msg = "                -- Menu Rapport --"
        self.base_views.presentation(msg)
        
        for elt in RAPPORT_OPTIONS:
            print(RAPPORT_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_joueur(self):
        
        msg = '         -- Classement des joueurs par ordre alphabetique --'
        self.base_views.presentation(msg)
        
        joueurs_data = self.database.lire_database("data/liste_joueurs.json")
 
        self.liste_joueurs = joueurs_data['liste_joueurs']
        self.liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        
        if not self.liste_joueurs:
            print("Aucuns joueurs touvés !")
            return
        
        for i, joueur in enumerate(self.liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']}")
        
    
    
    def affichage_tournoi(self):
        
        afficher_tournoi = ViewsMenuTournoi()
        afficher_tournoi.afficher_les_tournois()
        

    def afficher_details_tournoi(self):
        
        msg = '             -- Liste des tournois terminés --'
        self.base_views.presentation(msg)
        
        tournoi = self.database.lire_database("data/historique_tournois.json")

        
        tournoi_termine = tournoi['liste_des_tournois']
        
        if not tournoi_termine:
            print("Aucuns tournois trouvés !")
            return
        
        # Afficher tous les tournois terminés
        i = 1
        for i, tournoi in enumerate(tournoi_termine):
            nom = tournoi["nom"]
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi {nom} - date(s) : {dates}")
        
 
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))
        
        # Détails du tournoi sélectionné
        self.tournoi_selectionne = tournoi_termine[choix_tournoi - 1]
        
        
        msg = '               -- Détails du tournoi terminé --'
        self.base_views.presentation(msg)
        
        # Afficher les informations du tournoi
        self.views_menu_tournoi.affichage_infos_tournoi(self.tournoi_selectionne)
        
        msg = "               -- Classement de joueurs par scores --"
        self.base_views.presentation(msg)
        
        # Joueurs rangés par ordre alphabétique
        self.liste_joueurs = self.tournoi_selectionne['joueurs']
        self.liste_joueurs.sort(key=lambda joueur: joueur['score'], reverse=True)
        
        # Afficher les joueurs du tournoi 
        for i, joueur in enumerate(self.liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Score : {joueur['score']}")
        
        self.infos_rounds()
        
     
     # Informations détaillées de chaque round   
    def infos_rounds(self):
        
        msg = "               -- Résultats des matchs par rounds --"
        self.base_views.presentation(msg)
        
        resultats = self.tournoi_selectionne["resultats"]
        
        for round, infos in resultats.items():
            print(f"{round} :")
            
            matchs = infos['matchs']
            for match in matchs:
                print(f"{match}")
                
            print(f"Début: {infos['debut']}")
            print(f"Fin: {infos['fin']}\n")
                      
   
    def affichage_scores_joueurs(self, liste_joueurs):
        
        msg = "               -- Liste des joueurs --"
        self.base_views.presentation(msg)
        
        # Afficher les joueurs du tournoi 
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Score :  {joueur['score']}")
               
