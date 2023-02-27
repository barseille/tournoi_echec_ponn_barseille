from database.database import Database
from views.base_views import BaseViews


class ViewsRepriseTournoi(BaseViews):
    
   
    
    def reprendre_tournoi(self):
        

        
        self.joueurs = []
        
        d = Database()
        # data.lire_database("data/historique_tournois.json")
        data = d.lire_database("data/historique_tournois.json")
        
        # self.rounds_totals = self.tournoi["nombres_de_rounds"]
        # self.rounds_termines = self.tournoi["rounds_effectues"] 
        # self.rounds_restants = self.rounds_totals - self.rounds_termines
        
        # print(self.rounds_totals)
        # print(self.rounds_termines)
        # print(self.rounds_restants)
        
        
        tournois_non_termines = []
        
        # S'il n'y a aucuns tournois dans la base de données
        if not data["liste_des_tournois"]:
            msg = "Aucun tournoi dans la base de données !"
            super().afficher_msg(msg)
            return
        
        # Recherche des tournois inachevés
        for tournoi in data["liste_des_tournois"]:
            if tournoi["statut"] == "tournoi non termine":
                tournois_non_termines.append(tournoi)
        
         # S'il n'y a aucuns tournois avec le statut "tournoi non terminé"       
        if not tournois_non_termines:
            msg = "Aucuns tournois inachevés dans la base de données !"
            super().afficher_msg(msg)
            return

        # Afficher tous les tournois inachevés
        for i, tournoi in enumerate(tournois_non_termines):
            liste = f'{i + 1}. Nom du tournoi : {tournoi["nom"]} - Dates: {tournoi["dates"]}'
            super().afficher_msg(liste)     
            i += 1
            
        while True:
            try:
                
                choix = int(input("Quel tournoi souhaitez-vous continuer (choisir son numéro) ? ")) 
                self.tournoi = tournois_non_termines[choix - 1]
                
                super().presentation("            -- Informations du tournoi --")
                print(f'Nom du tournoi : {self.tournoi["nom"]}')
                print(f'Lieu : {self.tournoi["lieu"]}')
                print(f'Dates : {self.tournoi["dates"]}')
                print(f'Description : {self.tournoi["description"]}')
                print(f'Mode de jeu : {self.tournoi["mode_de_jeu"]}') 
                
                super().presentation("                   -- Joueurs --")    
                for i, joueur in enumerate(self.tournoi["joueurs"]):
                    print(f'{i + 1} - {joueur["prenom"]} {joueur["nom"]}')
                    self.joueurs.append(joueur)
                    
                    
                
                # super().presentation("              -- Informations sur les rounds --")  
                # self.nb_rounds_termines = self.tournoi["rounds_effectues"]
                # print(f"Nombre(s) de round(s) effectué(s) : {(self.nb_rounds_termines)} Round(s)")
                
                # self.nb_de_rounds_restants = self.tournoi["nombres_de_rounds"] - self.tournoi["rounds_effectues"]
                # print(f"Nombre(s) de round(s) restant(s) : {(self.nb_de_rounds_restants)} Round(s)")
                break
 
            except ValueError:
                affiche = BaseViews()
                affiche.affichage_erreur_type()
                
            except IndexError:
                affiche = BaseViews()
                affiche.affichage_erreur_numero()
                
        return self.tournoi