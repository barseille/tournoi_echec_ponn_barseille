import json
from .base_views import BaseViews

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs',
    'Retour'
)


class ViewsMenuJoueur:
    
    liste_des_joueurs = []
    rencontres = {} 
       
    def afficher_menu_joueur(self):
        
        titre = "                -- Menu Joueur --"
        affiche = BaseViews()
        affiche.presentation(titre)

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        titre = "                -- Création Joueur --"
        affiche = BaseViews()
        affiche.presentation(titre)
        

        
    def affichage_erreur_creation(self):     
        print("Erreur : Veuillez entrer 'o' pour créer un autre joueur ou 'n' pour quitter.")
    
    
    def afficher_des_joueurs(self):
        """ désérialisation la liste des joueurs """
        
        
        titre = "               -- Liste des joueurs --"
        affiche = BaseViews()
        affiche.presentation(titre)
        
           
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
            
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Classement : {joueur['classement']}")
            print(f"                Identifiant : {joueur['id']}")
            
            
    def trier_joueurs_par_score(self):
        
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        titre = "              -- Classement par score -- "
        affiche = BaseViews()
        affiche.presentation(titre)

         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
            
 
    def selectionner_participants(self):
    
        with open("data/liste_joueurs.json", "r") as f:                
            joueurs_data = json.load(f)
                
            # Récupérer la liste des joueurs
            liste_joueurs = joueurs_data['liste_joueurs']
            
            for i, joueur in enumerate(liste_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")     
            
            # Demander à l'utilisateur combien de joueurs il souhaite sélectionner
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
            affiche = BaseViews()
            affiche.presentation(titre)                       


            
            for i, joueur in enumerate(self.liste_des_joueurs):
                print(f"Joueur {i+1}: {joueur['nom']}")
                
        return self.liste_des_joueurs
        
    
    
 

        
        
        
