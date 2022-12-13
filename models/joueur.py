class Joueur:
    def __init__(self, data):
        
        self.nom = data["Nom"]
        self.prenom = data["Prenom"]
        self.date_de_naissance = data["Date de naissance"]
        self.genre = data["Genre"]
        self.classement = data["Classement"]
        self.score = 0


    def serialiser(self):
        
        joueur_serialiser = {
            'Nom': self.nom,
            'Prenom': self.prenom,
            'Date_de_naissance': self.date_de_naissance,
            'Genre': self.genre,
            'Classement': self.classement,
            'Score': self.score
        }
        return joueur_serialiser