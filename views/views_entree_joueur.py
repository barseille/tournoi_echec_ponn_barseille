import datetime
from .base_views import BaseViews


class ViewsEntreeJoueur(BaseViews):

    def creation_joueur_nom(self):

        while True:
            nom = input("Entrez votre nom : ")
            if len(nom) <= 50:
                return nom
            else:
                super().affichage_erreur_texte()

    def creation_joueur_prenom(self):

        while True:
            prenom = input("Entrez votre prenom : ")
            if len(prenom) <= 50:
                return prenom
            else:
                super().affichage_erreur_texte()

    def creation_joueur_date_de_naissance(self):

        while True:
            try:
                date_de_naissance = input("Entrez la date de naissance (jj/mm/aaaa): ")
                datetime.datetime.strptime(date_de_naissance, "%d/%m/%Y")
                return date_de_naissance
            except ValueError:
                super().affichage_erreur_date()
