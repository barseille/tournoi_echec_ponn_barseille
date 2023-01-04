class Tournoi:
    
    def __init__(self, nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu):
        
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombres_de_rounds = nombres_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu
        self.liste_des_participants = []
        self.score = 0
       
        
    def serialiser(self):
        
        tournoi_serialiser = {'nom': self.nom,
                              'lieu': self.lieu,
                              'dates': self.dates,    
                              'nombres_de_rounds': self.nombres_de_rounds,
                              'description': self.description,
                              'mode_de_jeu': self.mode_de_jeu,
                              'score':0
                             
                              }
        return tournoi_serialiser
  
    def affichage_tournoi_termine(self):
        pass




        






 

    
   
