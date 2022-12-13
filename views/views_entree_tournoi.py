from models.tournoi import MODE_DE_JEU



    
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


def creation_date_debut_tournoi():
    try:
        date_debut_tournoi = input('Entrez la date de début du tournoi (JJ-MM-AAAA): ')
        return date_debut_tournoi
    except ValueError:
        print('erreur - veuillez réessayer')
        
def creation_date_fin_tournoi():
    try:
        date_fin_tournoi = input('Entrez la date de fin du tournoi (JJ-MM-AAAA): ')
        return date_fin_tournoi
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_nombre_de_rounds():     
    try:
        nombre_de_rounds = int(input("Entrez le nombre de round : "))
        return nombre_de_rounds
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_description():      
    try:
        description = input("Entrez la description : ")
        return description
    except ValueError:
        print('erreur - veuillez réessayer')


def selection_mode_de_jeu():      
    options_utilisateur = 0

    def afficher_menu():
        for elt in MODE_DE_JEU:
            print(MODE_DE_JEU.index(elt), '-', elt)
    afficher_menu()
    
    try:
        options_utilisateur = int(input('Sélectionnez le mode de jeu par le chiffre correspondant : '))
    except ValueError:
        print('Veuillez le bon chiffre')
    return options_utilisateur


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


