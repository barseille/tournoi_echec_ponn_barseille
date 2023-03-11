from .base_views import BaseViews

JOUEUR_OPTIONS = ("Créer un joueur", "Informations sur les joueurs", "Retour")


class ViewsMenuJoueur(BaseViews):
    def __init__(self):
        self.liste_des_joueurs = []
        self.rencontre = {}
        self.nombre_joueurs = 8

    def afficher_menu_joueur(self):
        titre = "                -- Menu Joueur --"
        super().presentation(titre)

        for elt in JOUEUR_OPTIONS:
            print(JOUEUR_OPTIONS.index(elt) + 1, "-", elt)

    # Titre
    def affichage_creation_joueur(self):
        titre = "                -- Création Joueur --"
        super().presentation(titre)

    # Sélectionner participants pour le tournoi
    def selectionner_participants(self, liste_joueurs):
        titre = "               -- Liste des joueurs --"
        super().presentation(titre)

        # Récupérer la clé liste des joueurs
        self.liste_joueurs = liste_joueurs["liste_joueurs"]

        for i, joueur in enumerate(self.liste_joueurs):
            print(f"Joueur {i+1}: {joueur['prenom']} {joueur['nom']}")
        print("")

        # L'utilisateur doit choisir 8 joueurs
        print(f"Sélectionnez {self.nombre_joueurs} joueurs dans la liste ci-dessus\n")

        i = 1
        while i <= self.nombre_joueurs:
            try:
                choix_joueur = int(input("Saisir un joueur par son index : "))
                joueur_selectionne = self.liste_joueurs[choix_joueur - 1]

                # Vérifier si le joueur a déjà été sélectionné
                if joueur_selectionne in self.liste_des_joueurs:
                    print("Saisir un autre joueur.\n")
                else:
                    self.liste_des_joueurs.append(joueur_selectionne)
                    print("Joueur ajouté avec succès !\n")
                    i += 1
            except ValueError:
                super().affichage_erreur_type()

            except IndexError:
                super().affichage_erreur_numero()

        titre = "       -- Liste des joueurs sélectionnés --"
        super().presentation(titre)

        for i, joueur in enumerate(self.liste_des_joueurs):
            print(f"Joueur {i+1}: {joueur['nom']}")
        print("")

        return self.liste_des_joueurs

    def affichage_joueur_cree(self):
        print("******** Joueur créé avec succès ! ********\n")

    def afficher_infos_joueurs(self, joueurs):
        """Informations détaillées sur les joueurs"""

        titre = "  -- Liste des joueurs triés par ordre alphabetique --"
        super().presentation(titre)

        joueurs["liste_joueurs"].sort(key=lambda joueur: joueur["nom"])

        for joueur in joueurs["liste_joueurs"]:
            print(f"{joueur['prenom']} {joueur['nom']}")
            print(f"Date de naissance : {joueur['date_de_naissance']}")
            print(f"Identifiant : {joueur['id']}\n")
