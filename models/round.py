


import random

class Round:
    def __init__(self, nom, date, debut, fin):
        
        self.nom = nom
        self.date = date
        self.debut = debut
        self.fin = fin
        self.resultats = []
        self.liste_matchs = []


    def serialiser(self):
        
        """Sérialise les données du round"""
        round_data = {
            'nom': self.nom,
            'debut': self.debut,
            'fin': self.fin,
            'resultats': self.resultats
        }
        return round_data
    
    def lancer_premier_round(self):
        
        """ mélangez tous les joueurs de façon aléatoire """
        pass


    def trier_joueurs_par_totale_points(self):
        pass
    
    def trier_joueurs_par_ordre(self):
        pass
    
    def choisir_joueurs_aleatoirement(self):
        """ si les joueurs ont le même nombre de points, choisir aléatoirement"""
        pass
    
    def generer_paires(self):
        pass
    
    def mise_a_jour_points(self):
        pass
    
    
    
    


