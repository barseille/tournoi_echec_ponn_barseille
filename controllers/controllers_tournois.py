import  views.views_entree_tournoi as entree_tournoi
from views.views_menu_tournoi import ViewsMenuTournoi
from models.tournoi import Tournoi
import json
from views.base_views import BaseViews


class ControllersTournois(BaseViews): 
    
   
    def recuperer_entree_tournoi(self):
        """ sérialiser les données du tournoi"""
        
        creer_tournoi = ViewsMenuTournoi()
        creer_tournoi.affichage_creation_tournoi()
        
        while True:    
            self.nom = entree_tournoi.demander_nom_tournoi()
            self.lieu = entree_tournoi.demander_lieu_tournoi()
            self.dates = entree_tournoi.demander_dates_tournoi()  
            self.nombres_de_rounds = entree_tournoi.demander_rounds()
            self.description = entree_tournoi.demander_description()
            self.mode_de_jeu = entree_tournoi.demander_mode_de_jeu()
            
            tournoi = Tournoi(self.nom,
                              self.lieu,
                              self.dates,             
                              self.nombres_de_rounds,
                              self.description,
                              self.mode_de_jeu)  
            
            tournoi_infos = tournoi.afficher_tournoi()
            self.ecrire_json(tournoi_infos, "data/liste_tournois.json")   
            
            autre_tournoi = ""  
            while True:      
                autre_tournoi = input("Souhaitez-vous créer un autre tournoi ? (o/n) : ")
                if autre_tournoi in ["o", "n"]:
                    break
                else:
                    affiche = BaseViews()
                    affiche.affichage_erreur()
                    
                    
            if autre_tournoi == "o": 
                msg = "Créer un nouveau tournoi : "  
                affiche = BaseViews()
                affiche.afficher_msg(msg)    
                
                
            elif autre_tournoi == "n":
                msg = "Tournoi sauvegarder avec succès !"  
                affiche = BaseViews()
                affiche.afficher_msg(msg)

                break
                
            
    def ecrire_json(self, tournoi_infos, dossier ='data/liste_tournois.json'):
        
        """
        La méthode prend en premier argument un dictionnaire (tournoi_infos) 
        et en second argument (optionnel) le fichier JSON où enregistrer les données du tournoi.
        Elle ouvre le fichier JSON en mode lecture/écriture ('r+').
        Elle charge les données du fichier JSON dans un dictionnaire (liste_tournois).
        Elle ajoute tournoi_infos à liste_tournois.
        Elle remet le curseur de fichier au début (f.seek(0)) 
        et écrit le dictionnaire modifié dans le fichier JSON en utilisant la fonction json.dump.

        """
        
        with open(dossier,'r+') as f:    
            liste_tournois = json.load(f)
            liste_tournois["liste_tournois"].append(tournoi_infos)        
            f.seek(0)  
            json.dump(liste_tournois, f, indent=4)

    



            











