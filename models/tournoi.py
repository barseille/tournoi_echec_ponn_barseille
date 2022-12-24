class Tournoi:
    
    def __init__(self, nom, lieu, date_debut_tournoi, date_fin_tournoi, nombres_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self.date_debut_tournoi = date_debut_tournoi
        self.date_fin_tournoi = date_fin_tournoi
        self.nombres_de_rounds = nombres_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu
        self.liste_des_participants = []
        self.rounds = []
        self.tournoi_terminer = False
        
        
    def serialiser(self):
        
        tournoi_serialiser = {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut_tournoi": self.date_debut_tournoi,
            "date_fin_tournoi":self.date_fin_tournoi,
            "nombres_de_rounds": self.nombres_de_rounds,
            "description": self.description,
            "mode_de_jeu": self.mode_de_jeu,
        }

        return tournoi_serialiser
    
    
            # 'participants': self.liste_participants_deserialiser(self.liste_des_participants),
            # 'rounds': self.recuperer_rounds_terminer(self.rounds),
            # 'tournoi_terminer': self.tournoi_terminer
    



 

    
   
