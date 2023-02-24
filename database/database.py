import json

class Database:
    
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
    
    
    def mettre_a_jour_classement_historique_tournoi(self):
    
        with open("data/historique_tournois.json", "r+") as f:
            tournois = json.load(f)
            self.tournoi_en_cours = tournois["liste_des_tournois_en_cours"][-1]
            joueurs = self.tournoi_en_cours["joueurs"]

        """ 
        fonction lambda est utilisée pour définir une fonction 
        qui prend en paramètre un élément de la liste joueurs et 
        qui renvoie la valeur de la clé "score" de cet élément. 
        Cette fonction est utilisée en tant que key pour le tri de la liste joueurs.
        """
        # Trier la liste des joueurs par score décroissant
        joueurs.sort(key=lambda x: x["score"], reverse=True)

        # Mettre à jour le classement de chaque joueur
        for i, joueur in enumerate(joueurs):
            joueur["classement"] = i + 1

        # Enregistrer les modifications dans le fichier JSON
        with open("data/historique_tournois.json", "w") as f:
            json.dump(tournois, f, indent=4)
            
            
            
    def mettre_a_jour_classement_score_liste_joueurs(self):
        
        with open("data/historique_tournois.json", "r") as f:
            historique_tournois = json.load(f)
        with open("data/liste_joueurs.json", "r") as f:
            liste_joueurs = json.load(f)

        for tournoi in historique_tournois["liste_des_tournois_en_cours"]:
            for joueur_tournoi in tournoi["joueurs"]:
                for joueur_liste in liste_joueurs["liste_joueurs"]:
                    if joueur_tournoi["nom"] == joueur_liste["nom"] and joueur_tournoi["prenom"] == joueur_liste["prenom"]:
                        joueur_liste["classement"] = joueur_tournoi["classement"]
                        # joueur_liste["score"] = joueur_tournoi["score"]

        with open("data/liste_joueurs.json", "w") as f:
            json.dump(liste_joueurs, f, indent=4)  
