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
