JOUEUR_OPTIONS = (
    'Créer un joueur',
    'Charger un joueur existant',
    'Mise à jour classement joueur',
    'Retour'
)


class ViewsMenuJoueur:
       
    def afficher_menu_joueur(self):
        print("-"*50) 
        print("                -- Menu Joueur --")  
        print("-"*50) 

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, '-', elt)
