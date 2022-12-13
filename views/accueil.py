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
              
        choix_utilisateur = 0   
        
        print('Faite votre choix : ')
        
        for elt in OPTIONS:
            print(OPTIONS.index(elt) + 1 , '-', elt)
        
        # try:      
        #     choix_utilisateur = int(input('Saisir le chiffre correspondant : '))         
        # except Exception:
        #     print("Erreur ! Veuillez saisir un chiffre entre 1 et 3")
        #     return choix_utilisateur