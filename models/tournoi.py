from datetime import datetime
class Tournoi:

    def __init__(self, nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu):
        self.nom = nom
        self.lieu = lieu
        self.dates = dates
        self.nombres_de_rounds = nombres_de_rounds
        self.description = description
        self.mode_de_jeu = mode_de_jeu

    def afficher_tournoi(self):
        tournoi_infos = {'nom': self.nom,
                         'lieu': self.lieu,
                         'dates': self.dates,
                         'nombres_de_rounds': self.nombres_de_rounds,
                         'description': self.description,
                         'mode_de_jeu': self.mode_de_jeu,
                         }
        return tournoi_infos
  
 
class Round(Tournoi):

    def __init__(self, nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu):
        super().__init__(nom, lieu, dates, nombres_de_rounds, description, mode_de_jeu)


    def afficher_rounds(self):
        liste_de_round = []
        for i in range(self.nombres_de_rounds):
            msg = f"                -- ROUND {i + 1}/{self.nombres_de_rounds} --"
            print(msg)
            liste_de_round.append(i + 1)
        return liste_de_round

    def temps_round(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        temps = f"Date et heure du Round : {date}"
        print(temps)



        






 

    
   
