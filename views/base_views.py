class BaseViews:
    
    def afficher_msg(self, msg):   
        print(msg)

        
    def presentation(self, affichage):
        
            print('-'*60)
            print(affichage)
            print('-'*60)
        
        
    def affichage_erreur(self):     
        print('Erreur! Veuillez saisir "o" pour oui ou "n" pour quitter.')
    
    def  affichage_erreur_type(self):
        print("Erreur ! Veuillez entrer un nombre entier valide")
        
    def affichage_erreur_numero(self):
        print("Erreur ! Veuillez saisir le numéro correspondant")
        
    def affichage_tournoi_termine(self):     
        print('                *** Tournoi terminé ***')
            
        
    
        
        