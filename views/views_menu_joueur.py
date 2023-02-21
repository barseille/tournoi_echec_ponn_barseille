from .base_views import BaseViews

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs',
    'Informations sur les joueurs',
    'Retour'
)


class ViewsMenuJoueur:
    
    liste_des_joueurs = []
    rencontres = {} 
       
    def afficher_menu_joueur(self):
        
        titre = "                -- Menu Joueur --"
        self.presentatation(titre)
    

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        titre = "                -- Création Joueur --"
        self.presentatation(titre)
        
        
    def affichage_erreur_creation(self):     
        affiche = BaseViews()
        affiche.affichage_erreur()
    
    
    def afficher_infos_joueurs(self):
        """ Informations détaillées sur les joueurs """
        
        titre = "               -- Liste des joueurs --"
        self.presentatation(titre)
        
        # Ouvrir le fichier liste_joueurs.json
        data_joueur = BaseViews()
        liste_joueurs = data_joueur.lire_fichier_json("data/liste_joueurs.json")
         
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Classement : {joueur['classement']}")
            print(f"                Identifiant : {joueur['id']}")
            
            
    def trier_joueurs_par_score(self):
        
        # Ouvrir le fichier liste_joueurs.json
        data_joueur = BaseViews()
        liste_joueurs = data_joueur.lire_fichier_json("data/liste_joueurs.json")
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        titre = "              -- Classement par score -- "
        self.presentatation(titre)

         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
            
 
    def selectionner_participants(self):
 
        data_joueur = BaseViews()
        liste_joueurs = data_joueur.lire_fichier_json("data/liste_joueurs.json")
                
        # Récupérer la liste des joueurs
        liste_joueurs = liste_joueurs['liste_joueurs']
        
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
        self.presentatation(titre)                     
 
        for i, joueur in enumerate(self.liste_des_joueurs):
            print(f"Joueur {i+1}: {joueur['nom']}")
                
        return self.liste_des_joueurs
    
    
    def presentatation(self, titre):
        affiche = BaseViews()
        affiche.presentation(titre)
        
    # def lire_joueurs_json(self):
    #     # Ouvrir le fichier liste_joueurs.json
    #     data_joueur = BaseViews()
    #     liste_joueurs = data_joueur.lire_fichier_json("data/liste_joueurs.json")
        
    
    
 

        
        
        
