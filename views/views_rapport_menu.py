from .views_menu_tournoi import ViewsMenuTournoi
from .base_views import BaseViews


RAPPORT_OPTIONS = (
    "Liste de tous les joueurs par ordre alphabétique",
    "Liste de tous les tournois crées",
    "Liste des tournois terminés",
    "Retour",
)


class ViewsRapportMenu(BaseViews):
    def __init__(self):
        self.views_menu_tournoi = ViewsMenuTournoi()
        self.joueurs = []

    def afficher_menu_rapport(self):
        msg = "                -- Menu Rapport --"
        super().presentation(msg)

        for elt in RAPPORT_OPTIONS:
            print(RAPPORT_OPTIONS.index(elt) + 1, "-", elt)

    def affichage_joueur(self, joueur):
        msg = "         -- Classement des joueurs par ordre alphabetique --"
        super().presentation(msg)

        self.liste_joueurs = joueur["liste_joueurs"]
        self.liste_joueurs.sort(key=lambda joueur: joueur["nom"])

        if not self.liste_joueurs:
            print("Aucuns joueurs touvés !")
            return

        for i, joueur in enumerate(self.liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']}")

        # Demander à l'utilisateur de choisir un joueur par son index
        while True:
            try:
                choix = int(input("Choisissez un joueur pour plus d'infos : "))
                joueur_info = self.liste_joueurs[choix - 1]
                break
            except ValueError:
                super().affichage_erreur_type()
            except IndexError:
                super().affichage_erreur_numero()

        titre = "         -- Informations du joueur sélectionné --"
        super().presentation(titre)

        print(f"Joueur : {joueur_info['prenom']} {joueur_info['nom']}")
        print(f"Date de naissance : {joueur_info['date_de_naissance']}")
        print(f"Identifiant : {joueur_info['id']}\n")

    # Informations complète sur les tournois terminés
    def afficher_details_tournoi(self, tournoi):
        msg = "             -- Liste des tournois terminés --"
        super().presentation(msg)

        tournoi_termine = tournoi["liste_des_tournois"]

        if not tournoi_termine:
            print("Aucuns tournois trouvés !")
            return

        # Afficher tous les tournois terminés
        # i = 1
        for i, tournoi in enumerate(tournoi_termine):
            nom = tournoi["nom"]
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi {nom} - date(s) : {dates}")

        choix_tournoi = None
        while not choix_tournoi:
            try:
                choix_tournoi = int(input("Saisir un tournoi pour plus de détails : "))
                if choix_tournoi <= 0 or choix_tournoi > len(tournoi_termine):
                    print("Le numéro de tournoi saisi n'est pas valide.")
                    choix_tournoi = None
            except ValueError:
                print("Le numéro de tournoi saisi n'est pas valide.")
                choix_tournoi = None

        # Détails du tournoi sélectionné
        self.tournoi = tournoi_termine[choix_tournoi - 1]

        msg = "               -- Détails du tournoi terminé --"
        super().presentation(msg)

        # Afficher les informations du tournoi
        self.views_menu_tournoi.affichage_infos_tournoi(self.tournoi)

        # Afficher les matchs de chaque rounds
        self.infos_rounds()

        msg = "-- Classement des joueurs du tournoi par score --"
        super().presentation(msg)

        # Joueurs rangés par ordre alphabétique
        self.liste_joueurs = self.tournoi["joueurs"]
        self.liste_joueurs.sort(key=lambda joueur: joueur["score"], reverse=True)

        # Afficher les joueurs du tournoi
        for i, joueur in enumerate(self.liste_joueurs):
            print(
                f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Score : {joueur['score']}"
            )
        print("")

    # Informations détaillées de chaque match de chaque round
    def infos_rounds(self):
        msg = "               -- Résultats des matchs par rounds --"
        super().presentation(msg)

        resultats = self.tournoi["resultats"]

        for round, infos in resultats.items():
            print(f"{round} :")

            matchs = infos["matchs"]
            for match in matchs:
                joueur1, score1 = match[0][0], match[0][1]
                joueur2, score2 = match[1][0], match[1][1]
                print(f"{joueur1} VS {joueur2} = {score1} - {score2}")

            print(f"Début du round: {infos['debut']}")
            print(f"Fin du round: {infos['fin']}\n")

    def affichage_scores_joueurs(self, liste_joueurs):
        msg = "          -- Liste des joueurs --"
        super().presentation(msg)

        # Afficher les joueurs du tournoi
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['nom']} Score : {joueur['score']}")
