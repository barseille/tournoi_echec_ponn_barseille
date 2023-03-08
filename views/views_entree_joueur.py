import datetime
from .base_views import BaseViews
from models.joueur import Joueur
from database.database import Database


class ViewsEntreeJoueur(BaseViews):
    def creation_joueur_nom(self):
        while True:
            """
            Méthode isalpha() vérifie
            si une chaîne de caractères contient
            uniquement des lettres alphabétiques.
            """
            nom = input("Entrez votre nom : ")
            if nom.isalpha():
                return nom
            else:
                super().affichage_erreur_texte()

    def creation_joueur_prenom(self):
        while True:
            prenom = input("Entrez votre prenom : ")
            if prenom.isalpha():
                return prenom
            else:
                super().affichage_erreur_texte()

    def creation_joueur_date_de_naissance(self):
        while True:
            try:
                date_de_naissance = input("Entrez date de naissance (jj/mm/aaaa): ")
                datetime.datetime.strptime(date_de_naissance, "%d/%m/%Y")
                return date_de_naissance
            except ValueError:
                super().affichage_erreur_date()

    def creation_joueur_classement(self):
        # Ouvrir le fichier liste_joueurs.json
        data = self.lire_database()
        classements_existants = []

        for joueur in data["liste_joueurs"]:
            classements_existants.append(joueur["classement"])

        """ On vérifie si le numéro du classement existe """
        while True:
            try:
                classement = int(input("Saisir numéro classement joueur : "))
                if classement not in classements_existants:
                    if 1 <= classement <= 3000:
                        return classement
                    else:
                        print(
                            "Le numéro de classement doit être entre 1 et 3000 inclus !"
                        )
                else:
                    print("Le numéro de classement existe déjà !")
                    continue
            except ValueError:
                super().affichage_erreur_type()

    def ajout_identifiant(self):
        # Ouvrir le fichier liste_joueurs.json
        data = self.lire_database()

        id_existant = []
        for id in data["liste_joueurs"]:
            id_existant.append(id["id"])

        while True:
            """
            méthode isdigit() vérifie si tous les caractères
            de cette chaîne sont des chiffres.
            """

            # AB12345
            id = input("Entrez un Id à 5 chiffres : ")
            if id.isdigit() and len(id) == 5:
                id = "AB" + id
                if id not in id_existant:
                    return id
                else:
                    print("Cet identifiant existe déjà !")
            else:
                print("Erreur : Veuillez entrer exactement 5 chiffres.")

    def lire_database(self):
        data_joueur = Database()
        data = data_joueur.lire_database("data/liste_joueurs.json")
        return data

    def infos_joueur(self):
        """Sérialiser les informations joueurs dans un dictionnaire"""

        self.nom = self.creation_joueur_nom()
        self.prenom = self.creation_joueur_prenom()
        self.date_de_naissance = self.creation_joueur_date_de_naissance()
        self.classement = self.creation_joueur_classement()
        self.id_joueur = self.ajout_identifiant()

        joueur = Joueur(
            self.nom,
            self.prenom,
            self.date_de_naissance,
            self.classement,
            self.id_joueur,
        )

        self.joueur = joueur.afficher_infos()
        return self.joueur
