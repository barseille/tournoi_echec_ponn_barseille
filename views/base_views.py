# éléments communs
class BaseViews:
    def afficher_msg(self, msg):
        print(msg)

    def presentation(self, affichage):
        print("-" * 60)
        print(affichage)
        print("-" * 60)

    def affichage_erreur_texte(self):
        print("Erreur ! Veuillez saisir des lettres alphabétiques")

    def affichage_erreur_choix(self):
        print('Erreur! Veuillez saisir "o" pour continuer ou "n" pour quitter')

    def affichage_erreur_type(self):
        print("Erreur ! Veuillez entrer un nombre entier valide")

    def affichage_erreur_numero(self):
        print("Erreur ! Veuillez saisir le numéro correspondant")

    def affichage_erreur_date(self):
        print("Veuillez la saisir au format jj/mm/aaaa.")

    def affichage_termine(self):
        print("************************** Terminé ************************\n")

    def retour_au_menu(self):
        input("Appuyez sur ENTREE pour revenir au menu")
