import datetime
from .match import Match


class Tournoi:
    def __init__(self, nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self._dates = dates
        self.nombres_de_rounds = nombres_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu
        self.joueur1 = None
        self.joueur2 = None
        self.paires_precedentes = []
        self.match = Match(self.joueur1, self.joueur2)
        self.match_info = []
        self.resultats_round = {}
        self.liste_matchs = []
        self.rounds_restants = 0
        self.tournoi_inacheve = {}

    def afficher_tournoi(self):
        tournoi_infos = {
            "nom": self.nom,
            "lieu": self.lieu,
            "dates": self._dates,
            "nombres_de_rounds": self.nombres_de_rounds,
            "description": self.description,
            "mode_de_jeu": self.mode_de_jeu,
        }
        return tournoi_infos

    @property
    def dates(self):
        return self._dates

    # value : 23/05/1994
    @dates.setter
    def dates(self, value):
        try:
            datetime.datetime.strptime(value, "%d/%m/%Y")
            self._dates = value

        except ValueError:
            raise ValueError("Date de naissance doit être un str(jj/mm/aaaa)")
