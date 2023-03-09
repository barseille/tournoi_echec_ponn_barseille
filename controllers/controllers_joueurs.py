from views.views_entree_joueur import ViewsEntreeJoueur
from views.views_menu_joueur import ViewsMenuJoueur
from database.database import Database
from views.base_views import BaseViews
from models.joueur import Joueur


class ControllersJoueurs:

    def __init__(self):

        self.views_entree_joueur = ViewsEntreeJoueur()
        self.views_menu_joueur = ViewsMenuJoueur()
        self.database = Database()
        self.base_views = BaseViews()

    def infos_joueur(self):
        """Sérialiser les informations joueurs dans un dictionnaire"""

        self.nom = self.views_entree_joueur.creation_joueur_nom()
        self.prenom = self.views_entree_joueur.creation_joueur_prenom()
        self.date_de_naissance = self.views_entree_joueur.creation_joueur_date_de_naissance()
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

    def creation_joueur_classement(self):

        # Ouvrir le fichier liste_joueurs.json
        data = self.database.lire_database("data/liste_joueurs.json")

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
                        msg = "Le numéro de classement doit être entre 1 et 3000 inclus !"
                        self.base_views.afficher_msg(msg)
                else:
                    msg = "Le numéro de classement existe déjà !"
                    self.base_views.afficher_msg(msg)
                    continue
            except ValueError:
                self.base_views.affichage_erreur_type()

    def ajout_identifiant(self):

        data = self.database.lire_database("data/liste_joueurs.json")

        id_existant = []
        for id in data["liste_joueurs"]:
            id_existant.append(id["id"])

        while True:
            """
            méthode isdigit() vérifie si tous les caractères
            de cette chaîne sont des chiffres.
            """

            # AB12345
            id = input("Entrez un Identifiant à 5 chiffres : ")

            if id.isdigit() and len(id) == 5:
                id = "AB" + id
                if id not in id_existant:
                    return id
                else:
                    msg = "Cet identifiant existe déjà !"
                    self.base_views.afficher_msg(msg)
            else:
                msg = "Erreur ! Veuillez entrer exactement 5 chiffres."
                self.base_views.afficher_msg(msg)

    def recuperer_infos_joueur(self):
        """Récupère les entrées utilisateur pour créer un nouveau joueur"""

        # Affiche le menu de création de joueur
        self.views_menu_joueur.affichage_creation_joueur()

        # Récupération de la création joueur
        self.joueur = self.infos_joueur()

        # sauvegarder les informations du joueur(données, clé, chemin)
        self.database.ecrire_database(self.joueur, "liste_joueurs", "data/liste_joueurs.json")

        # Demande à l'utilisateur s'il veut créer un autre joueur
        choix = ""
        while True:
            choix = input("Souhaitez-vous créer un autre joueur ? (o/n) : ")
            if choix in ["o", "n"]:
                break
            else:
                self.views_menu_joueur.affichage_creation_joueur()

        if choix == "o":
            self.recuperer_infos_joueur()
        elif choix == "n":
            self.views_menu_joueur.affichage_joueur_cree()
