
from .base_views import BaseViews
from database.database import Database

TOURNOI_OPTIONS = (
    'Créer un nouveau tournoi',
    'Lancer un nouveau tournoi',
    'Relancer un tournoi existant',
    'Retour'
)

class ViewsMenuTournoi(BaseViews):
    
    def afficher_menu_tournoi(self):
        
        titre = "                -- Menu Tournoi --"
        super().presentation(titre)

        print("Faites votre choix : ")
  
        for elt in TOURNOI_OPTIONS:
            print(TOURNOI_OPTIONS.index(elt) + 1, '-', elt)
            
            
    def affichage_creation_tournoi(self):
        titre = "                -- Création Tournoi --"
        super().presentation(titre)
        
        
    def afficher_les_tournois(self):
        """deserialiser la liste des tournois"""
        
        titre = "                -- Liste des tournois --"
        super().presentation(titre)
        
        data = Database()
        self.data_tournois = data.lire_database("data/liste_tournois.json")
    #     self.selectionner_tournoi()
      
            
    # def selectionner_tournoi(self):
        """ afficher la liste des tournois"""
  
        # Accéder à la clé "liste_tournoi" dans database
        self.liste_tournois = self.data_tournois['liste_tournois']

        # Afficher la liste des tournois
        for i, tournoi in enumerate(self.liste_tournois):
            print(f"Tournoi {i+1}: {tournoi['nom']}")

        # Demander à l'utilisateur de choisir un tournoi par son index
        while True:
            try:
                choix_tournoi = int(input("Choisissez un tournoi par son index: "))
                self.tournoi = self.liste_tournois[choix_tournoi -1]
                break
            except ValueError:
                super().affichage_erreur_type()
            except IndexError:
                super().affichage_erreur_numero()
        
        self.affichage_infos_tournoi()
        
        return self.tournoi
    

    
    def affichage_infos_tournoi(self):
        
        titre = "         -- Informations du Tournoi sélectionné --"
        super().presentation(titre)
        
        print(f"Nom du tournoi : {self.tournoi['nom']}")
        print(f"Lieu du tournoi : {self.tournoi['lieu']}")
        print(f"Date(s) du tournoi : {self.tournoi['dates']}")
        print(f"Nombres de rounds : {self.tournoi['nombres_de_rounds']}")
        print(f"Description : {self.tournoi['description']}")
        print(f"Mode de jeu : {self.tournoi['mode_de_jeu']}")
  
        
    def selectionner_tournoi_existant(self):
        try:
            entree = int(input("Saisir le numéro du tournoi : "))
            if entree > 0:
                return entree
            else:
                super().affichage_erreur_numero()
        except ValueError:
            super().affichage_erreur_type()



    
 
    def affichage_resultats(self):
        
            joueur1 = f"Résultat du match : {joueur1['prenom']} {joueur1['nom']} a gagné !"
            joueur2 = f"Résultat du match : {joueur2['prenom']} {joueur2['nom']} a gagné !"         
            match_nul = "Match nul !"          

    
    


            
            
            
            




