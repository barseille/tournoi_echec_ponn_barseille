OPTIONS = (
    'Tournoi',
    'Joueur',
    'Rapports'
)

class ViewsAccueil:

    def accueil_principal(self): 
        print("-"*50) 
        print("  -- Bienvenue dans le Menu Tournoi d'échec --" )
        print("-"*50)
    
        
        print('Faite votre choix : ')
        
        for elt in OPTIONS:
            print(OPTIONS.index(elt) + 1 , '-', elt)
