from views.base_views import BaseViews
from .controllers_base import ControllersBase
from models.match import Match
from database.database import Database
from views.views_menu_tournoi import ViewsMenuTournoi
import json


class ControllersReprise(ControllersBase):
    def __init__(self):
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.database = Database()
        self.joueur1 = None
        self.joueur2 = None
        self.match = Match(self.joueur1, self.joueur2)
        self.paires_precedentes = []
        self.base_views = BaseViews()
        self.match_info = []
        self.data_tournoi = {}
        self.resultats_round = {}
        self.joueurs = []
        self.tournois_non_termines = []

    def reprendre_tournoi(self):
        data = self.database.lire_database("data/non_termines.json")

        while True:
            # S'il n'y a aucuns tournois dans la base de données
            if not data["non_termines"]:
                msg = "****** Aucun tournoi dans la base de données *******"
                self.base_views.afficher_msg(msg)
                return

            # Recherche des tournois inachevés
            for tournoi in data["non_termines"]:
                if tournoi["statut"] == "tournoi non termine":
                    self.tournois_non_termines.append(tournoi)

            # S'il n'y a aucuns tournois avec le statut "tournoi non terminé"
            if not self.tournois_non_termines:
                msg = "Aucuns tournois inachevés dans la base de données !"
                self.base_views.afficher_msg(msg)
                return

            # Afficher tous les tournois inachevés
            for i, tournoi in enumerate(self.tournois_non_termines):
                liste = f'{i + 1}. Nom du tournoi : {tournoi["nom"]} - Dates: {tournoi["dates"]}'
                self.base_views.afficher_msg(liste)
            print("")

            try:
                choix = int(
                    input(
                        "Quel tournoi souhaitez-vous continuer (choisir son numéro) ? "
                    )
                )
                self.tournoi = self.tournois_non_termines[choix - 1]

                # Information du tournoi
                self.base_views.presentation(
                    "            -- Informations du tournoi --"
                )
                self.views_menu_tournoi.affichage_infos_tournoi(self.tournoi)

                # Information des joueurs du tournoi
                self.base_views.presentation("                   -- Joueurs --")
                self.views_menu_tournoi.affichage_joueurs(self.tournoi)

                # Historique des rounds du tournoi
                msg = "            -- Historique des rounds --"
                self.base_views.presentation(msg)

                # Récupération du tournoi précédent
                self.recup_tournoi_en_cours()

                # Informations des rounds restants
                self.historique_rounds()

                # Reprendre le tournoi en cours
                self.continuer_tournoi()
                break

            except ValueError:
                self.base_views.affichage_erreur_type()

            except IndexError:
                self.base_views.affichage_erreur_numero()
            break

    # Récupération des données du tournoi en cours
    def recup_tournoi_en_cours(self):
        self.data_tournoi = {
            "nom": self.tournoi.get("nom", ""),
            "lieu": self.tournoi.get("lieu", ""),
            "dates": self.tournoi.get("dates", ""),
            "nombres_de_rounds": self.tournoi.get("nombres_de_rounds", ""),
            "description": self.tournoi.get("description", ""),
            "mode_de_jeu": self.tournoi.get("mode_de_jeu", ""),
            "id": self.tournoi.get("id", ""),
            "joueurs": self.tournoi.get("joueurs", ""),
            "resultats": self.tournoi.get("resultats", []),
            "statut": self.tournoi.get("statut", ""),
            "round_termine": self.tournoi.get("round_termine", []),
        }

        return self.data_tournoi

    # Informations des rounds du tournoi en cours
    def historique_rounds(self):
        self.rounds_totals = self.data_tournoi.get("nombres_de_rounds", "")
        self.round_termine = self.data_tournoi.get("round_termine", "")
        self.rounds_restants = self.rounds_totals - self.round_termine

        self.base_views.afficher_msg(f"Nombres totals de rounds : {self.rounds_totals}")
        self.base_views.afficher_msg(f"Round(s) terminé(s) : {self.round_termine}")
        self.base_views.afficher_msg(f"Round(s) restant(s) : {self.rounds_restants}\n")

    # Reprise du tournoi
    def continuer_tournoi(self):
        while True:
            reponse = input("Voulez-vous continuer le tournoi ? (o/n) : ")
            if reponse == "o":
                self.lancer_tournoi()
            elif reponse == "n":
                self.base_views.affichage_termine()
                return False
            else:
                self.base_views.affichage_erreur_choix()
            break

    # Démarrage du tournoi
    def lancer_tournoi(self):
        # Boucle sur les rounds restants
        for i in range(self.rounds_restants):
            msg = f"                   -- ROUND {self.round_termine + 1 + i}/{self.rounds_totals} --"
            self.base_views.presentation(msg)

            # Ajouter le temps de début du round
            debut_round = self.enregistrer_temps_round()

            # Trier les joueurs par score en ordre décroissant
            self.data_tournoi["joueurs"].sort(key=lambda x: x["score"], reverse=True)

            # Lancer les matchs pour chaque round
            self.lancer_match(self.data_tournoi["joueurs"])

            # Mise à joueur du classement en fonction des scores
            self.mise_a_jour_classement_joueur(self.data_tournoi)

            # Ajouter le temps de fin du round
            fin_round = self.enregistrer_temps_round()

            # Ajouter les résultats du round au dictionnaire resultats_round
            self.resultats_round[
                f"Round {self.round_termine + i + 1}/{self.rounds_totals}"
            ] = {
                "matchs": self.match_info.copy(),
                "debut": debut_round,
                "fin": fin_round,
                # "scores_joueurs": self.liste_matchs.copy(),
            }

            # Vider la liste des matchs pour le prochain round
            self.vider_listes_matchs()

            # Tant qu'il reste des rounds, demander à l'utilisateur s'il veut continuer
            if i + 1 < self.rounds_restants:
                while True:
                    reponse = input(
                        "Voulez_vous continuer le prochain round ? (o/n) : "
                    )
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        # Ajout du dict contenant les matchs au dict "resultats"
                        self.data_tournoi["resultats"].update(self.resultats_round)

                        # Ajout du statut "tournoi non termine"
                        self.data_tournoi["statut"] = "tournoi non termine"

                        # Informations des rounds terminés
                        self.data_tournoi["round_termine"] = self.round_termine + i + 1

                        # "Terminé"
                        self.base_views.affichage_termine()

                        # Sauvegarder data
                        self.sauvegarde_tournoi_non_termines()

                        # Effacer les données avec le même id
                        self.effacer_tournoi()

                        return
                    else:
                        self.base_views.affichage_erreur_choix()

        # Ajout du dict contenant les matchs au dict "resultats"
        self.data_tournoi["resultats"].update(self.resultats_round)

        # Ajout du statut "tournoi non termine"
        self.data_tournoi["statut"] = "tournoi termine"

        # Informations des rounds terminés
        self.data_tournoi["round_termine"] = self.round_termine + i + 1

        # Sauvegarder data
        self.sauvegarde_tournoi_termines()

        # Effacer les données avec le même id
        self.effacer_tournoi()

        # "Terminé"
        self.affichage_tournoi_termine(self.data_tournoi)

    def sauvegarde_tournoi_non_termines(self):
        self.database.ecrire_database(
            self.data_tournoi,
            cle="non_termines",
            chemin_fichier="data/non_termines.json",
        )

    def sauvegarde_tournoi_termines(self):
        self.database.ecrire_database(
            self.data_tournoi,
            cle="liste_des_tournois",
            chemin_fichier="data/historique_tournois.json",
        )

    def effacer_tournoi(self):
        """
        Supprimer le tournoi non terminé
        dans la liste "non_termines",
        en supprimant le tournoi correspondant à l'Id
        et en sauvegardant la nouvelle liste de tournois non terminés dans le fichier.
        """
        with open("data/non_termines.json", "r") as f:
            data = json.load(f)

        for tournoi in data["non_termines"]:
            if tournoi["id"] == self.data_tournoi["id"]:
                data["non_termines"].remove(tournoi)

        with open("data/non_termines.json", "w") as f:
            json.dump(data, f, indent=4)

    # Mise à jour du classement en fonction du score lors d'un tournoi
    def mise_a_jour_classement_joueur(self, joueurs):
        # Récupérer la liste des joueurs dans le tournoi
        joueurs = self.data_tournoi["joueurs"]

        # Trier la liste des joueurs par score décroissant, puis par ordre alphabétique croissant
        joueurs_tries = sorted(joueurs, key=lambda x: (-x["score"], x["nom"]))

        # Mettre à jour le classement des joueurs en fonction de leur position dans la liste triée
        for i, joueur in enumerate(joueurs_tries):
            joueur["classement"] = i + 1

        # Mettre à jour la liste des joueurs dans le tournoi avec la liste triée
        self.data_tournoi["joueurs"] = joueurs_tries
