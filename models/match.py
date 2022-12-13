from models.joueur import Joueur

class Match:
    def __init__(self, joueur_1, joueur_2, score):
        
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.joueur_1_match_score = None
        self.joueur_2_match_score = None   
        self.score = score
        self.match_terminer = ()


    def serialiser_joueur(self, joueur):
        joueur = Joueur()
        return joueur.serialiser()


    def afficher_score(self, joueur_gagnant):

    
        if joueur_gagnant == self.joueur_2:
            self.joueur_2.score += 1
            self.joueur_2_match_score = 1
            self.joueur_1.score += 0
            self.joueur_1_match_score = 0
            
        elif joueur_gagnant == self.joueur_1:
            self.joueur_1.score += 1
            self.joueur_1_match_score = 1
            self.joueur_2.score += 0
            self.joueur_2_match_score = 0
            
        elif joueur_gagnant is None:
            self.joueur_1.score += 0.5
            self.joueur_1_match_score = 0.5
            self.joueur_2.score += 0.5
            self.joueur_2_match_score = 0.5
            
        else:
            pass

        self.match_terminer = ([self.joueur_1, self.joueur_1_match_score],
                               [self.joueur_2, self.joueur_2_match_score])
   
      
    def serialiser(self):
        match_serialiser = {
            
            'joueur_1': self.serialiser_joueur(self.joueur_1),
            'joueur_2': self.serialiser_joueur(self.joueur_2),
            
            'joueur_1_match_score': self.joueur_1_match_score,
            'joueur_2_match_score': self.joueur_2_match_score,
            
            'terminer': self.match_terminer,
        }
        return match_serialiser

