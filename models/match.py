import random
from views.base_views import BaseViews


class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueurs = []
        self.paires_de_joueurs = []
        self.score = 0
        self.matchs_joues = []
        self.paires_precedentes = []
        self.match_info = []

    def melanger_joueurs(self, joueurs):
        random.shuffle(joueurs)

    def generer_paire(self, joueurs):
        paires = []
        for i in range(0, len(joueurs), 2):
            joueur1 = joueurs[i]
            joueur2 = joueurs[i + 1]
            paires.append((joueur1, joueur2))
        return paires

    def saisir_scores(self, paire):
        for i, j in enumerate(paire):
            self.match_joueurs = f"Match {i+1} : {j[0]['prenom']} {j[0]['nom']} VS {j[1]['prenom']} {j[1]['nom']}"

            afficher = BaseViews()
            afficher.afficher_msg(self.match_joueurs)

            while True:
                choix = input(
                    "Choisissez le gagnant du match (1 pour J1, 2 pour J2 et 3 pour égalité) : "
                )
                try:
                    if choix == "1":
                        j[0]["score"] += 1

                        afficher.afficher_msg(
                            f"{j[0]['prenom']} {j[0]['nom']} a gagné\n"
                        )
                        self.match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(self.match_joueurs)
                        break

                    elif choix == "2":
                        j[1]["score"] += 1

                        afficher.afficher_msg(
                            f"{j[1]['prenom']} {j[1]['nom']} a gagné\n"
                        )
                        self.match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(self.match_joueurs)
                        break

                    elif choix == "3":
                        j[0]["score"] += 0.5
                        j[1]["score"] += 0.5

                        afficher.afficher_msg("Match nul !\n")
                        self.match_joueurs += f": {j[0]['score']} - {j[1]['score']}"
                        self.match_info.append(self.match_joueurs)
                        break

                    else:
                        afficher.afficher_msg("Veuillez taper 1, 2, 3")

                except ValueError:
                    afficher.afficher_msg("Veuillez taper 1, 2, 3")

        return self.match_info

    def affichage_msg(self, msg):
        affiche = BaseViews()
        affiche.afficher_msg(msg)
