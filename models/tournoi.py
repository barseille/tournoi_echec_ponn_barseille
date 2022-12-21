class Tournoi:
    
    def __init__(self, nom, lieu, date_tournoi, nombre_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self.date_tournoi = date_tournoi
        self.nombre_de_rounds = nombre_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu
        self.liste_des_participants = []
        self.rounds = []
        self.tournoi_terminer = False
        
        
    def serialiser(self):
        
        tournoi_serialiser = {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_tournoi": self.date_tournoi,
            "nombres_de_rounds": self.nombre_de_rounds,
            "description": self.description,
            "mode_de_jeu": self.mode_de_jeu,
            # 'participants': self.liste_participants_deserialiser(self.liste_des_participants),
            # 'rounds': self.recuperer_rounds_terminer(self.rounds),
            # 'tournoi_terminer': self.tournoi_terminer
        }

        return tournoi_serialiser
    



 

    
   
