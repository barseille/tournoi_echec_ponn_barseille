import json
from .accueil import ViewsAccueil

RAPPORT_OPTIONS = ("Liste de tous les joueurs par ordre alphabétique", 
                   "Liste de tous les tournois")

RAPPORT_TOURNOIS = ("Liste de tous les tournois")


class ViewsRapportMenu:
    
    def afficher_menu_rapport(self):
        print("-"*60) 
        print("                -- Menu Rapport --")  
        print("-"*60) 
        
        for elt in RAPPORT_OPTIONS:
            print(RAPPORT_OPTIONS.index(elt) + 1, '-', elt)
            
   
        
    def affichage_joueur(self):
        
        print('-'*70)
        print('         -- Classement des joueurs par ordre alphabetique --')
        print('-'*70)
        
        with open("liste_joueurs.json", "r") as f:
            joueurs_data = json.load(f)
        
        liste_joueurs = joueurs_data['liste_joueurs']
        liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        
        i = 1   
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['nom']} {joueur['prenom']} | Classement {joueur['classement']}")
            
    
    
    def affichage_tournoi(self):
        
        print('-'*70)
        print('                 -- Liste de tous les tournois --')
        print('-'*70)
        
        with open("liste_tournois.json", "r") as f:
            liste_tournois_data = json.load(f)
            
        self.liste_tournois = liste_tournois_data["liste_tournois"]
        
        i = 1
        for i, tournoi in enumerate(self.liste_tournois):
            nom = tournoi["nom"]
           
            dates = tournoi["dates"]
            print(f"{i+1} - Tournoi {nom} | Date : {dates}")
            
  
    
    def afficher_details_tournoi(self):
        
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))

        tournoi_selectionne = self.liste_tournois[choix_tournoi - 1]
        nom_tournoi = tournoi_selectionne['nom']
        
        with open("historique_tournois.json", "r") as f:
            historique_tournois_data = json.load(f) 
            
        tournois_en_cours = historique_tournois_data["liste_des_tournois_en_cours"]
        
        # On vérifie s'il y a plusieurs tournois du même nom et qu'ils sont terminés
        tournois_meme_nom = []
        for tournoi in tournois_en_cours:
            if tournoi["nom"] == nom_tournoi:
                tournois_meme_nom.append(tournoi)
   
        # on filtre pour récupérer les tournois ayant un id unique        
        ids = []
        for i, tournoi in enumerate(tournois_meme_nom):
            if tournoi['id'] not in ids :
                ids.append(tournoi['id'])
                print(f"{i+1} - {tournoi['nom']} | {tournoi['dates']}")
        choix = int(input("Plusieurs tournois ont le même nom. Choisissez le tournoi que vous souhaitez sélectionner : "))
        tournoi_fini = tournois_meme_nom[choix-1]
                
        # # On récupère le tournoi terminé
        # tournois_meme_id = []
        # if len(tournois_meme_nom) > 1:
            
        #     for tournoi in tournois_meme_nom:
        #         if len(tournoi["id"]) > 1 :
        #             tournois_meme_id.append(tournoi)
        #     tournoi_fini = tournois_meme_id[-1]
                                
        nom_tournoi = tournoi_fini["nom"]
        date_tournoi = tournoi_fini["dates"]
        
        print('-'*70)
        print('                 -- Informations du tournoi --')
        print('-'*70)
        print(f"Nom du tournoi : {nom_tournoi} | Date(s) : {date_tournoi}")
        
        print("Liste des joueurs :")
        for joueur in tournoi_fini["joueurs"]:
            print(f" - {joueur['nom']} {joueur['prenom']}")
            
                
        for round in tournoi_fini["liste_de_rounds"]:
            for cle, valeur in round.items():
                print('-'*50)
                print(f"               -- {cle} --")
                print('-'*50)
                for match in valeur["liste_de_matchs"]:
                    joueur1 = match[0]
                    score = match[1]
                    print(f"{joueur1} : {score}")
                    
  




 