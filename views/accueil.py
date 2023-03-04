from .base_views import BaseViews

OPTIONS = (
    'Tournoi',
    'Joueur',
    'Rapport'
)

class ViewsAccueil(BaseViews):  
   
    def accueil_principal(self): 
      
        msg = "      -- Bienvenue dans le Menu Tournoi d'échec --" 
        super().presentation(msg)
      
        print('Faites votre choix : ')
        
        for elt in OPTIONS:
            print(OPTIONS.index(elt) + 1 , '-', elt)
            
            

        
        
        
        
