from views.views_entree_joueur import ViewsEntreeJoueur
from views.views_menu_joueur import ViewsMenuJoueur
from models.joueur import Joueur
from views.base_views import BaseViews

class ControllersJoueurs:
    
    def recuperer_infos_joueur(self):
        """ Récupère les entrées utilisateur pour créer un nouveau joueur """

        # Affiche le menu de création de joueur
        creer_joueur = ViewsMenuJoueur()
        creer_joueur.affichage_creation_joueur()

 
        v = ViewsEntreeJoueur()
        self.nom = v.creation_joueur_nom()
        self.prenom = v.creation_joueur_prenom()
        self.date_de_naissance = v.creation_joueur_date_de_naissance()
        self.classement = v.creation_joueur_classement()
        self.id_joueur = v.ajout_identifiant()
        
        self.afficher_infos_joueur()
            
    def afficher_infos_joueur(self):
        """ Afficher les informations joueurs """
        
        joueur = Joueur(self.nom,
                        self.prenom,
                        self.date_de_naissance,
                        self.classement,
                        self.id_joueur)

        self.joueur_infos = joueur.afficher_infos()
        
        # sauvegarder les informations du joueur(données, clé, chemin)
        self.sauvergarde()
        self.demande_autre_joueur()
        
        # return self.joueur_infos
 
    def demande_autre_joueur(self):
            while True:
                choix = input("Souhaitez vous créer un autre joueur ? (o/n) : ")
                if choix == "o":
                    self.joueur_infos = self.recuperer_infos_joueur()
                
                elif choix == "n":
                    titre = "Joueur créé avec succès !"
                    affiche = BaseViews()
                    affiche.afficher_msg(titre)
                    return
                else:
                    msg_erreur = BaseViews()
                    msg_erreur.affichage_erreur()
                    
    def sauvergarde(self):
        base_views = BaseViews()
        base_views.ecrire_json(self.joueur_infos, "liste_joueurs", fichier='data/liste_joueurs.json')
        

        

    
            

     
 
 
 
 
 
 
 
 
 
 
 
 
        

        
        


        
           
            
            
        
        
        
        
        
        
            
                
    

    
    
    
    
    
   
   

        
    






