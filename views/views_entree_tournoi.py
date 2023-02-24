from datetime import datetime
from .base_views import BaseViews
from models.tournoi import Tournoi

class ViewsEntreeTournoi(BaseViews):

    def demander_nom_tournoi(self):
        """ 
        la méthode isalpha() renvoie True
        si la chaîne de caractères ne contient que 
        des lettres alphabétiques
        """
        while True:
            nom = input('Entrez le nom du tournoi : ')
            if nom.isalpha():
                return nom
            else:
                super().affichage_erreur_texte()

    def demander_lieu_tournoi(self):
        
        while True:
            lieu = input('Entrez le lieu du tournoi : ')
            if lieu.isalpha():
                return lieu
            else:
                super().affichage_erreur_texte()
    

    def demander_dates_tournoi(self):
        
        entree_date = input("Entrer une date unique ou une plage de dates ? u(unique)/ p(plage de date) : ")

        # Saisie d'une seule date de tournoi
        if entree_date == 'u':      
            while True:
                date_unique = input("Entrez la date unique au format jj/mm/aaaa : ")
                try:
                    date = datetime.strptime(date_unique, "%d/%m/%Y")
                    return date_unique
                except ValueError:
                    super().affichage_erreur_date()

        # Saisie de début et de fin de tournoi
        elif entree_date == 'p':     
            plage_date = []   
            while True:
                date_debut = input("Entrez la date de début au format jj/mm/aaaa : ")
                try:
                    date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
                    plage_date.append(date_debut)
                    break
                except ValueError:
                    super().affichage_erreur_date()

            while True:
                date_fin = input("Entrez la date de fin au format jj/mm/aaaa : ")
                try:
                    date_fin = datetime.strptime(date_fin, "%d/%m/%Y")
                    plage_date.append(date_fin)
                    break
                except ValueError:
                    super().affichage_erreur_date()

            return plage_date


    def demander_rounds(self):
        
        """ 
        La méthode isdigit() est une méthode de l'objet str (chaîne de caractères) en Python. 
        Elle permet de vérifier si tous les caractères d'une chaîne sont des chiffres. 
        Elle renvoie True si tous les caractères sont des chiffres, et False sinon.
        """
        
        rounds = input("Combien de rounds souhaitez-vous jouer ? (4 par défaut) ")

        # Si l'utilisateur n'a pas saisi de nombre, utilise 4 rounds par défaut
        if not rounds.isdigit():
            rounds = 4
        else:
            # Convertit la chaîne de caractères en entier
            rounds = int(rounds)

        print(f"Vous avez choisi de jouer {rounds} rounds.")
        return rounds


    def demander_description(self):        
        description = input("Entrez la description : ")
        return description


    def demander_mode_de_jeu(self):
        
        mode_de_jeu = ["bullet", "blitz", "fast"]

        for i, mode in enumerate(mode_de_jeu):
            print(f"{i + 1} - {mode}")

        try:
            entree = int(input('Sélectionnez le mode de jeu par le chiffre correspondant : '))
            if entree < 1 or entree > 3:
                raise ValueError
        except ValueError:
            super().affichage_erreur_numero()
            return self.demander_mode_de_jeu()

        return mode_de_jeu[entree - 1]
    
    def infos_tournoi(self):
        """ Afficher les informations du tournoi dans un dictionnaire """
        
        self.nom = self.demander_nom_tournoi()
        self.lieu = self.demander_lieu_tournoi()
        self.dates = self.demander_dates_tournoi()  
        self.nombres_de_rounds = self.demander_rounds()
        self.description = self.demander_description()
        self.mode_de_jeu = self.demander_mode_de_jeu()
        
        tournoi = Tournoi(self.nom,
                            self.lieu,
                            self.dates,             
                            self.nombres_de_rounds,
                            self.description,
                            self.mode_de_jeu)  
        self.tournoi_cree = tournoi.afficher_tournoi()
        return self.tournoi_cree
        










        
        
        


