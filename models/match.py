

class Match:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.paires_de_joueurs = []

    def ajouter_paire_joueurs(self, joueur1, joueur2):
        if (joueur1, joueur2) in self.paires_de_joueurs or (joueur2, joueur1) in self.paires_de_joueurs:
            print("La paire existe déjà.")
        else:
            self.paires_de_joueurs.append((joueur1, joueur2))
            return self.paires_de_joueurs

    def choisir_score(self):
        choix = input(
            "Choisissez le gagnant du match (1 pour J1, 2 pour J2, ENTREE pour égalité) : ")
        try:
            if choix == "1":
                self.joueur1.score += 1
                print("Joueur1 gagne")
            elif choix == "2":
                self.joueur2.score += 1
                print("Joueur2 gagne")
            elif choix == "3":
                self.joueur1.score += 0.5
                self.joueur2.score += 0.5
                print("match nul")
            else:
                return
        except ValueError:
            print("Erreur de frappe")