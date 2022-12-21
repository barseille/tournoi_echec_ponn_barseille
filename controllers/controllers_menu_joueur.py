import views.views_entree_joueur as entree_joueur
from models.joueur import Joueur
import json

liste_des_joueurs_deserialiser = []

def creation_joueur():
    """ serialiser joueur """
    
    entree_joueur.accueil_joueur()
    
    nom = entree_joueur.creation_joueur_nom()
    prenom = entree_joueur.creation_joueur_prenom()
    date_de_naissance = entree_joueur.creation_joueur_date_de_naissance()
    genre = entree_joueur.creation_joueur_genre()
    classement = entree_joueur.creation_joueur_classement()
       
    joueur = Joueur(nom,
                    prenom,
                    date_de_naissance,
                    genre,
                    classement)
    
    joueur_serialiser = joueur.serialiser()
    with open("joueurs.json", "a") as jd:
        json.dump(joueur_serialiser, jd, indent=4)
    # joueur_serialiser = json.dumps(joueur_serialiser)  
   
    """ désérialisation joueur """
    with open("joueurs.json", "r") as jl:
        joueur_deserialiser = json.load(jl)
    # joueur_deserialiser = json.loads(joueur_serialiser)
    
    joueur_deserialiser = {'nom' : joueur_deserialiser["nom"],
                            'prenom' : joueur_deserialiser["prenom"],
                            'date_de_naissance' : joueur_deserialiser["date_de_naissance"],
                            'genre' : joueur_deserialiser["genre"],
                            'classement' : joueur_deserialiser["classement"]}
    
    autre_joueur = input("Voulez vous créer un autre joueur ? o(oui) / n(non)")
    
    if autre_joueur == "o":
        autre_joueur = creation_joueur()

    elif autre_joueur == "n":
        print(joueur_deserialiser)
    else:
        print("Veuillez saisir correctement ! ")
    

    return joueur_deserialiser
    
    # print(f'Nom : {liste_des_joueurs_deserialiser["nom"]}')
    # print(f'Prénom : {liste_des_joueurs_deserialiser["prenom"]}')
    # print(f'Date de naissance : {liste_des_joueurs_deserialiser["date_de_naissance"]}')
    # print(f'Genre : {liste_des_joueurs_deserialiser["genre"]}')
    # print(f'Classement : {liste_des_joueurs_deserialiser["classement"]}')

    return liste_des_joueurs_deserialiser
        

 
    
    
    
    
    
    
    
    
    
    
    



def afficher_joueur():
    
    joueur_serialiser = creation_joueur()
    
    
  
   
    
   
    
    
    # print(f'Nom : {joueur_deserialiser["nom"]}')
    # print(f'Prénom : {joueur_deserialiser["prenom"]}')
    # print(f'Date de naissance : {joueur_deserialiser["date_de_naissance"]}')
    # print(f'Genre : {joueur_deserialiser["genre"]}')
    # print(f'Classement : {joueur_deserialiser["classement"]}')
    
    
    
    # joueur_deserialiser = {'nom' : joueur_deserialiser["nom"],
    #                 'prenom' : joueur_deserialiser["prenom"],
    #                 'date_de_naissance' : joueur_deserialiser["date_de_naissance"],
    #                 'genre' : joueur_deserialiser["genre"],
    #                 'classement' : joueur_deserialiser["classement"]  
    #                 }
    # return joueur_deserialiser


# def  affichage_joueur():
#     print(f'Nom : {joueur_deserialiser["nom"]}')
#     print(f'Prénom : {joueur_deserialiser["prenom"]}')
#     print(f'Date de naissance : {joueur_deserialiser["date_de_naissance"]}')
#     print(f'Genre : {joueur_deserialiser["genre"]}')
#     print(f'Classement : {joueur_deserialiser["classement"]}')
    
    
    
#     joueur_deserialiser = {'nom' : joueur_deserialiser["nom"],
#                     'prenom' : joueur_deserialiser["prenom"],
#                     'date_de_naissance' : joueur_deserialiser["date_de_naissance"],
#                     'genre' : joueur_deserialiser["genre"],
#                     'classement' : joueur_deserialiser["classement"]  
#                     }
#     return joueur_deserialiser
   
   
   
    
    # joueur_deserialiser = json.loads(joueur)
    
    # print(f'Nom : {joueur_deserialiser["nom"]}')
    # print(f'Prénom : {joueur_deserialiser["prenom"]}')
    # print(f'Date de naissance : {joueur_deserialiser["date_de_naissance"]}')
    # print(f'Genre : {joueur_deserialiser["genre"]}')
    # print(f'Classement : {joueur_deserialiser["classement"]}')
    
    
    # joueur_deserialiser = {'nom' : joueur_deserialiser["nom"],
    #                 'prenom' : joueur_deserialiser["prenom"],
    #                 'date_de_naissance' : joueur_deserialiser["date_de_naissance"],
    #                 'genre' : joueur_deserialiser["genre"],
    #                 'classement' : joueur_deserialiser["classement"]  
    #                 }
    # return joueur_deserialiser

 
      
   


# def afficher_joueur_deserialiser():
#     joueur_deserialiser = creation_joueur()
#     joueur_deserialiserd = json.loads(joueur_deserialiser)
            
#     joueur_deserialiser = {"nom": joueur_deserialiser["nom"],
#                     "prenom": joueur_deserialiser["prenom"],
#                     "date de naissance": joueur_deserialiser["date_de_naissance"],
#                     "genre": joueur_deserialiser["genre"],
#                      "classement": joueur_deserialiser["classement"]
#                     }  

    
#     print(joueur_deserialiserd)
    
    # joueur_serialiser = json.loads(creation_joueur())
    
    # joueur_deserialiser = Joueur
    # joueur_deserialiser.deserialiser_joueurs(joueur_serialiser)
    
    # joueur_deserialiser = []
    # par = json.loads(joueur_deserialiser) 
    
    # print(par)
    
    # for participant in joueur_deserialiser:
    #     joueur_deserialiser.append(participant)
    #     print(joueur_deserialiser)
        
        
    






