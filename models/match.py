

import json
import random

class Match:
    def __init__(self, joueur1, joueur2, resultat):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat


    def serialiser(self):
        """Sérialise les données du match"""
        match_data = {
            'joueur1': self.joueur1,
            'joueur2': self.joueur2,
            'resultat': self.resultat
        }
        
        with open('match.json', 'w') as f:
            json.dump(match_data, f, indent=4)
    
    def stocker_un_match(self):
        """ 
        tuple contenant deux listes, chacune contenant deux éléments : 
        un joueur et un score 
        """
        
        pass
    
    def stocker_liste_de_matchs(self):
        """ matchs doivent être stockés sous forme de liste"""
        pass
    






