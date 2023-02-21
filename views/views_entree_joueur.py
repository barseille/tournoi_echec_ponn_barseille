import datetime
from .base_views import BaseViews
from models.joueur import Joueur
from database.database import Database


class ViewsEntreeJoueur(BaseViews):

    def creation_joueur_nom(self):       
        try:
            nom = input('Entrez votre nom : ')
            return nom
        except ValueError:
            print('erreur - veuillez réessayer')

    def creation_joueur_prenom(self):        
        try:
            prenom = input('Entrez votre prénom : ')
            return prenom
        except ValueError:
            print('erreur - veuillez réessayer')

    def creation_joueur_date_de_naissance(self):    
        try:
            date_de_naissance = input('Entrez votre date de naissance au format jj/mm/aaaa : ')
            datetime.datetime.strptime(date_de_naissance, '%d/%m/%Y')
            return date_de_naissance
        except ValueError:
            print("La date entrée n'est pas valide, veuillez la saisir au format jj/mm/aaaa.")
            return

    def creation_joueur_classement(self):  
        
        # Ouvrir le fichier liste_joueurs.json
        data = self.sauvegarde()
         
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
                
    def ajout_identifiant(self):     
     
        # Ouvrir le fichier liste_joueurs.json
        data = self.sauvegarde()
          
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
                
    def sauvegarde(self):
        
        data_joueur = Database()
        data = data_joueur.lire_database(chemin_fichier="data/liste_joueurs.json")
        return data
                
    def infos_joueur(self):
        """ Afficher les informations joueurs dans un dictionnaire """
        
        self.nom = self.creation_joueur_nom()
        self.prenom = self.creation_joueur_prenom()
        self.date_de_naissance = self.creation_joueur_date_de_naissance()
        self.classement = self.creation_joueur_classement()
        self.id_joueur = self.ajout_identifiant()
           
        joueur = Joueur(self.nom,
                        self.prenom,
                        self.date_de_naissance,
                        self.classement,
                        self.id_joueur)

        self.joueur_creer = joueur.afficher_infos()
        return self.joueur_creer
   
    
   

 
