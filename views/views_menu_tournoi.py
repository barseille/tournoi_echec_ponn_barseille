TOURNOI_OPTIONS = (
    'Créer un nouveau tournoi',
    'Lancer un tournoi',
    'Retour'
)

class ViewsMenuTournoi:
    
    def afficher_menu_tournoi(self):
        
        print("-"*50)
        print("-- Menu Tournoi --" )
        print("-"*50)

        print("Faites votre choix : ")
  
        for elt in TOURNOI_OPTIONS:
            print(TOURNOI_OPTIONS.index(elt) + 1, '-', elt)
            
    
    def selectionner_tournoi_existant(self):
        try:
            entree = int(input("Saisir le numéro du tournoi : "))
            if entree > 0:
                return entree
            else:
                print("Veuillez saisir le numéro correspondant ! ")
        except ValueError:
            print("Veuillez saisir le numéro correspondant !")


