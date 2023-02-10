# from views.views_rapport_menu import ViewsRapportMenu
from views.views_menu_tournoi import ViewsMenuTournoi
import json

class ControllersRapport:
    
    def affichage_joueur(self):
        
        print('-'*70)
        print('         -- Classement des joueurs par ordre alphabetique --')
        print('-'*70)
        
        with open("data/liste_joueurs.json", "r") as f:
            joueurs_data = json.load(f)
        
        liste_joueurs = joueurs_data['liste_joueurs']
        liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        
        # Afficher tous les joueurs créés
        i = 1   
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Classement {joueur['classement']}")
            
    
    
    def affichage_tournoi(self):
        
        afficher_tournoi = ViewsMenuTournoi()
        afficher_tournoi.afficher_les_tournois()
        
        print('-'*60)
        print('                 -- Liste de tous les tournois --')
        print('-'*60)
        
        with open("data/liste_tournois.json", "r") as f:
            liste_tournois_data = json.load(f)
            
        self.liste_tournois = liste_tournois_data["liste_tournois"]
        
         # Afficher tous les tournois créés
        i = 1
        for i, tournoi in enumerate(self.liste_tournois):
            nom = tournoi["nom"]
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi : {nom} - date(s) : {dates}")
            
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))
        tournoi_selectionne = self.liste_tournois[choix_tournoi - 1]
        
       
        print('-'*60)
        print('               -- Détails du tournoi --')
        print('-'*60)
        print(f'Nom du tournoi : {tournoi_selectionne["nom"]}')
        print(f'Lieu : {tournoi_selectionne["lieu"]}')
        print(f'Dates(s) : {tournoi_selectionne["dates"]}')
        print(f'Nombres de rounds : {tournoi_selectionne["nombres_de_rounds"]}')
        print(f'Mode de jeu : {tournoi_selectionne["mode_de_jeu"]}')
            
  
    
    def afficher_details_tournoi(self):
        
        print('-'*60)
        print('                 -- Liste des tournois terminés --')
        print('-'*60)
        
        with open("data/historique_tournois.json", "r") as f:
            tournoi = json.load(f)
        
        tournoi_termine = tournoi['liste_des_tournois_en_cours']
        
        # Afficher tous les tournois terminés
        i = 1
        for i, tournoi in enumerate(tournoi_termine):
            nom = tournoi["nom"]
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi {nom} - date(s) : {dates}")
        
 
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))
        
        # Détails du tournoi sélectionné
        tournoi_selectionne = tournoi_termine[choix_tournoi - 1]
        
        print('-'*60)
        print('               -- Détails du tournoi terminé --')
        print('-'*60)
        print(f'Nom du tournoi : {tournoi_selectionne["nom"]}')
        print(f'Lieu : {tournoi_selectionne["lieu"]}')
        print(f'Dates(s) : {tournoi_selectionne["dates"]}')
        print(f'Nombres de rounds : {tournoi_selectionne["nombres_de_rounds"]}')
        print(f'Mode de jeu : {tournoi_selectionne["mode_de_jeu"]}')
        
        # Joueurs rangés par ordre alphabétique
        liste_joueurs = tournoi_selectionne['joueurs']
        liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        i = 1  
        
        # Afficher les joueurs du tournoi 
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Classement {joueur['classement']}")
         
        
        # Afficher les détails des matchs par round
        for round in tournoi_selectionne['liste_de_rounds']:
            numero_round = round['numero_round']
            date_debut = round['date_debut']
            date_fin = round['date_fin']
            matchs = round['matchs']
      
      
            print('-'*60)
            print("                       -- Round", numero_round, "--")
            print('-'*60)
            print("Date de début : ", date_debut)
            print("Date de fin : ", date_fin)
      
            
            for match in matchs:
                joueur1 = match['joueur1']
                joueur2 = match['joueur2']
                score = match['score']
                print(joueur1 + " VS " + joueur2 + " = " + score)
            
            

            
   
        
      
        


            

            
            
      
  




    
    