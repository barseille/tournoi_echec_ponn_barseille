import json

class Database:
    

    
    # def ecrire_database(self, infos, cle, chemin_fichier):
    #     """
    #     Cette méthode prend :
    #     - en 1er argument les données à sauvergarder (infos), 
    #     - en 2ème argument la clé du dictionnaire du fichier json où ajouter les données, 
    #     - et en 3ème argument, le chemin du fichier JSON où enregistrer les données.
        
    #     Elle ouvre le fichier en mode écriture ('w'), 
    #     écrit le dictionnaire avec la nouvelle valeur associée à la clé 'cle'
    #     en utilisant la fonction json.dump. Enfin, elle retourne les données.
    #     """
    #     with open(chemin_fichier, 'r+') as f:
    #         donnees = json.load(f)
    #         donnees[cle] = infos
    #         f.seek(0)
    #         json.dump(donnees, f, indent=2)
    #         return donnees

    
    def ecrire_database(self, infos, cle, chemin_fichier):
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
        with open(chemin_fichier, 'r+') as f:
            donnees = json.load(f)
            donnees[cle].append(infos)
            f.seek(0)
            json.dump(donnees, f, indent=2)
            return donnees
        


    def lire_database(self, chemin_fichier):
        """
        Lit un fichier JSON à partir d'un chemin de fichier donné 
        en entrée et renvoie les données sous forme de dictionnaire
        """
        
        with open(chemin_fichier, "r") as f:
            data = json.load(f)
        return data   
    
    
