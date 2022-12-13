from tinydb import TinyDB
from models.tournoi import Tournoi
import  views.views_entree_tournoi as entree_tournoi



def creation_tournoi():
    
    entree_tournoi.bienvenue()
 
    
    nom = entree_tournoi.creation_nom_tournoi()
    lieu = entree_tournoi.creation_lieu_tournoi()
    date_debut = entree_tournoi.creation_date_debut_tournoi()
    date_fin = entree_tournoi.creation_date_fin_tournoi()
    nombre_de_rounds = entree_tournoi.creation_nombre_de_rounds()
    description = entree_tournoi.creation_description()
    mode_de_jeu = entree_tournoi.selection_mode_de_jeu()
    
    
    tournoi = Tournoi(nom,
                      lieu,
                      date_debut,
                      date_fin,
                      nombre_de_rounds,
                      description,
                      mode_de_jeu
                      )
    
    tournoi_serialiser = tournoi.serialiser()
    
    db = TinyDB("db.json")
    tournois_table = db.table("Tournois")
    tournois_table.insert(tournoi_serialiser)

    print("Tournoi crée avec succes !")