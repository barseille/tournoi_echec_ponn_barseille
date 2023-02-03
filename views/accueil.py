OPTIONS = (
    'Tournoi',
    'Joueur',
    'Rapport'
)

class ViewsAccueil:

    def accueil_principal(self): 
        print("-"*60) 
        print("      -- Bienvenue dans le Menu Tournoi d'échec --" )
        print("-"*60)
    
        
        print('Faites votre choix : ')
        
        for elt in OPTIONS:
            print(OPTIONS.index(elt) + 1 , '-', elt)
