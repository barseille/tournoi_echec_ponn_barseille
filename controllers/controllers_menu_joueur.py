from tinydb import TinyDB
import views.views_entree_joueur as entree_joueur
from models.joueur import Joueur


def sauvegarder():
    
    entree_joueur.accueil_joueur()
    
    nom = entree_joueur.creation_joueur_nom()
    prenom = entree_joueur.creation_joueur_prenom()
    date_de_naissance = entree_joueur.creation_joueur_date_de_naissance()
    genre = entree_joueur.creation_joueur_genre()
    classement = entree_joueur.creation_joueur_classement()
    
    data = {"Nom": nom,
            "Prenom": prenom,
            "Date de naissance": date_de_naissance,
            "Genre": genre,
            "Classement": classement}
    
    joueur = Joueur(data)
    joueur_serialiser = joueur.serialiser()

    db = TinyDB("db.json")
    joueurs_table = db.table("Joueurs")
    joueurs_table.insert(joueur_serialiser)
    

    print("Joueur crée avec succes !")
    

def creation_autre_joueur():

    try:           
        options_utilisateur_utilisateur = input('Voulez vous créer un nouveau joueur? oui(o) / non(n)')
        options_utilisateur_utilisateur = str(options_utilisateur_utilisateur).lower()
        
        if options_utilisateur_utilisateur == 'o' or options_utilisateur_utilisateur == 'oui':
            return True
        elif options_utilisateur_utilisateur == 'n' or options_utilisateur_utilisateur == 'non':
            return False
        else:
            return False
        
    except ValueError:
        print('erreur - veuillez réessayer')