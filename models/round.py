


import random

class Round:
    def __init__(self, numero, debut, fin):
        
        self.numero = numero
        self.debut = debut
        self.fin = fin
        self.resultats = []
        


    def serialiser(self):
        
        """Sérialise les données du round"""
        round_data = {
            'numero': self.numero,
            'debut': self.debut,
            'fin': self.fin,
            'resultats': self.resultats
        }
        return round_data




