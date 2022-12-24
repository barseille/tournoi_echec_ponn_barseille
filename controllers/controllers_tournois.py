import  views.views_entree_tournoi as entree_tournoi
from models.tournoi import Tournoi
import json


class ControllersTournois:
    
    # def __init__(self):
        
    #     self.tournoi_charger = []
    
    
    
    def recuperer_entree_tournoi(self):
        
        print("Créer votre tournoi : ")
        
        self.nom = entree_tournoi.creation_nom_tournoi()
        self.lieu = entree_tournoi.creation_lieu_tournoi()
        self.date_debut_tournoi = entree_tournoi.creation_date_debut_tournoi()
        self.date_fin_tournoi = entree_tournoi.creation_date_fin_tournoi()
        self.nombres_de_rounds = entree_tournoi.creation_nombres_de_rounds()
        self.description = entree_tournoi.creation_description()
        self.mode_de_jeu = entree_tournoi.selection_mode_de_jeu()
        
        tournoi = [self.nom, 
                   self.lieu, 
                   self.date_debut_tournoi, 
                   self.date_fin_tournoi,
                   self.nombres_de_rounds, 
                   self.description, 
                   self.mode_de_jeu]
        
        return tournoi


    def serialiser(self):
        
        
        tournoi = Tournoi(self.nom,
                    self.lieu,
                    self.date_debut_tournoi,
                    self.date_fin_tournoi,
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
            tournoi_charger = json.load(tl)
            
        tournoi_charger = {"nom" : tournoi_charger["nom"],
                        "lieu" : tournoi_charger["lieu"],
                        "date_debut_tournoi" : tournoi_charger["date_debut_tournoi"],
                        "date_fin_tournoi" : tournoi_charger["date_fin_tournoi"],
                        "nombres_de_rounds" : tournoi_charger["nombres_de_rounds"],
                        "description" : tournoi_charger["description"],
                        "mode_de_jeu" : tournoi_charger["mode_de_jeu"]}
        
        return tournoi_charger
        # for i in tournoi_charger:
        #     self.tournoi_deserialiser.append(i)
            
        # print(self.tournoi_deserialiser) 
        
      

  
    # def afficher_les_tournois(self):
   
    #     for tournoi in self.tournoi_deserialiser:
            
    #         print(self.tournoi_deserialiser.index(tournoi) + 1 
    #               , '-'
    #               , 'Nom : ', tournoi["nom"]
    #               , '| Lieu : ', tournoi["lieu"]
    #               , '| Date de début du tournoi : ', tournoi["date_debut_tournoi"]
    #               , '| Date de fin du tournoi : ', tournoi["date_fin_tournoi"]
    #               , '| Nombres de rounds : ', tournoi["nombres_de_rounds"]
    #               , '| Description : ', tournoi["description"]
    #               , '| Mode de jeu : ', tournoi["mode_de_jeu"])
            
       

        # with open ("liste_tournois.json", "r") as tl:
        #     tournoi_deserialiser = json.load(tl)
            
        # self.tournoi_deserialiser = [{"nom" : tournoi_deserialiser["nom"],
        #                               "lieu" : tournoi_deserialiser["lieu"],
        #                               "date_debut_tournoi" : tournoi_deserialiser["date_debut_tournoi"],
        #                               "date_fin_tournoi" : tournoi_deserialiser["date_fin_tournoi"],
        #                               "nombres_de_rounds" : tournoi_deserialiser["nombres_de_rounds"],
        #                               "description" : tournoi_deserialiser["description"],
        #                               "mode_de_jeu" : tournoi_deserialiser["mode_de_jeu"]}]       
           
        
              
             
    
        
























