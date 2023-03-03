from datetime import datetime
from .match import Match
from .joueur import Joueur
from dataclasses import dataclass
from datetime import date

class Round:

    def __init__(self, nombres_de_rounds):
        self.nombres_de_rounds = nombres_de_rounds

    def periode_round(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        temps = f"Date et heure du Round : {date}"
        print(temps)
        





# @dataclass
# class Round:
#     """Represents a round of matches"""

#     nom: str
#     matches: list[Match]
#     debut: str = str(date.today())
#     fin: str = ""
#     statut: str = "En cours"

#     def __str__(self) -> str:
#         msg = f"Round {self.nom} - Début : {self.debut} - "
#         if self.fin == "":
#             msg += "En cours ..."
#         else:
#             msg += f"Fini le : {self.fin}"
#         return msg

#     def serialiser(self) -> dict:
#         """ Renvoie les donnnées sérialisées pour le round dans le dictionnaire """
#         matches = [match.serialiser() for match in self.matches]

#         data = {
#             "nom": self.nom,
#             "debut": self.debut,
#             "fin": self.fin,
#             "statut": self.statut,
#             "matches": [match.serialiser() for match in self.matches],
#         }
#         return data

#     @classmethod
#     def create_from_document(csl, data: dict) -> "Round":
#         """ Retourner un objet Round à partir d'un dict """
#         # create the round unpacking the simple data
#         round = csl(**data)

#         # create the more complex object (Match object)
#         round.matches = Match.create_from_document(data["matches"])
#         return round

#     @classmethod
#     def get_round_list(cls, rounds: list[dict]) -> list["Round"]:
#         """Return a list of Round from a list of dict"""

#         return [cls.create_from_document(round) for round in rounds]


# if __name__ == "__main__":
#     from datetime import date

#     p1 = Joueur("Carlsen", "Magnus", date(1990, 10, 15), "M", 2850, id=1)
#     p2 = Joueur("Vachier", "Max", date(1990, 12, 25), "M", 2800, id=2)

#     ps1 = joueurScore(p1)
#     ps2 = joueurScore(p2)

#     # p1 win
#     ps1.score = 1

#     m1 = Match(ps1, ps2)
#     m2 = Match(ps2, ps1)

#     r1 = Round("Round 1", [m1, m2])

#     print(r1)
#     for m in r1.matches:
#         msg = f"{m.joueur1} Vs {m.joueur_score2}"
#         print(msg)

#     print(m1.serialiser())