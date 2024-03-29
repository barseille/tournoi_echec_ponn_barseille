from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_entree_tournoi import ViewsEntreeTournoi
from views.base_views import BaseViews
from database.database import Database
from models.tournoi import Tournoi


class ControllersTournois(BaseViews):
    def __init__(self):
        self.views_entree_tournoi = ViewsEntreeTournoi()
        self.views_menu_tournoi = ViewsMenuTournoi()

    def infos_tournoi(self):
        """Serialiser les informations du tournoi dans un dictionnaire"""

        self.nom = self.views_entree_tournoi.demander_nom_tournoi()
        self.lieu = self.views_entree_tournoi.demander_lieu_tournoi()
        self.dates = self.views_entree_tournoi.demander_dates_tournoi()
        self.nombres_de_rounds = self.views_entree_tournoi.demander_rounds()
        self.description = self.views_entree_tournoi.demander_description()
        self.mode_de_jeu = self.views_entree_tournoi.demander_mode_de_jeu()

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

    def recuperer_entree_tournoi(self):
        """Récupère les entrées utilisateur pour créer un nouveau tournoi"""

        # Affiche le menu de création du tournoi
        self.views_menu_tournoi.affichage_creation_tournoi()

        # Récupération de la création joueur
        self.tournoi = self.infos_tournoi()

        # sauvegarder les informations du tournoi
        self.sauvergarde()

        autre_tournoi = ""
        while True:
            autre_tournoi = input("Créer un autre tournoi ? (o/n) : ")
            if autre_tournoi in ["o", "n"]:
                break
            else:
                self.views_menu_tournoi.affichage_erreur_choix()

        if autre_tournoi == "o":
            msg = "Créer un nouveau tournoi : "
            self.views_entree_tournoi.afficher_msg(msg)
            self.recuperer_entree_tournoi()

        elif autre_tournoi == "n":
            msg = "********** Tournoi sauvegarder avec succès ! *********\n"
            self.views_entree_tournoi.afficher_msg(msg)

    def sauvergarde(self):
        data = Database()
        data.ecrire_database(self.tournoi, "liste_tournois", "data/liste_tournois.json")
