TOURNOI_OPTIONS = (
    'Créer un nouveau tournoi',
    'Chercher un tournoi',
    'Retour'
)

class ViewsMenuTournoi:
    
    def afficher_menu_tournoi(self):
        
        print("-"*50)
        print("-- Menu Tournoi --" )
        print("-"*50)
        
        choix_utilisateur = 0
  
        print("Faite votre choix : ")

        
        for elt in TOURNOI_OPTIONS:
            print(TOURNOI_OPTIONS.index(elt) + 1, '-', elt)
            
