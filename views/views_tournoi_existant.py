import json



class ViewsTournoiExistant:
    
    def chercher_tournois_existant(self):
        
        self.tournoi_selectionne = None
        
        self.liste_des_joueurs = []
        
        with open("data/tournois_inacheves.json", "r") as f:
            data = json.load(f)
            if not data["tournois_inacheves"]:
                print("                  *** Aucuns Tournois ***")
                return
            i = 1
            for i, tournoi in enumerate(data["tournois_inacheves"]):
                print(f'{i + 1}. Nom du tournoi: {tournoi["nom"]} - Dates: {tournoi["dates"]}')
                i += 1

        while True:
                
            choix_tournoi = int(input("Quel tournoi souhaitez-vous continuer (numéro index) ? ")) 
            self.tournoi_selectionne = data["tournois_inacheves"][choix_tournoi-1]
            
            
            print('-'*60)
            print("            -- Informations du tournoi --")
            print('-'*60)   
            print(f'Nom du tournoi : {self.tournoi_selectionne["nom"]}')
            print(f'Lieu : {self.tournoi_selectionne["lieu"]}')
            print(f'Dates : {self.tournoi_selectionne["dates"]}')
            print(f'Description : {self.tournoi_selectionne["description"]}')
            print(f'Mode de jeu : {self.tournoi_selectionne["mode_de_jeu"]}')     
            print('-'*60)
            print("                   -- Joueurs --")
            print('-'*60)
            
            for joueur in self.tournoi_selectionne["joueurs"]:
                print(f'{joueur["prenom"]} {joueur["nom"]}')
                self.liste_des_joueurs.append(joueur)
                
            self.nb_rounds_effectues = len(self.tournoi_selectionne["liste_de_rounds"]) 
            print(f"Nombre de rounds effectués : {self.nb_rounds_effectues} Round(s)")
            
            self.nombre_de_rounds_restants = self.tournoi_selectionne["nombres_de_rounds"] - self.nb_rounds_effectues
            print(f"Nombre de rounds restants : {self.nombre_de_rounds_restants} Round(s)")
            

            break
        return self.tournoi_selectionne
        
