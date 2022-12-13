MODE_DE_JEU = ("bullet", "blitz", "fast")


class Tournoi:
    def __init__(self, nom, lieu, date, nombre_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_rounds = nombre_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu
        self.participants = []
        self.rounds = []
    

    def serialiser_joueur_tournoi(self, participants):
        serialiser_joueur = []
        if participants > 0:
            for participant in participants:
                serialiser_joueur.append(participant.serialiser())
        return serialiser_joueur

    def serialiser_round_tournoi(self, rounds):
        serialiser_round = []
        if rounds > 0:
            for round in rounds:
                serialiser_round.append(round.serialiser())
        return serialiser_round

    def serialiser(self):
        tournoi_serialiser = {
            'nom': self.nom,
            'lieu': self.lieu,
            'date': self.date,
            'nombre_de_rounds': self.nombre_de_rounds,
            'description': self.description,
            'mode_de_jeu': self.mode_de_jeu,
            'participants': self.serialiser_joueur_tournoi(self.participants),
            'rounds': self.serialiser_round_tournoi(self.rounds)
        }
        return tournoi_serialiser
