import datetime


class Round:   
    def __init__(self, numero, debut_round, fin_round,  round_terminer):
        self.numero = numero
        self.debut_round = debut_round
        self.fin_round = fin_round
        self.round_terminer = round_terminer
        self.matchs = []


    def debut_round(self, debut_round, matchs):
        self.debut_round = debut_round
        self.matchs = matchs


    def fin_round(self, fin_round):
        self.fin_round = fin_round
        self.round_terminer = True


    def recuperer_matchs_serialiser(self, matchs):
        matchs_serialiser = []
        if matchs > 0:
            for match in matchs:
                matchs_serialiser.append(match.serialiser())
        return matchs_serialiser

    def serialiser(self):
        round_serialiser = {
            'numero': self.numero,
            'debut du round': self.debut_round,
            'fin du round': self.fin_round,
            'round terminer': self.round_terminer,
            'matchs': self.recuperer_matchs_serialiser(self.matchs)
        }
        return round_serialiser

