from datetime import datetime
from .round import Round
from .match import Match

class Tournoi:

    def __init__(self, nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
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
        
        tournoi_infos = {'nom': self.nom,
                         'lieu': self.lieu,
                         'dates': self.dates,
                         'nombres_de_rounds': self.nombres_de_rounds,
                         'description': self.description,
                         'mode_de_jeu': self.mode_de_jeu,
                         }
        return tournoi_infos
    
    # def __str__(self):
    #     print(f'Nom du tournoi : {self.tournoi["nom"]}')
    #     print(f'Lieu : {self.tournoi["lieu"]}')
    #     print(f'Dates : {self.tournoi["dates"]}')
    #     print(f'Description : {self.tournoi["description"]}')
    #     print(f'Mode de jeu : {self.tournoi["mode_de_jeu"]}') 
        
    
    
    def temps_round(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        temps = f"Date et heure du Round : {date}"
        print(temps)
    

  
 
    # def serialise(self):
    #     """Return a dictionnary from the objects attributs"""

    #     serialise_data = {
    #                         "name": self.nom,
    #                         "lieu": self.lieu,
    #                         "description": self.description,
    #                         "debut_round": self.debut_round,
    #                         "mode_de_jeu": self.mode_de_jeu,
    #                         "speed": self.speed,
    #                         "nombres_de_rounds": self.nombres_de_rounds,
    #                         "round_actuel": self.round_actuel,
    #                         "statut": self.statut,
    #                         "rencontres": self.rencontres,
    #                         "joueurs": [joueur.id for joueur in self.joueurs],
    #                         "rounds": [round.serialise() for round in self.rounds],
    #                         }
    #     return serialise_data



        






 

    
   
