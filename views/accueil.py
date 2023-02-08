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
            
            
    def afficher_msg_erreur(self): 
        print("Erreur ! Veuillez saisir le chiffre correspondant à l'index")
  
        
    def retour_au_menu(self):   
        input("Appuyez sur une touche pour revenir au menu")
        
    def selectionner_choix(self):
         input("Faites votre choix : ") 
        
        
        
        
