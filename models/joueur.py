
class Joueur:

    def __init__(self, nom, prenom, date_de_naissance, classement, id):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.classement = classement
        self.id = id
        self.opposants = []
        self.score = 0

    def afficher_infos(self):
        joueur_infos = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_de_naissance': self.date_de_naissance,
            'classement': self.classement,
            'score': self.score,
            'id': self.id
        }
        return joueur_infos
    
class Match(Joueur):

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
    
    # def ajouter_points(self, points):
    #     self.points += points
        
    # def ajouter_opposant(self, opposant):
    #     self.opposants.append(opposant)
        
    # def deja_jouer_contre(self, opposant):
    #     return opposant in self.opposants

