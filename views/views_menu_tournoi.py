import json



TOURNOI_OPTIONS = (
    'Créer un nouveau tournoi',
    'Lancer un nouveau tournoi',
    'Relancer un tournoi existant',
    'Retour'
)

class ViewsMenuTournoi:
    
    def afficher_menu_tournoi(self):
        
        print("-"*60)
        print("              -- Menu Tournoi --")
        print("-"*60)

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
  
            
    def affichage_creation_tournoi(self):
        
        print('-'*60)
        print("                -- Création Tournoi --")
        print('-'*60)
     
        
    def afficher_les_tournois(self):
        """deserialiser la liste des tournois"""
        
        print('-'*60)
        print('                -- Liste des tournois --')
        print('-'*60)
        
        with open ("data/liste_tournois.json", "r") as f:
            self.liste_tournois = json.load(f)       
    
        # Accéder aux index, aux clés et aux valeurs d'un dictionnaire
        for index, tournoi in enumerate(self.liste_tournois["liste_tournois"]):
            print(f"Tournoi n°{index} : {tournoi['nom']}")
            print(f"              Date(s) : {tournoi['dates']}")
            print(f"              Lieu : {tournoi['lieu']}")
            print(f"              Nombres de rounds : {tournoi['nombres_de_rounds']}")
            print(f"              Description : {tournoi['description']}")
            print(f"              Mode de jeu : {tournoi['mode_de_jeu']}\n")
    
            
    def selectionner_tournoi(self):
        """ afficher la liste des tournois"""
        
        # Charger le fichier JSON dans une variable
        with open('data/liste_tournois.json', 'r') as f:
            tournois_data = json.load(f)

        # Récupérer la liste des tournois
        self.liste_tournois = tournois_data['liste_tournois']

        # Afficher la liste des tournois
        for i, tournoi in enumerate(self.liste_tournois):
            print(f"Tournoi {i+1}: {tournoi['nom']}")

        # Demander à l'utilisateur de choisir un tournoi par son index
        while True:
            try:
                choix_tournoi = int(input("Choisissez un tournoi par son index: "))
                self.tournoi_selectionne = self.liste_tournois[choix_tournoi -1]
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide")
            except IndexError:
                print("L'index choisi n'est pas valide")

        
        print('-'*60)
        print("         -- Informations du Tournoi sélectionné --")
        print('-'*60)
        
        print(f"Nom du tournoi : {self.tournoi_selectionne['nom']}")
        print(f"Lieu du tournoi : {self.tournoi_selectionne['lieu']}")
        print(f"Date(s) du tournoi : {self.tournoi_selectionne['dates']}")
        print(f"Nombres de rounds : {self.tournoi_selectionne['nombres_de_rounds']}")
        print(f"Description : {self.tournoi_selectionne['description']}")
        print(f"Mode de jeu : {self.tournoi_selectionne['mode_de_jeu']}")
      
        return self.tournoi_selectionne



    
 
            

    
    


            
            
            
            




