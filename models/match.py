from models.joueur import Joueur

class Match:
    def __init__(self, joueur_1, joueur_2, match_terminer):
        
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.joueur_1_match_terminer = None
        self.joueur_2_match_terminer = None   
        self.match_terminer = match_terminer
        self.resultat = ()
        

    def recuperer_joueurs_serialiser(self, joueur):
        joueur = Joueur()
        return joueur.serialiser()
    
    
    
    def serialiser(self):
        match_serialiser = {
            'joueur_1': self.recuperer_joueurs_serialiser(self.joueur_1),
            'joueur_2': self.recuperer_joueurs_serialiser(self.joueur_2),
            'match_terminer': self.match_terminer,
            'joueur_1_match_terminer': self.joueur_1_match_terminer,
            'joueur_2_match_terminer': self.joueur_2_match_terminer       
        }
        return match_serialiser


    def afficher_match_terminer(self, joueur_gagnant):
 
        if joueur_gagnant == self.joueur_1:
            self.joueur_1_match_terminer = 1
            self.joueur_2_match_terminer = 0
            
        elif joueur_gagnant == self.joueur_2:   
            self.joueur_2_match_terminer = 1
            self.joueur_1_match_terminer = 0
            
        elif joueur_gagnant is None:   
            self.joueur_1_match_terminer = 0.5
            self.joueur_2_match_terminer = 0.5
            
        else:
            pass

        self.match_terminer = ([self.joueur_1, self.joueur_1_match_terminer],
                               [self.joueur_2, self.joueur_2_match_terminer])
        
        self.match_terminer = True
   
      


