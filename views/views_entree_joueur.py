GENRE = ("homme", "femme")

def accueil_joueur():
    print("-"*40)
    print('       -- Créer votre joueur --')
    print("-"*40)


def creation_joueur_nom():
    try:
        nom = input('Entrez votre nom : ')
        return nom
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_joueur_prenom():
    try:
        prenom = input('Entrez votre prénom : ')
        return prenom
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_joueur_date_de_naissance():
    try:
        date_de_naissance = input('Entrez votre date de naissance (JJ-MM-AAAA): ')
        return date_de_naissance
    except ValueError:
        print('erreur - veuillez réessayer')


def creation_joueur_genre():
    options_utilisateur = 0

    def afficher_menu():
        for elt in GENRE:
            print(GENRE.index(elt) + 1, '-', elt)
    afficher_menu()
    
    try:
        options_utilisateur = int(input('Vous êtes un homme ou une femme : '))
        if options_utilisateur == 1:
            return options_utilisateur == GENRE[1]
        elif options_utilisateur == 2:
            return options_utilisateur == GENRE[2]
            
    except ValueError:
        print('Veuillez taper le chiffre correspondant !')

    return options_utilisateur

def creation_joueur_classement():

    try:
        classement = int(input("Entrez le numéro du joueur dans le classement : "))
        return classement
    except ValueError:
        print('erreur - veuillez réessayer')



            

