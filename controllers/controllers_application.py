from .controllers_tournois import ControllersTournois
from .controllers_joueurs import ControllersJoueurs
import json
import random
from models.match import Match

class ControllersApplication :

    
    def fusion_tournoi_avec_joueurs(self):
        "sérialiser les tournois complets"
        
        self.liste_des_tournois = ControllersTournois()
        self.liste_des_tournois.selectionner_tournoi()
        self.liste_des_participants = ControllersJoueurs()
        self.liste_des_participants.selectionner_participants()

        tournoi_complet = self.liste_des_tournois.liste_des_tournois + self.liste_des_participants.liste_des_participants       
      
        
        with open('tournoi_avec_joueurs.json', 'w') as f:
            json.dump(tournoi_complet, f, indent=4)
     
            
    def afficher_infos_tournoi(self):
        " désérialiser le tournoi complet "
        
        with open('tournoi_avec_joueurs.json', 'r') as f:
            self.tournoi_data = json.load(f)
 
        for e, info in enumerate(self.tournoi_data):

            if "nom" in info and "lieu" in info:
                
                print('-'*50)
                print("           -- Information de l'évènement -- ")
                print('-'*50)
          
                print("Nom de l'évènement : ", info["nom"])
                print("Lieu de l'évènement : ", info["lieu"])
                print("Date de l'évènement : ", info["dates"])
                print("Nombres de rounds : ", info["nombres_de_rounds"])
                print("Description : ", info["description"])
                print("Mode de jeu : ", info["mode_de_jeu"])
                
            elif "nom" in info and "prenom" in info:
                
                print('-'*50)
                print("           -- Information des joueurs -- ")
                print('-'*50)
                print(f'Joueur {e}')
                print("Nom du joueur:", info['nom'])
                print("Prénom du joueur:", info['prenom'])
                print("Date de naissance du joueur:", info['date_de_naissance'])
                print("Genre du joueur:", info['genre'])
                print("Classement du joueur:", info['classement'])
                print("Score du joueur: ", info["score"])
                
        return self.tournoi_data
    
    def lancer_tournoi(self):
        reponse = input("Souhaitez-vous lancer le tournoi ? (o/n) ")
        
        if reponse == "o":
            pass
        elif reponse == "n":
             self.liste_des_tournois.selectionner_tournoi()
            

 
 
 
 
    
 

    

   