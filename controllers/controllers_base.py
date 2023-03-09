from views.views_menu_tournoi import ViewsMenuTournoi
from views.views_menu_joueur import ViewsMenuJoueur
from views.base_views import BaseViews
from .controllers_joueurs import ControllersJoueurs
from .controllers_tournois import ControllersTournois
from models.match import Match
from database.database import Database
from datetime import datetime
import random
import uuid


class ControllersBase:
    def __init__(self):
        self.joueur1 = None
        self.joueur2 = None
        self.controllers_joueurs = ControllersJoueurs()
        self.controllers_tournois = ControllersTournois()
        self.views_menu_joueur = ViewsMenuJoueur()
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.database = Database()
        self.base_views = BaseViews()
        self.paires_precedentes = []
        self.match = Match(self.joueur1, self.joueur2)
        self.match_info = []
        self.resultats_round = {}
        self.liste_matchs = []
        self.rounds_restants = 0

    def fusion_tournoi_avec_joueurs(self):
        # Générer un identifiant unique pour le tournoi
        id_tournoi = str(uuid.uuid4())

        # Demander à l'utilisateur de sélectionner un tournoi
        tournoi = self.database.lire_database("data/liste_tournois.json")
        tournoi_selectionne = self.views_menu_tournoi.afficher_les_tournois(tournoi)

        # Demander à l'utilisateur de sélectionner les joueurs
        joueur = self.database.lire_database("data/liste_joueurs.json")
        joueurs_selectionnes = self.views_menu_joueur.selectionner_participants(joueur)

        # Ajouter l'identifiant unique au tournoi sélectionné
        tournoi_selectionne["id"] = id_tournoi

        # Ajouter les joueurs sélectionnés au tournoi sélectionné
        tournoi_selectionne["joueurs"] = joueurs_selectionnes

        # Enregistrer le tournoi mis à jour dans la variable self.tournoi
        self.tournoi = tournoi_selectionne

    def enregistrer_temps_round(self):
        temps_round = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return temps_round

    def lancer_round(self):
        self.tournoi["resultats"] = {}
        self.round_termine = 0
        for i in range(self.tournoi["nombres_de_rounds"]):
            msg = f"                        -- ROUND {i + 1}/{self.tournoi['nombres_de_rounds']} --"
            titre = BaseViews()
            titre.presentation(msg)
            self.round_termine += 1

            # Ajouter le temps de début du round
            debut_round = self.enregistrer_temps_round()

            if i == 0:
                # Mélanger les joueurs pour le premier round
                random.shuffle(self.tournoi["joueurs"])
            else:
                # Trier les joueurs par score et par ordre alphabétique
                self.tournoi["joueurs"].sort(key=lambda x: x["score"], reverse=True)

            # Lancer les matchs pour chaque round
            self.lancer_match(self.tournoi["joueurs"])

            # Mise à joueur du classement en fonction des scores
            self.mise_a_jour_classement_joueur(self.tournoi["joueurs"])

            # Ajouter le temps de fin du round
            fin_round = self.enregistrer_temps_round()

            # Récupération des tuples (joueur, score)
            self.liste_matchs = self.score_joueur(self.tournoi["joueurs"])

            # Récupération des données des matchs
            self.resultats_round[f"Round {i+1}/{self.tournoi['nombres_de_rounds']}"] = {
                "matchs": self.match_info.copy(),
                "debut": debut_round,
                "fin": fin_round,
                "scores_joueurs": self.liste_matchs.copy(),
            }

            # Vider la liste des matchs pour le prochain round
            self.vider_listes_matchs()

            # Tant qu'il reste des rounds, demander à l'utilisateur s'il veut continuer
            if i < self.tournoi["nombres_de_rounds"] - 1:
                while True:
                    reponse = input(
                        "Voulez_vous continuer le prochain round ? (o/n) : "
                    )
                    if reponse == "o":
                        break
                    elif reponse == "n":
                        # Récupération  et sauvegarde du tournoi dans un dict
                        self.recup_tournoi_inacheve()
                        return
                    else:
                        self.base_views.affichage_erreur_choix()

        # Ajout du dict contenant les matchs au dict "resultats"
        self.tournoi["resultats"].update(self.resultats_round)

        # Ajout du statut "tournoi termine"
        self.tournoi["statut"] = "tournoi termine"

        # Ajout des rounds terminés
        self.tournoi["round_termine"] = self.round_termine

        # Ajout du tournoi dans base de données
        self.database.ecrire_database(self.tournoi, "liste_des_tournois", "data/historique_tournois.json")

        # Si on atteint le nombre total de rounds, on affiche le msg
        self.affichage_tournoi_termine(self.tournoi)

        return self.resultats_round

    # Affiche à l'utilisateur : "Terminé"
    def affichage_tournoi_termine(self, tournoi):
        if tournoi["nombres_de_rounds"]:
            self.base_views.affichage_termine()

    def lancer_match(self, joueurs):
        # Création de paire de joueurs
        paire = self.match.generer_paire(joueurs)

        # Mélanger aléatoirement les joueurs
        self.match.melanger_joueurs(joueurs)

        """
        Vérifiez si la paire de joueurs générée est identique à l'une des paires précédentes
        en vérifiant si elle est présente dans "self.paires_precedentes".
        Si la paire de joueurs est identique, vous mélangez à nouveau les joueurs
        et générez une nouvelle paire.
        """
        while paire and paire in self.paires_precedentes:
            self.match.melanger_joueurs(joueurs)
            paire = self.match.generer_paire(joueurs)

        """
        Ajoutez ensuite la paire de joueurs générée à "self.paires_precedentes"
        pour maintenir un historique des paires de joueurs précédentes.
        """
        self.paires_precedentes.append(paire)

        # Paire de joueurs générée pour saisir les scores du match
        self.match_info = self.match.saisir_scores(paire)

    # [(joueur, score)]
    def score_joueur(self, joueurs):
        liste_scores_joueurs = []
        for joueur in joueurs:
            nom = joueur["nom"]
            score = joueur["score"]
            liste_scores_joueurs.append((nom, score))
        return liste_scores_joueurs

    # Afficher un message
    def affichage_msg(self, msg):
        affiche = BaseViews()
        affiche.afficher_msg(msg)
        self.base_views.afficher_msg(msg)

    # Mise à jour du classement en fonction du score lors d'un tournoi
    def mise_a_jour_classement_joueur(self, joueurs):
        # Récupérer la liste des joueurs dans le tournoi
        joueurs = self.tournoi["joueurs"]

        # Trier la liste des joueurs par score décroissant, puis par ordre alphabétique croissant
        joueurs_tries = sorted(joueurs, key=lambda x: (-x["score"], x["nom"]))

        # Mettre à jour le classement des joueurs en fonction de leur position dans la liste triée
        for i, joueur in enumerate(joueurs_tries):
            joueur["classement"] = i + 1

        # Mettre à jour la liste des joueurs dans le tournoi avec la liste triée
        self.tournoi["joueurs"] = joueurs_tries

    # Effacer toutes les informations des matchs précédents et remettre à zéro
    def vider_listes_matchs(self):
        self.match_info.clear()
        self.liste_matchs.clear()

    # Récupération du tournoi dans database, si l'utilisateur décide de na poursuivre le tournoi
    def recup_tournoi_inacheve(self):
        self.tournoi_inacheve = {
            "nom": self.tournoi["nom"],
            "lieu": self.tournoi["lieu"],
            "dates": self.tournoi["dates"],
            "nombres_de_rounds": self.tournoi["nombres_de_rounds"],
            "description": self.tournoi["description"],
            "mode_de_jeu": self.tournoi["mode_de_jeu"],
            "id": self.tournoi["id"],
            "joueurs": self.tournoi["joueurs"],
            "resultats": self.resultats_round,
            "statut": "tournoi non termine",
            "round_termine": self.round_termine,
        }

        data = Database()
        data.ecrire_database(
            self.tournoi_inacheve, "non_termines", "data/non_termines.json"
        )

        return self.tournoi_inacheve
