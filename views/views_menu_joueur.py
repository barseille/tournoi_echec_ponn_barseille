from .base_views import BaseViews
from database.database import Database

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs',
    'Informations sur les joueurs',
    'Retour'
)


class ViewsMenuJoueur(BaseViews):
    
    def __init__(self):
        self.liste_des_joueurs = []
        self.rencontre = {}
       
    def afficher_menu_joueur(self):
        
        titre = "                -- Menu Joueur --"
        self.presentation(titre)
    
        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        titre = "                -- Création Joueur --"
        self.presentation(titre)
        
        
    def affichage_erreur_creation(self):     
        affiche = BaseViews()
        affiche.affichage_erreur()
    
    
    def afficher_infos_joueurs(self):
        """ Informations détaillées sur les joueurs """
        
        titre = "               -- Liste des joueurs --"
        self.presentation(titre)
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.sauvegarde()
         
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Classement : {joueur['classement']}")
            print(f"                Identifiant : {joueur['id']}\n")
            
            
    def trier_joueurs_par_score(self):
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.sauvegarde()
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        titre = "              -- Classement par score -- "
        self.presentation(titre)
         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
            
 
    def selectionner_participants(self):
        
        # Ouvrir le fichier liste_joueurs.json
        liste_joueurs = self.sauvegarde()
                
        # Récupérer la clé liste des joueurs
        liste_joueurs = liste_joueurs['liste_joueurs']
        
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1}: {joueur['nom']}")     
        
        # L'utilisateur doit choisir 8 joueurs
        nombre_joueurs = 8
        print(f"Sélectionnez {nombre_joueurs} joueurs :")
        
        i = 1
        while i <= nombre_joueurs:
            try:
                choix_joueur = int(input("Choisissez un joueur : "))
                joueur_selectionne = liste_joueurs[choix_joueur - 1]
                
                # Vérifier si le joueur a déjà été sélectionné
                if joueur_selectionne in self.liste_des_joueurs:
                    print("Ce joueur a déjà été sélectionné. Veuillez en sélectionner un autre joueur.")
                else:
                    self.liste_des_joueurs.append(joueur_selectionne)
                    print("Joueur ajouté avec succès !")
                    i += 1
            except ValueError:
                print("Veuillez entrer un nombre entier valide")
            except IndexError:
                    print("L'index choisi n'est pas valide")
                    
        titre = "         -- Liste des joueurs sélectionnés --"
        self.presentation(titre)                     
 
        for i, joueur in enumerate(self.liste_des_joueurs):
            print(f"Joueur {i+1}: {joueur['nom']}")
                
        return self.liste_des_joueurs
    
    
    def presentation(self, titre):
        affiche = BaseViews()
        affiche.presentation(titre)
        
    def affichage_joueur_creer(self):
        print("Joueur créé avec succès !")
                
    def sauvegarde(self):
        data_joueur = Database()
        data = data_joueur.lire_database(chemin_fichier="data/liste_joueurs.json")
        return data
            
  
 

        
        
        
