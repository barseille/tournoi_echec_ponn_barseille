
def creation_nom_tournoi():  
    try:
        nom = input('Entrez le nom du tournoi :')
        return nom
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_lieu_tournoi():
    try:
        lieu = input('Entrez le lieu du tournoi : ')
        return lieu
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_date_debut_tournoi():
    try:
        date_debut_tournoi = input("Saisissez une date (JJ-MM-AAAA): ")
        return date_debut_tournoi
    except ValueError:
        print('erreur - veuillez réessayer')
        
     
def creation_date_fin_tournoi():
    entree = input("Voulez-vous sélectionner una date de fin de tournoi ?  o(oui) / n(non) ")
    if entree == 'o':
        date_fin_tournoi = input("Saisissez une date (JJ-MM-AAAA): ")
        return date_fin_tournoi
    elif entree == "n":
        pass
    else:
        print("Veuillez saisir correctement")
        creation_date_fin_tournoi()
    

def creation_nombres_de_rounds():     
    try:
        rounds = 4
        nombres_de_rounds = int(input("Entrez le nombre de rounds : "))
        if nombres_de_rounds is not 4:
            print(f'Vous avez saisie {nombres_de_rounds} rounds')
            return nombres_de_rounds

        else:
            nombres_de_rounds = rounds
            print("4 rounds par défaut")
        
        return nombres_de_rounds
    except ValueError:
        print('erreur - veuillez réessayer')
        return creation_nombres_de_rounds()


def creation_description():      
    try:
        description = input("Entrez la description : ")
        return description
    except ValueError:
        print('erreur - veuillez réessayer')


def selection_mode_de_jeu():

    mode_de_jeu = ["bullet", "blitz", "fast"]

    def afficher_menu():
        for elt in mode_de_jeu:
            print(mode_de_jeu.index(elt) + 1, '-', elt)

    afficher_menu()

    try:
        entree = int(input('Sélectionnez le mode de jeu par le chiffre correspondant : '))
        if entree == 1:
            entree = mode_de_jeu[0]
            print(f'Vous avez saisie {mode_de_jeu[0]}')
        elif entree == 2:
            entree = mode_de_jeu[1]
            print(f'Vous avez saisie {mode_de_jeu[1]}')
        elif entree == 3:
            entree = mode_de_jeu[2]
            print(f'Vous avez saisie {mode_de_jeu[2]}')
        else:
            print("Erreur ! Recommencez")
            return selection_mode_de_jeu()
    except ValueError:
        print('Veuillez saisir un chiffre entre 1 et 3 !')
        return selection_mode_de_jeu()
    return entree


 
        
        
        


