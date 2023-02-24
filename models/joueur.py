
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
    

    


