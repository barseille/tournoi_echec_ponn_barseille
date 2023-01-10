import json
from .accueil import ViewsAccueil

RAPPORT_OPTIONS = ("Liste de tous les joueurs par ordre alphabétique", 
                   "Liste de tous les tournois")


class ViewsRapportMenu:
    
    def afficher_menu_rapport(self):
        print("-"*60) 
        print("                -- Menu Rapport --")  
        print("-"*60) 
        
        for elt in RAPPORT_OPTIONS:
            print(RAPPORT_OPTIONS.index(elt) + 1, '-', elt)
            
        entree = input("Faites votre choix : ")
        if entree == 1:
            self.affichage_joueur()
        elif entree == 2:
            self.affichage_tournoi()
            
        # retour = input("Appuyer sur ENTREE pour revenir au menu")
        # if retour == '':
        #     accueil = ViewsAccueil()
        #     accueil.accueil_principal()
    
    
    
        
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
            
        
            
            
            # retour = input("Appuyer sur ENTREE pour revenir au menu")
            # if retour == 'o':
            #     accueil = ViewsAccueil()
            #     accueil.accueil_principal()
                
    
    
    
    
    
    
    def affichage_tournoi(self):
        pass
    
    