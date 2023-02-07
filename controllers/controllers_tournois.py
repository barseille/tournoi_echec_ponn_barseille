import  views.views_entree_tournoi as entree_tournoi
from models.tournoi import Tournoi
import json


class ControllersTournois: 
    
   
    def recuperer_entree_tournoi(self):
        """ sérialiser les données du tournoi"""
        
        print('-'*60)
        print("              -- Création Tournoi --")
        print('-'*60)
        
        while True:    
            self.nom = entree_tournoi.demander_nom_tournoi()
            self.lieu = entree_tournoi.demander_lieu_tournoi()
            self.dates = entree_tournoi.demander_dates_tournoi()  
            self.nombres_de_rounds = entree_tournoi.demander_rounds()
            self.description = entree_tournoi.demander_description()
            self.mode_de_jeu = entree_tournoi.demander_mode_de_jeu()
            
            tournoi = Tournoi(self.nom,
                              self.lieu,
                              self.dates,             
                              self.nombres_de_rounds,
                              self.description,
                              self.mode_de_jeu)  
            
            tournoi_serialiser = tournoi.serialiser()
            self.ecrire_json(tournoi_serialiser, "data/liste_tournois.json")   
            
            autre_tournoi = ""  
            while True:      
                autre_tournoi = input("Souhaitez-vous créer un autre tournoi ? (o/n) : ")
                if autre_tournoi in ["o", "n"]:
                    break
                else:
                    print("Erreur : Veuillez entrer 'o' pour créer un autre tournoi ou 'n' pour quitter.")
                    
            if autre_tournoi == "o":        
                print('Créer un nouveau tournoi : ')
                
            elif autre_tournoi == "n":
                print('Tournoi sauvegarder avec succès !')
                break
                
            
    def ecrire_json(self, tournoi_serialiser, dossier ='data/liste_tournois.json'):
        
        """
        La méthode prend en premier argument un dictionnaire (tournoi_serialiser) 
        et en second argument (optionnel) le fichier JSON où enregistrer les données du tournoi.
        Elle ouvre le fichier JSON en mode lecture/écriture ('r+').
        Elle charge les données du fichier JSON dans un dictionnaire (liste_tournois).
        Elle ajoute tournoi_serialiser à liste_tournois.
        Elle remet le curseur de fichier au début (f.seek(0)) 
        et écrit le dictionnaire modifié dans le fichier JSON en utilisant la fonction json.dump.

        """
        
        with open(dossier,'r+') as f:    
            liste_tournois = json.load(f)
            liste_tournois["liste_tournois"].append(tournoi_serialiser)        
            f.seek(0)  
            json.dump(liste_tournois, f, indent=4)



    def afficher_les_tournois(self):
        """deserialiser la liste des tournois"""
        
        print('-'*60)
        print('           -- Liste des tournois --')
        print('-'*60)
        
        with open ("data/liste_tournois.json", "r") as f:
            liste_tournois = json.load(f)       
        
    
        # Accéder aux index, aux clés et aux valeurs d'un dictionnaire
        for index, tournoi in enumerate(liste_tournois["liste_tournois"]):
            print(f" - Tournoi n°{index} : {tournoi['nom']} - lieu : {tournoi['lieu']} - Date(s) {tournoi['dates']}.")
            print(f"                 Nombres de rounds {tournoi['nombres_de_rounds']} - Mode de jeu : {tournoi['mode_de_jeu']}.")
            print(f"                 Description : {tournoi['description']}\n")


    
    def selectionner_tournoi(self):
        """ afficher la liste des tournois"""
        
        # Charger le fichier JSON dans une variable
        with open('data/liste_tournois.json', 'r') as f:
            tournois_data = json.load(f)

        # Récupérer la liste des tournois
        liste_tournois = tournois_data['liste_tournois']

        
        # Afficher la liste des tournois
        for i, tournoi in enumerate(liste_tournois):
            print(f"Tournoi {i+1}: {tournoi['nom']}")

        # Demander à l'utilisateur de choisir un tournoi par son index
        while True:
            try:
                choix_tournoi = int(input("Choisissez un tournoi par son index: "))
                self.tournoi_selectionne = liste_tournois[choix_tournoi -1]
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide")
            except IndexError:
                print("L'index choisi n'est pas valide")

        # Afficher les informations du tournoi sélectionné
        print('-'*60)
        print("             -- Tournoi sélectionné -- ")
        print('-'*60)
        print(f"Nom: {self.tournoi_selectionne['nom']}")
        print(f"Lieu: {self.tournoi_selectionne['lieu']}")
        print(f"Date(s): {self.tournoi_selectionne['dates']}")
        print(f"Nombre de rounds: {self.tournoi_selectionne['nombres_de_rounds']}")
        print(f"Description: {self.tournoi_selectionne['description']}")
        print(f"Mode de jeu: {self.tournoi_selectionne['mode_de_jeu']}")
        
        return self.tournoi_selectionne


            











