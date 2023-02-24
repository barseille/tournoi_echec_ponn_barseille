from .base_views import BaseViews
from database.database import Database

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs par score',
    'Informations sur les joueurs',
    'Retour'
)


class ViewsMenuJoueur(BaseViews):
    
    def __init__(self):
        self.liste_des_joueurs = []
        self.rencontre = {}
       
    def afficher_menu_joueur(self):
        
        titre = "                -- Menu Joueur --"
        super().presentation(titre)
    
        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        titre = "                -- Création Joueur --"
        super().presentation(titre)
        
        
    # def affichage_erreur_creation(self):   
    #     super().affichage_erreur_choix()       
 
    def selectionner_participants(self):
        
        titre = "               -- Liste des joueurs --"
        super().presentation(titre)
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.ouvrir_database()
                
        # Récupérer la clé liste des joueurs
        self.liste_joueurs = liste_joueurs['liste_joueurs']
        
        for i, joueur in enumerate(self.liste_joueurs):
            print(f"Joueur {i+1}: {joueur['prenom']} {joueur['nom']}")     
        
        # L'utilisateur doit choisir 8 joueurs
        nombre_joueurs = 8
        print(f"Sélectionnez {nombre_joueurs} joueurs :")
        
        i = 1
        while i <= nombre_joueurs:
            try:
                choix_joueur = int(input("Choisissez un joueur par son numéro : "))
                joueur_selectionne = self.liste_joueurs[choix_joueur - 1]
                
                # Vérifier si le joueur a déjà été sélectionné
                if joueur_selectionne in self.liste_des_joueurs:
                    print("Ce joueur a déjà été sélectionné. Veuillez en sélectionner un autre joueur.")
                else:
                    self.liste_des_joueurs.append(joueur_selectionne)
                    print("Joueur ajouté avec succès !")
                    i += 1
            except ValueError:
                super().affichage_erreur_type()
               
            except IndexError:
                super().affichage_erreur_numero()
                    
        titre = "         -- Liste des joueurs sélectionnés --"
        super().presentation(titre)                    
 
        for i, joueur in enumerate(self.liste_des_joueurs):
            print(f"Joueur {i+1}: {joueur['nom']}")
                
        return self.liste_des_joueurs
    
    

        
    def affichage_joueur_cree(self):
        print("Joueur créé avec succès !")
        
        
    def afficher_infos_joueurs(self):
        """ Informations détaillées sur les joueurs """
        
        titre = "               -- Liste des joueurs --"
        super().presentation(titre)
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.ouvrir_database()
         
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Classement : {joueur['classement']}")
            print(f"                Identifiant : {joueur['id']}\n")
            
            
    def trier_joueurs_par_score(self):
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.ouvrir_database()
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        titre = "              -- Classement par score -- "
        super().presentation(titre)
         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
                
    def ouvrir_database(self):
        data_joueur = Database()
        data = data_joueur.lire_database(chemin_fichier="data/liste_joueurs.json")
        return data
            
  
 

        
        
        
