
class Joueur:
    
    def __init__(self, nom, prenom, date_de_naissance, genre, classement):
        
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.genre = genre
        self.classement = classement
        


    def serialiser(self):

        joueur_serialiser = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_de_naissance': self.date_de_naissance,
            'genre': self.genre,
            'classement': self.classement,
            'score': 0
        }
        return joueur_serialiser

