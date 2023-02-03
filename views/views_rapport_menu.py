RAPPORT_OPTIONS = ("Liste de tous les joueurs par ordre alphabétique", 
                   "Liste de tous les tournois",
                   "Liste des tournois terminés")




class ViewsRapportMenu:
    
    def afficher_menu_rapport(self):
        print("-"*60) 
        print("                -- Menu Rapport --")  
        print("-"*60) 
        
        for elt in RAPPORT_OPTIONS:
            print(RAPPORT_OPTIONS.index(elt) + 1, '-', elt)
            
   
        
   