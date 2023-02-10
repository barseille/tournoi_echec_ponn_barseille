# class Match:
#     def __init__(self, joueur1, joueur2):
#         self.joueur1 = joueur1
#         self.joueur2 = joueur2
#         self.gagnant = None

#     def jouer(self):
#         """Détermine le gagnant du match et attribue les points appropriés."""
#         # Déterminez le gagnant ici
#         if self.joueur1.cote > self.joueur2.cote:
#             self.joueur1.points += 1
#             self.gagnant = self.joueur1
#         elif self.joueur1.cote < self.joueur2.cote:
#             self.joueur2.points += 1
#             self.gagnant = self.joueur2
#         else:
#             self.joueur1.points += 0.5
#             self.joueur2.points += 0.5
#             self.gagnant = None

