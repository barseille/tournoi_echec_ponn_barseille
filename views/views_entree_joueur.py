import json
import datetime
from .base_views import BaseViews

GENRE = ("homme", "femme")
# erreur = ""
# erreur = BaseViews()
# erreur.affichage_erreur()


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
        date_de_naissance = input('Entrez votre date de naissance au format jj/mm/aaaa : ')
        datetime.datetime.strptime(date_de_naissance, '%d/%m/%Y')
        return date_de_naissance
    except ValueError:
        print("La date entrée n'est pas valide, veuillez la saisir au format jj/mm/aaaa.")
        creation_joueur_date_de_naissance()


def creation_joueur_genre():
    
    genre = ["homme", "femme"]
    
    def afficher_menu():
        for elt in genre:
            print(genre.index(elt) + 1, '-', elt)

    afficher_menu()

    try:
        entree = int(input('Veuillez saisir, 1 pour homme ou 2 pour femme : '))
        
        if entree == 1:
            entree = genre[0]
            print(f'Vous avez saisie {genre[0]}')
        elif entree == 2:
            entree = genre[1]
            print(f'Vous avez saisie {genre[1]}')
        else:
            print("Erreur ! Recommencez")
            return creation_joueur_genre()  
           
    except ValueError:
        print('Veuillez taper le chiffre correspondant !')
        return creation_joueur_genre()
    
    return entree



def creation_joueur_classement():
      
    with open("data/liste_joueurs.json", "r") as f:
        data = json.load(f)
        
        classements_existants = []
        
        for joueur in data['liste_joueurs']:
            classements_existants.append(joueur['classement'])     
              
    while True:
        try:
        
            classement = int(input("Entrez le numéro du joueur dans le classement : "))
        
            if classement not in classements_existants:
                return classement 
            else:
                print("Le numéro de classement existe déjà. Veuillez réessayer.")
                continue
                
        except ValueError:
            print('erreur - veuillez réessayer')
            
def ajout_identifiant():
    
    with open("data/liste_joueurs.json", "r") as f:
        data = json.load(f)
        
        id_existant = []
        
        for id in data['liste_joueurs']:
            id_existant.append(id['id'])
            
    while True:
        """
        méthode isdigit() est une fonction Python qui s'applique à une chaîne de caractères 
        et vérifie si tous les caractères de cette chaîne sont des chiffres.
        Elle retourne True si la chaîne est constituée uniquement de chiffres, 
        sinon elle retourne False
        """

        id = input("Entrez un nombre à 5 chiffres : ")
        if id.isdigit() and len(id) == 5:
            id = "AB" + id
            if id not in id_existant:
                return id
            else:
                print("Cet identifiant existe déjà. Veuillez en choisir un autre.")
        else:
            print("Erreur : Veuillez entrer exactement 5 chiffres.")

 
    
   
    
   

 
