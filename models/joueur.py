
class Joueur:
    
    def __init__(self, nom, prenom, date_de_naissance, classement, id):
        
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.classement = classement
        self.id = id
        self.opposants = []
        self.points = 0
        

    def serialiser(self):

        joueur_serialiser = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_de_naissance': self.date_de_naissance,
            'classement': self.classement,
            'score': 0,
            'id': self.id
        }
        return joueur_serialiser
    
    def ajouter_points(self, points):
        self.points += points
        
    def ajouter_opposant(self, opposant):
        self.opposants.append(opposant)
        
    def deja_jouer_contre(self, opposant):
        return opposant in self.opposants

