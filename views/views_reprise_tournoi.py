
class ViewsRepriseTournoi():
    
    
    def affichage_tournoi(self, tournoi):
        
            print(f'Nom du tournoi : {tournoi["nom"]}')
            print(f'Lieu : {tournoi["lieu"]}')
            print(f'Dates : {tournoi["dates"]}')
            print(f'Description : {tournoi["description"]}')
            print(f'Mode de jeu : {tournoi["mode_de_jeu"]}') 
            
    
    def affichage_joueurs(self, tournoi):
        self.joueurs = []
        
        for i, joueur in enumerate(tournoi["joueurs"]):
            print(f'{i + 1} - {joueur["prenom"]} {joueur["nom"]}')
            self.joueurs.append(joueur)
            
        return self.joueurs
     
