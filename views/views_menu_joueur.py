import json

JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Classement des joueurs',
    'Retour'
)


class ViewsMenuJoueur:
       
    def afficher_menu_joueur(self):
        print("-"*60) 
        print("                -- Menu Joueur --")  
        print("-"*60) 

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
            
    def affichage_creation_joueur(self):
        
        print('-'*60)
        print("                -- Création Joueur --")
        print('-'*60)
    
    
    def afficher_des_joueurs(self):
        """ désérialisation la liste des joueurs """
        
        print('-'*60)
        print('           -- Liste des joueurs --')
        print('-'*60)
        
           
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
            
        for index, joueur in enumerate(liste_joueurs["liste_joueurs"]):
            print(f" - Joueur n°{index + 1} : {joueur['prenom']} {joueur['nom']}")
            print(f"                Date de naissance : {joueur['date_de_naissance']}")
            print(f"                Genre : {joueur['genre']} - Classement : {joueur['classement']}")
            print(f"                Classement : {joueur['classement']}")
            
            
    def trier_joueurs_par_score(self):
        
        with open("data/liste_joueurs.json", "r") as f:        
            liste_joueurs = json.load(f)
        
        liste_joueurs_triee = sorted(liste_joueurs["liste_joueurs"], key=lambda x: x["classement"]) 
        
        print('-'*60)
        print('              -- Classement par score -- ') 
        print('-'*60) 
         
        for joueur in liste_joueurs_triee:
            print(f"{joueur['classement']} - {joueur['prenom']} {joueur['nom']}")
            
                
    # def demande_nouveau_joueur(self):
    #     autre_joueur = input("Souhaitez vous créer un autre joueur ? (o/n) : ")
    #     if autre_joueur == "o":
    #         print('Créer un nouveau joueur : ')
    #     elif autre_joueur == "n":
    #         print('Joueur créé avec succès !')
    #     else:
    #         print("Erreur : Veuillez entrer 'o' pour créer un autre joueur ou 'n' pour quitter.")

            
        
            
                
        
        
