
def bienvenue():
    print('-'*40)
    print("-- Créer votre Nouveau Tournoi --")
    print('-'*40)


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


def creation_date_tournoi():

    date_tournoi = input("Saisissez une date (JJ-MM-AAAA): ")
    entree = input("Voulez-vous sélectionner una autre date ?  o(oui) / n(non) ")
    if entree == 'o':
        return creation_date_tournoi()
    elif entree == "n":
       
        return date_tournoi
    else:
        print("Veuillez saisir correctement")


def creation_nombre_de_rounds():     
    try:
        rounds = 4
        nombre_de_rounds = int(input("Entrez le nombre de rounds : "))
        if nombre_de_rounds is not 4:
            print(f'Vous avez saisie {nombre_de_rounds} rounds')
            return nombre_de_rounds

        else:
            nombre_de_rounds = rounds
            print("4 rounds par défaut")
        
        return nombre_de_rounds
    except ValueError:
        print('erreur - veuillez réessayer')
        return creation_nombre_de_rounds()


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



def creation_autre_tournoi():
    
    autre_tournoi = input("Voulez-vous créer un autre tournoi ? o(oui) / n(non)")
    
    if autre_tournoi == "o":
        return True
        
    elif autre_tournoi == "n":
        return False
    else:
        print("Veuillez saisir correctement ! ")
 
  






def creation_tournoi_confirmee():
    try:
        print("Tournoi crée avec succes !")
        entree_utilisateur = input('Voulez-vous lancer ce tournoi ? oui(o) / non(n)')
        entree_utilisateur = str(entree_utilisateur).lower()
        if entree_utilisateur == 'o' or entree_utilisateur == 'oui':
            return True
        elif entree_utilisateur == 'n' or entree_utilisateur == 'non':
            return False
        else:
            return False
    except ValueError:
        print('erreur - veuillez réessayer')
        
        
        


