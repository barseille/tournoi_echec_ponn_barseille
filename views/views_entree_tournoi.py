from datetime import datetime



def demander_nom_tournoi():
    nom = input('Entrez le nom du tournoi : ')
    return nom


def demander_lieu_tournoi():
    lieu = input('Entrez le lieu du tournoi : ')
    return lieu


def demander_dates_tournoi():
    
    entree_date = input("Souhaitez-vous entrer une date unique ou une plage de dates ? u(unique)/ p(plage de date) : ")

    if entree_date == 'u':   
        
        while True:
            date_unique = input("Entrez la date unique au format jj/mm/aaaa : ")
            try:
                date = datetime.strptime(date_unique, "%d/%m/%Y")
                return date_unique
            except ValueError:
                print("La date n'est pas au bon format (jj/mm/aaaa).")

    elif entree_date == 'p': 
        
        plage_date = []   
        while True:
            date_debut = input("Entrez la date de début au format jj/mm/aaaa : ")
            try:
                date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
                plage_date.append(date_debut)
                break
            except ValueError:
                print("La date de début n'est pas au bon format (jj/mm/aaaa).")

        while True:
            date_fin = input("Entrez la date de fin au format jj/mm/aaaa : ")
            try:
                date_fin = datetime.strptime(date_fin, "%d/%m/%Y")
                plage_date.append(date_fin)
                break
            except ValueError:
                print("La date de fin n'est pas au bon format (jj/mm/aaaa).")

        return plage_date




def demander_rounds():
  rounds = input("Combien de rounds souhaitez-vous jouer ? (4 par défaut) ")

  # Si l'utilisateur n'a pas saisi de nombre, utilise 4 rounds par défaut
  if not rounds.isdigit():
    rounds = 4
  else:
    # Convertit la chaîne de caractères en entier
    rounds = int(rounds)

  print(f"Vous avez choisi de jouer {rounds} rounds.")
  return rounds


def demander_description():      
    try:
        description = input("Entrez la description : ")
        return description
    except ValueError:
        print('erreur - veuillez réessayer')
        
    return description


def demander_mode_de_jeu():
    mode_de_jeu = ["bullet", "blitz", "fast"]

    for i, mode in enumerate(mode_de_jeu):
        print(f"{i + 1} - {mode}")

    try:
        entree = int(input('Sélectionnez le mode de jeu par le chiffre correspondant : '))
        if entree < 1 or entree > 3:
            raise ValueError
    except ValueError:
        print('Veuillez saisir un chiffre entre 1 et 3 !')
        return demander_mode_de_jeu()

    return mode_de_jeu[entree - 1]










        
        
        


