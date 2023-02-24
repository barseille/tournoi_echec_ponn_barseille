import json

class BaseViews:
    
    def afficher_msg(self, msg):   
        print(msg)
  
    def presentation(self, affichage):       
            print('-'*60)        
            print(affichage)
            print('-'*60)
            
    def affichage_erreur_texte(self):
        print("Erreur ! Veuillez saisir des lettres alphabétiques")
        
        
    def affichage_erreur_choix(self):     
        print('Erreur! Veuillez saisir "o" pour oui ou "n" pour quitter')
   
    
    def  affichage_erreur_type(self):
        print("Erreur ! Veuillez entrer un nombre entier valide")
   
        
    def affichage_erreur_numero(self):
        print("Erreur ! Veuillez saisir le numéro correspondant")
        
    def affichage_erreur_date(self):
        print("La date entrée n'est pas valide, veuillez la saisir au format jj/mm/aaaa.")
        
        
    def affichage_termine(self):     
        print('****************** Terminé ********************')
    
        
    def retour_au_menu(self):   
        input("Appuyez sur ENTREE pour revenir au menu")
    
        

    def ecrire_json(self, infos, cle, fichier):
        """
        Cette méthode prend :
        - en 1er argument les données à sauvergarder (infos), 
        - en 2ème argument la clé du dictionnaire du fichier json où ajouter les données, 
        - et en 3ème argument, le chemin du fichier JSON où enregistrer les données.
        
        Elle ouvre le fichier en mode lecture/écriture ('r+'), 
        charge les données dans un dictionnaire (donnees), 
        ajoute la liste 'infos' à la 'cle' de 'donnees', 
        puis réécrit le fichier avec les données mises à jour en utilisant
        la fonction json.dump. Enfin, elle retourne les données.
        """
        with open(fichier, 'r+') as f:
            donnees = json.load(f)
            donnees[cle].append(infos)
            f.seek(0)
            json.dump(donnees, f, indent=4)
            return donnees
        


    def lire_fichier_json(self, chemin_fichier):
        """
        Lit un fichier JSON à partir d'un chemin de fichier donné 
        en entrée et renvoie les données sous forme de dictionnaire
        """
        
        with open(chemin_fichier, "r") as f:
            data = json.load(f)
        return data



            
        
    
        
        