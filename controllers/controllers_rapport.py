from views.views_rapport_menu import ViewsRapportMenu
import json

class ControllersRapport:
    
    def affichage_joueur(self):
        
        print('-'*70)
        print('         -- Classement des joueurs par ordre alphabetique --')
        print('-'*70)
        
        with open("liste_joueurs.json", "r") as f:
            joueurs_data = json.load(f)
        
        liste_joueurs = joueurs_data['liste_joueurs']
        liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        
        i = 1   
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Classement {joueur['classement']}")
            
    
    
    def affichage_tournoi(self):
        
        print('-'*70)
        print('                 -- Liste de tous les tournois --')
        print('-'*70)
        
        with open("liste_tournois.json", "r") as f:
            liste_tournois_data = json.load(f)
            
        self.liste_tournois = liste_tournois_data["liste_tournois"]
        
        i = 1
        for i, tournoi in enumerate(self.liste_tournois):
            nom = tournoi["nom"]
           
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi {nom} - date(s) : {dates}")
            
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))
        tournoi_selectionne = self.liste_tournois[choix_tournoi - 1]
        
        print('-'*60)
        print('               -- Détails du tournoi --')
        print('-'*60)
        print(f'Nom du tournoi : {tournoi_selectionne["nom"]}')
        print(f'Lieu : {tournoi_selectionne["lieu"]}')
        print(f'Dates(s) : {tournoi_selectionne["dates"]}')
        print(f'Nombres de rounds : {tournoi_selectionne["nombres_de_rounds"]}')
        print(f'Mode de jeu : {tournoi_selectionne["mode_de_jeu"]}')
            
  
    
    def afficher_details_tournoi(self):
        
        print('-'*70)
        print('                 -- Liste des tournois terminés --')
        print('-'*70)
        
        with open("historique_tournois.json", "r") as f:
            tournoi = json.load(f)
        
        tournoi_termine = tournoi['liste_des_tournois_en_cours']
        
        i = 1
        for i, tournoi in enumerate(tournoi_termine):
            nom = tournoi["nom"]
            dates = tournoi["dates"]
            print(f"{i+1} - Nom du tournoi {nom} - date(s) : {dates}")
        
 
        choix_tournoi = int(input("Choisissez un tournoi pour plus de détails : "))

        tournoi_selectionne = tournoi_termine[choix_tournoi - 1]
        
        print('-'*60)
        print('               -- Détails du tournoi terminé --')
        print('-'*60)
        print(f'Nom du tournoi : {tournoi_selectionne["nom"]}')
        print(f'Lieu : {tournoi_selectionne["lieu"]}')
        print(f'Dates(s) : {tournoi_selectionne["dates"]}')
        print(f'Nombres de rounds : {tournoi_selectionne["nombres_de_rounds"]}')
        print(f'Mode de jeu : {tournoi_selectionne["mode_de_jeu"]}')
        
        
        liste_joueurs = tournoi_selectionne['joueurs']
        liste_joueurs.sort(key=lambda joueur: joueur['nom'])
        
        i = 1   
        for i, joueur in enumerate(liste_joueurs):
            print(f"Joueur {i+1} : {joueur['prenom']} {joueur['nom']} - Classement {joueur['classement']}")
         
         
         
        # for round in tournoi_selectionne['liste_de_rounds']:
        #     print(round)
        
        for round in tournoi_selectionne['liste_de_rounds']:
            numero_round = round['numero_round']
            date_debut = round['date_debut']
            date_fin = round['date_fin']
            matchs = round['matchs']
            points = round['points']

            print("Numéro de round : ", numero_round)
            print("Date de début : ", date_debut)
            print("Date de fin : ", date_fin)
            print("Matchs : ", matchs)
            print("Points : ", points)
            

            
   
        
      
        


            


        # for round in tournoi_selectionne["liste_de_rounds"]:
        #     print(f"Round : {round['numero_round']}")
        #     print(f"Début du round : {round['date_debut']}")
        #     print(f"Fin du round : {round['date_fin']}")
        #     print("Matchs :")
        #     for match in round['matchs']:
        #         print(f"{match['joueur1']} vs {match['joueur2']} : {match['score']}")
        #     print("Points :")
        #     for joueur, score in round['points']:
        #         print(f"{joueur} : {score}")
        #     print("\n")
        
        # for index, round_info in enumerate(tournoi_selectionne['liste_de_rounds']):
        #     print(f"Round {index}: {round_info['numero_round']}")


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # print(f"Round : {round['numero_round']}")
            # print('Du', round['date_debut'], 'au', round['date_fin'])
            # print('Matchs:')
            
            # for match in round['matchs']:
            #     print(match['joueur1'], 'vs', match['joueur2'], match['joueur1']['score'], '-', match['joueur2']['score'])
        
        # for joueur in tournoi_selectionne["joueurs"]:
        #     print(f'{joueur["prenom"]} {joueur["nom"]} : date de naissance : {joueur["date_de_naissance"]} / genre : {joueur["genre"]}')
            
        
        # with open("historique_tournois.json", "r") as f:
        #     historique_tournois_data = json.load(f) 
            
        # tournois_en_cours = historique_tournois_data["liste_des_tournois_en_cours"]
        
        # # On vérifie s'il y a plusieurs tournois du même nom et qu'ils sont terminés
        # tournois_meme_nom = []
        # for tournoi in tournois_en_cours:
        #     if tournoi["nom"] == nom_tournoi:
        #         tournois_meme_nom.append(tournoi)
   
        # # on filtre pour récupérer les tournois ayant un id unique        
        # ids = []
        # for i, tournoi in enumerate(tournois_meme_nom):
        #     if tournoi['id'] not in ids :
        #         ids.append(tournoi['id'])
        #         print(f"{i+1} - {tournoi['nom']} | {tournoi['dates']}")
        # choix = int(input("Plusieurs tournois ont le même nom. Choisissez le tournoi que vous souhaitez sélectionner : "))
        # tournoi_fini = tournois_meme_nom[choix-1]
                
        # # # On récupère le tournoi terminé
        # # tournois_meme_id = []
        # # if len(tournois_meme_nom) > 1:
            
        # #     for tournoi in tournois_meme_nom:
        # #         if len(tournoi["id"]) > 1 :
        # #             tournois_meme_id.append(tournoi)
        # #     tournoi_fini = tournois_meme_id[-1]
                                
        # nom_tournoi = tournoi_fini["nom"]
        # date_tournoi = tournoi_fini["dates"]
        
        # print('-'*70)
        # print('                 -- Informations du tournoi --')
        # print('-'*70)
        # print(f"Nom du tournoi : {nom_tournoi} | Date(s) : {date_tournoi}")
        
        # print("Liste des joueurs :")
        # for joueur in tournoi_fini["joueurs"]:
        #     print(f" - {joueur['nom']} {joueur['prenom']}")
            
                
        # for round in tournoi_fini["liste_de_rounds"]:
        #     for cle, valeur in round.items():
        #         print('-'*50)
        #         print(f"               -- {cle} --")
        #         print('-'*50)
        #         for match in valeur["liste_de_matchs"]:
        #             joueur1 = match[0]
        #             score = match[1]
        #             print(f"{joueur1} : {score}")
                    
  




    
    