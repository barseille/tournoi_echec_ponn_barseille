from models.tournoi import Tournoi
import  views.views_entree_tournoi as entree_tournoi
from models.tournoi import Tournoi
import json


def creation_tournoi():
    """serialiser tournoi"""
 
    entree_tournoi.bienvenue()
 
    nom = entree_tournoi.creation_nom_tournoi()
    lieu = entree_tournoi.creation_lieu_tournoi()
    date_tournoi = entree_tournoi.creation_date_tournoi()
    nombre_de_rounds = entree_tournoi.creation_nombre_de_rounds()
    description = entree_tournoi.creation_description()
    mode_de_jeu = entree_tournoi.selection_mode_de_jeu()
      
    tournoi = Tournoi(nom,
                      lieu,
                      date_tournoi,
                      nombre_de_rounds,
                      description,
                      mode_de_jeu
                      )

    
    tournoi_serialiser = tournoi.serialiser()
    tournoi_serialiser = json.dumps(tournoi_serialiser)
    
    """désérialisation tournoi"""
    tournoi_deserialiser = json.loads(tournoi_serialiser)
    
    tournoi_deserialiser = [{'nom' : tournoi_deserialiser["nom"],
                            'lieu' : tournoi_deserialiser["lieu"],
                            'date_tournoi' : tournoi_deserialiser["date_tournoi"],
                            'nombres_de_rounds' : tournoi_deserialiser["nombres_de_rounds"],
                            'description' : tournoi_deserialiser["description"],
                            'mode_de_jeu' : tournoi_deserialiser["mode_de_jeu"]}]
    
    liste_des_tournois_deserialiser = []
    
    autre_tournoi = input("Voulez-vous créer un autre tournoi ? o(oui) / n(non)")
    
    if autre_tournoi == "o":
        autre_tournoi = creation_tournoi()
        
    elif autre_tournoi == "n":
        pass
    else:
        print("Veuillez saisir correctement ! ")
        
    for tournoi in tournoi_deserialiser:
        liste_des_tournois_deserialiser.append(tournoi)
    
    
    
    print("Voici les tournois crées : ")
    print(liste_des_tournois_deserialiser)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print("Tournoi crée avec succes !")  

 

  

    

        
       
    
    

