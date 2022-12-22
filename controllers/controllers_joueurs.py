import views.views_entree_joueur as entree_joueur
from models.joueur import Joueur
import json

class ControllersJoueurs:
    
    liste_des_joueurs_deserialiser = []

    def recuperer_entree_joueur(self):
        
        print("Créer votre joueur : ")
         
        self.nom = entree_joueur.creation_joueur_nom()
        self.prenom = entree_joueur.creation_joueur_prenom()
        self.date_de_naissance = entree_joueur.creation_joueur_date_de_naissance()
        self.genre = entree_joueur.creation_joueur_genre()
        self.classement = entree_joueur.creation_joueur_classement()
        
        joueur = [self.nom,
                  self.prenom,
                  self.date_de_naissance,
                  self.genre,
                  self.classement]
        
        return joueur
    
    
    def serialiser(self):
        
        joueur = Joueur(self.nom,
                        self.prenom,
                        self.date_de_naissance,
                        self.genre,
                        self.classement)
        
        joueur_serialiser = joueur.serialiser()
        
        with open("liste_joueurs.json", "w") as jd:
            json.dump(joueur_serialiser, jd, indent=4)
        # joueur_serialiser = json.dumps(joueur_serialiser)  
  
    
    def deserialiser(self):
        """ désérialisation joueur """
           
        with open("liste_joueurs.json", "r") as jl:
            
            joueur_deserialiser = json.load(jl)
            # joueur_deserialiser = json.loads(joueur_serialiser)
             
        self.joueur_deserialiser = [{'nom' : joueur_deserialiser["nom"],
                                    'prenom' : joueur_deserialiser["prenom"],
                                    'date_de_naissance' : joueur_deserialiser["date_de_naissance"],
                                    'genre' : joueur_deserialiser["genre"],
                                    'classement' : joueur_deserialiser["classement"]}]
        
        return self.joueur_deserialiser
    
    
    def afficher_les_joueurs(self):
        
        for joueur in self.joueur_deserialiser:
            
            print(self.joueur_deserialiser.index(joueur) + 1
                  , '-'
                  , '| Nom : ', joueur["nom"]
                  , '| Prenom : ', joueur["prenom"]
                  , '| Date de naissance : ', joueur["date_de_naissance"]
                  , '| Genre : ', joueur["genre"]
                  , '| Classement', joueur["classement"])
            
        return self.joueur_deserialiser
        

        

 
    
    
    
    
    
    
    
    
   
   

        
    






