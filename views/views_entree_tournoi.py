from datetime import datetime
from .base_views import BaseViews
from models.tournoi import Tournoi


class ViewsEntreeTournoi(BaseViews):
    def demander_nom_tournoi(self):
        while True:
            """
            Méthode isalpha() permet de vérifier
            si une chaîne de caractères contient
            uniquement des lettres alphabétiques.
            """

            nom = input("Entrez le nom du tournoi : ")
            if nom.isalpha():
                return nom
            else:
                super().affichage_erreur_texte()

    def demander_lieu_tournoi(self):
        while True:
            lieu = input("Entrez le lieu du tournoi : ")
            if lieu.isalpha():
                return lieu
            else:
                super().affichage_erreur_texte()

    def demander_dates_tournoi(self):
        while True:
            entree_date = input(
                "Saisir une date unique ou plage de dates ? unique(u) / plage(p): "
            )

            if entree_date not in ["u", "p"]:
                print("Entrer 'u' pour une date ou 'p' pour plage de dates.")
                continue

            # Saisie d'une seule date de tournoi
            if entree_date == "u":
                while True:
                    date_unique = input("Entrez la date au format (jj/mm/aaaa) : ")
                    try:
                        date = datetime.strptime(date_unique, "%d/%m/%Y")

                        # Conversion objet datetime en str
                        return date.strftime("%d/%m/%Y")
                    except ValueError:
                        super().affichage_erreur_date()

            # Saisie de début et de fin de tournoi
            elif entree_date == "p":
                plage_date = []
                while True:
                    date_debut = input("Entrez date de début au format (jj/mm/aaaa) : ")
                    try:
                        date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
                        plage_date.append(date_debut.strftime("%d/%m/%Y"))
                        break
                    except ValueError:
                        super().affichage_erreur_date()

                while True:
                    date_fin = input("Entrez date de fin au format (jj/mm/aaaa) : ")
                    try:
                        date_fin = datetime.strptime(date_fin, "%d/%m/%Y")
                        plage_date.append(date_fin.strftime("%d/%m/%Y"))
                        break
                    except ValueError:
                        super().affichage_erreur_date()

                return plage_date

    def demander_rounds(self):
        """
        méthode isdigit() vérifie si tous les caractères
        de cette chaîne sont des chiffres.
        """

        rounds = input("Saisir nombres de rounds ? (4 par défaut) ")

        # Si l'utilisateur n'a pas saisi de nombre, utilise 4 rounds par défaut
        if not rounds.isdigit():
            rounds = 4
        else:
            # Convertit la chaîne de caractères en entier
            rounds = int(rounds)

        print(f"Vous avez choisi de jouer {rounds} rounds.")
        return rounds

    def demander_description(self):
        description = input("Entrez la description : ")
        return description

    def demander_mode_de_jeu(self):
        mode_de_jeu = ["bullet", "blitz", "fast"]

        for i, mode in enumerate(mode_de_jeu):
            print(f"{i + 1} - {mode}")

        try:
            entree = int(input("Saisir mode de jeu par son index : "))
            if entree < 1 or entree > 3:
                raise ValueError
        except ValueError:
            super().affichage_erreur_numero()
            return self.demander_mode_de_jeu()

        return mode_de_jeu[entree - 1]

    def infos_tournoi(self):
        """Serialiser les informations du tournoi dans un dictionnaire"""

        self.nom = self.demander_nom_tournoi()
        self.lieu = self.demander_lieu_tournoi()
        self.dates = self.demander_dates_tournoi()
        self.nombres_de_rounds = self.demander_rounds()
        self.description = self.demander_description()
        self.mode_de_jeu = self.demander_mode_de_jeu()

        tournoi = Tournoi(
            self.nom,
            self.lieu,
            self.dates,
            self.nombres_de_rounds,
            self.description,
            self.mode_de_jeu,
        )

        self.tournoi = tournoi.afficher_tournoi()
        return self.tournoi
