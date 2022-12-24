from .controllers_tournois import ControllersTournois
import json



class ControllersApplication :

    def selectionner_tournoi(self):

        print('-'*50)
        print("          -- Tous les Tournois -- ")
        print('-'*50)
        
        
        afficher_les_tournois = ControllersTournois()

        liste_des_tournois = afficher_les_tournois.deserialiser()

        print(liste_des_tournois)

    
    def afficher_tous_joueurs_du_tournoi(self):
        pass
    
    def choisir_joueur_tournoi(self):
        pass
    
    def afficher_details_tournoi(self):
        pass
    
    def lancer_round(self):
        pass
    
        def generer_premier_round(self):
            pass
        
        def generer_rounds_suivant(self):
            pass
    
    def afficher_les_matchs(self):
        pass
    
    def afficher_resultats_match(self):
        pass
    
    def afficher_resultat_round(self):
        pass
    
    def resultat_tournoi(self):
        pass
    
        def afficher_par_classement(self):
            pass
    
    def sauvegarde_tournoi_en_cours(self):
        pass
    
    
    
    
    
    
    
        
        