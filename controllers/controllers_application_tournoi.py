import json

class ControllersApplicationTournoi:

    def recuperation_tournois_existant(self):
        
        with open("tournois_inacheves.json", "r") as f:
            data = json.load(f)
            i = 1
            for i, tournoi in enumerate(data["tournois_inacheves"]):
                print(f'{i + 1}. Nom du tournoi: {tournoi["nom_tournoi"]} - Dates: {tournoi["dates"]}')
                i += 1

        while True:
                
            numero_tournoi = int(input("Quel tournoi souhaitez-vous continuer (numéro index)?"))
            
            tournoi_selectionne = data["tournois_inacheves"][numero_tournoi-1]
            
            print('-'*60)
            print("        -- Informations du tournoi --")
            print('-'*60)   
            print(f'Nom du tournoi : {tournoi_selectionne["nom_tournoi"]}')
            print(f'Lieu : {tournoi_selectionne["lieu"]}')
            print(f'Dates : {tournoi_selectionne["dates"]}')
            print(f'Description : {tournoi_selectionne["description"]}')
            print(f'Mode de jeu : {tournoi_selectionne["mode_de_jeu"]}')     
            print('-'*60)
            print("            -- Joueurs --")
            print('-'*60)
            for joueur in tournoi_selectionne["joueurs"]:
                print(f'{joueur["prenom"]} {joueur["nom"]}')
                
            dernier_round_index = len(tournoi_selectionne["liste_de_rounds"]) - 1
            print(f"Dernier Round effectué : {dernier_round_index} Round")
            
            continuer_tournoi = input("Souhaitez-vous continuer ce tournoi (o/n)?")
            if continuer_tournoi == "o":
                # code pour continuer le tournoi
                break
            elif continuer_tournoi == "n":
                # code pour retourner à l'accueil
                break
            else:
                print("Veuillez entrer 'oui' ou 'non'")
            break
            
          