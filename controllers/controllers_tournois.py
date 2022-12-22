import  views.views_entree_tournoi as entree_tournoi
from models.tournoi import Tournoi
import json


class ControllersTournois:
    
    def recuperer_entree_tournoi(self):
        
        print("Créer votre tournoi : ")
        
        self.nom = entree_tournoi.creation_nom_tournoi()
        self.lieu = entree_tournoi.creation_lieu_tournoi()
        self.date_tournoi = entree_tournoi.creation_date_tournoi()
        self.nombres_de_rounds = entree_tournoi.creation_nombres_de_rounds()
        self.description = entree_tournoi.creation_description()
        self.mode_de_jeu = entree_tournoi.selection_mode_de_jeu()
        
        tournoi = [self.nom, 
                   self.lieu, 
                   self.date_tournoi, 
                   self.nombres_de_rounds, 
                   self.description, 
                   self.mode_de_jeu]
        
        return tournoi


    def serialiser(self):
        
        
        tournoi = Tournoi(self.nom,
                    self.lieu,
                    self.date_tournoi,
                    self.nombres_de_rounds,
                    self.description,
                    self.mode_de_jeu
                    )
        
        tournoi_serialiser = tournoi.serialiser()
        
        with open("liste_tournois.json", "w") as td:
            json.dump(tournoi_serialiser, td, indent=4)
 
            
    def deserialiser(self):
        """deserialiser"""
        
        with open ("liste_tournois.json", "r") as tl:
            tournoi_deserialiser = json.load(tl)
            
        self.tournoi_deserialiser = [{"nom" : tournoi_deserialiser["nom"],
                                      "lieu" : tournoi_deserialiser["lieu"],
                                      "date_tournoi" : tournoi_deserialiser["date_tournoi"],
                                      "nombres_de_rounds" : tournoi_deserialiser["nombres_de_rounds"],
                                      "description" : tournoi_deserialiser["description"],
                                      "mode_de_jeu" : tournoi_deserialiser["mode_de_jeu"]}]
            
      
        return self.tournoi_deserialiser  

            
    def afficher_les_tournois(self):
        
        for tournoi in self.tournoi_deserialiser:
            
            print(self.tournoi_deserialiser.index(tournoi) + 1 
                  , '-'
                  , 'Nom : ', tournoi["nom"]
                  , '| Lieu : ', tournoi["lieu"]
                  , '| Date du tournoi : ', tournoi["nom"]
                  , '| Nombres de rounds : ', tournoi["nombres_de_rounds"]
                  , '| Description : ', tournoi["description"]
                  , '| Mode de jeu : ', tournoi["mode_de_jeu"])
            
        return self.tournoi_deserialiser        
        
           
        
              
             
    
        
























