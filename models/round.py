class Round:   
    def __init__(self, numero, debut_round, fin_round):
        self.numero = numero
        self.debut_round = debut_round
        self.fin_round = fin_round


    def debut_round(self, debut_round, matchs):
        self.debut_round = debut_round
        self.matchs = matchs


    def fin_round(self, fin_round):
        self.fin_round = fin_round
        self.round_terminer = True


    def round_a_serialiser(self):
        round_serialiser = {
            'numero': self.numero,
            'debut du round': self.debut_round,
            'fin du round': self.fin_round,
            'round terminer': self.round_terminer,
        }
        return round_serialiser

