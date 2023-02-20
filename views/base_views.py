import json

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
    
        
    def retour_au_menu(self):   
        input("Appuyez sur ENTREE pour revenir au menu")
    
        

    def ecrire_json(self, infos, cle, fichier='data/fichier.json'):
        """
        Cette méthode prend en premier argument un dictionnaire (infos), en second argument la clé du dictionnaire
        où ajouter les données, et en troisième argument (optionnel) le nom du fichier JSON où enregistrer les données.
        Elle ouvre le fichier en mode lecture/écriture ('r+'), charge les données dans un dictionnaire (donnees), ajoute
        la liste 'infos' à la clé 'cle' de 'donnees', puis réécrit le fichier avec les données mises à jour en utilisant
        la fonction json.dump. Enfin, elle retourne les données.
        """
        with open(fichier, 'r+') as f:
            donnees = json.load(f)
            donnees[cle].append(infos)
            f.seek(0)
            json.dump(donnees, f, indent=4)
            return donnees


            
        
    
        
        