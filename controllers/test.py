# Définit les classes propres à notre forum. ;)

class Fichier:
    """Fichier."""

    def __init__(self, nom, taille):
        """Initialise le nom et la taille."""
        self.nom = nom
        self.taille = taille

    def afficher(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.nom}'.")


class FichierImage(Fichier):
    """Fichier image.
    Pas plus à ajouter pour l'instant !
    """

    pass


class Utilisateur:
    """Utilisateur."""

    def __init__(self, nom_utilisateur, mot_de_passe):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    def se_connecter(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.nom_utilisateur} est connecté.")

    def poster(self, fil, contenu, fichier=None):
        """Poste un message dans un fil de discussion."""
        if fichier:
            post = PostAvecFichier(self, "aujourd'hui", contenu, fichier)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=contenu)
        fil.ajouter_post(post)
        return post

    def creer_fil(self, titre, contenu):
        """Crée un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", contenu)
        return FilDiscussion(titre, "aujourd'hui", post)

    def __str__(self):
        """Représentation de l'utilisateur."""
        return self.nom_utilisateur


class Moderateur(Utilisateur):
    """Utilisateur modérateur."""

    def modifier(self, post, contenu):
        """Modifie un message."""
        post.contenu = contenu

    def supprimer(self, fil, post):
        """Supprime un message."""
        index = fil.posts.index(post)
        del fil.posts[index]


class Post:
    """Message."""

    def __init__(self, utilisateur, temps_poste, contenu):
        """Initialise l'utilisateur, la date et le contenu."""
        self.utilisateur = utilisateur
        self.temps_poste = temps_poste
        self.contenu = contenu

    def afficher(self):
        """Affiche le message."""
        print(f"Message posté par {self.utilisateur} le {self.temps_poste}:")
        print(self.contenu)


class PostAvecFichier(Post):
    """Message comportant un fichier."""

    def __init__(self, utilisateur, temps_poste, contenu, fichier):
        """Initialise le fichier."""
        self.utilisateur = utilisateur
        self.temps_poste = temps_poste
        self.contenu = contenu
        self.fichier = fichier

    def afficher(self):
        """Affiche le contenu et le fichier."""
        super().afficher()
        print("Pièce jointe:")
        self.fichier.afficher()


class FilDiscussion:
    """Fil de discussions."""

    def __init__(self, titre, temps_poste, post):
        """Initialise le titre, la date et les posts.
        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourront s'ajouter qu'ultérieurement.
        En effet, on ne crée pas directement un nouveau fil avec des réponses. ;)
        """
        self.titre = titre
        self.temps_poste = temps_poste
        self.posts = [post]

    def continuer(self, post):
        """Ajoute un post au fil de discussion."""
        self.posts.append(post)

    def afficher(self):
        """Affiche le fil de discussion."""
        print("----- FIL DE DISCUSSION -----")
        print(f"Titre: {self.titre}, Date: {self.temps_poste}")
        print()
        for post in self.posts:
            post.afficher()
            print()
        print("------------------")
        
class Fichier:
    
    """Fichier."""
    def __init__(self, nom, taille):
        """Initialise le nom et la taille."""
        self.nom = nom
        self.taille = taille

    def afficher(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.nom}'.")

class FichierImage(Fichier):
    """Fichier image.
    Pas plus à ajouter pour l'instant !
    """
    pass

class Utilisateur:
    """Utilisateur."""
    def __init__(self, nom_utilisateur, mot_de_passe):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    def se_connecter(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.nom_utilisateur} est connecté.")

    def poster(self, fil_discussion, contenu, fichier=None):
        """Poste un message dans un fil de discussion."""
        if fichier:
            post = PostFichier(self, "aujourd'hui", contenu, fichier)
        else:
            post = Post(self, "aujourd'hui", contenu)
        fil_discussion.ajouter(post)
        return post

    def creer_fil(self, titre, contenu):
        """Crée un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", contenu)
        return FilDiscussion(titre, "aujourd'hui", post)

    def __str__(self):
        """Représentation de l'utilisateur."""
        return self.nom_utilisateur
    
class Modérateur(Utilisateur):
    """Utilisateur modérateur."""
    
    def modifier(self, post, contenu):
        """Modifie un message."""
        post.contenu = contenu

    def supprimer(self, fil_discussion, post):
        """Supprime un message."""
        index = fil_discussion.posts.index(post)
        del fil_discussion.posts[index]


class Post:
    """Message."""
    def __init__(self, utilisateur, temps_poste, contenu):
        """Initialise l'utilisateur, la date et le contenu."""
        self.utilisateur = utilisateur
        self.temps_poste = temps_poste
        self.contenu = contenu

    def afficher(self):
        """Affiche le message."""
        print(f"Message posté par {self.utilisateur} le {self.temps_poste}:")
        print(self.contenu)

class PostFichier(Post):
    """Message comportant un fichier."""
    def __init__(self, utilisateur, temps_poste, contenu, fichier):
        """Initialise le fichier."""
        self.utilisateur = utilisateur
        self.temps_poste = temps_poste
        self.contenu = contenu
        self.fichier = fichier

    def afficher(self):
        """Affiche le contenu et le fichier."""
        super().afficher()
        print("Pièce jointe:")
        self.fichier.afficher()









































# """Ici, nous allons serrer des vis et taper sur des clous!"""


# class BoiteAOutils:
#     """Boite à outils."""

#     def __init__(self):
#         """Initialise les outils."""
#         self.trousse_a_outils = []

#     def ajouter_outil(self, outil):
#         """Ajoute un outil."""
#         self.trousse_a_outils.append(outil)

#     def enlever_outil(self, outil):
#         """Enleve un outil."""
#         index = self.trousse_a_outils.index(outil)
#         del self.trousse_a_outils[index]


# class Tournevis:
#     """Tournevis."""

#     def __init__(self, taille=3):
#         """Initialise la taille."""
#         self.taille = taille

#     def serrer(self, vis):
#         """Serrer une vis."""
#         vis.serrer()

#     def desserer(self, vis):
#         """Desserre une vis."""
#         vis.desserer()

#     def __repr__(self):
#         """Représentation de l'objet."""
#         return f"Tournevis de taille {self.taille}"


# class Marteau:
#     """Marteau."""

#     def __init__(self, color="red"):
#         """Initialise la couleur."""
#         self.color = color

#     def paint(self, color):
#         """Paint le marteau."""
#         self.color = color

#     def marteau_enfonce(self, clou):
#         """Enfonce un clou."""
#         clou.enfoncer()

#     def remove(self, clou):
#         """Enleve un clou."""
#         clou.remove()

#     def __repr__(self):
#         """Représentation de l'objet."""
#         return f"Marteau de couleur {self.color}"


# class Vis:
#     """Vis."""

#     MAX_NIVEAU_SERRAGE = 5

#     def __init__(self):
#         """Initialise son degré de serrage."""
#         self.niveau_serrage = 0

#     def desserer(self):
#         """Déserre le vis."""
#         if self.niveau_serrage > 0:
#             self.niveau_serrage -= 1

#     def serrer(self):
#         """Serre le vis."""
#         if self.niveau_serrage < self.MAX_NIVEAU_SERRAGE:
#             self.niveau_serrage += 1

#     def __str__(self):
#         """Retourne une forme lisible de l'objet."""
#         return "Vis avec un serrage de {}".format(self.niveau_serrage)


# class Clou:
#     """Clou."""

#     def __init__(self):
#         """Initialise son statut "dans le mur"."""
#         self.dans_le_mur = False

#     def enfoncer(self):
#         """Enfonce le clou dans un mur."""
#         if not self.dans_le_mur:
#             self.dans_le_mur = True

#     def remove(self):
#         """Enlève le clou du mur."""
#         if self.dans_le_mur:
#             self.dans_le_mur = False

#     def __str__(self):
#         """Retourne une forme lisible de l'objet."""
#         etat_du_mur = "dans le mur" if self.dans_le_mur else "hors du mur"
#         return f"Clou {etat_du_mur}."


# # Instanciez une boîte à outils, un tournevis, et un marteau.
# marteau = Marteau()
# tournevis = Tournevis()
# boite_a_outils = BoiteAOutils()

# # Placez le marteau et le tournevis dans la boîte à outils.
# boite_a_outils.ajouter_outil(marteau)
# boite_a_outils.ajouter_outil(tournevis)

# # Instanciez une vis, et serrez-la avec le tournevis.
# # Affichez la vis avant après avoir été serrée.
# vis = Vis()
# print(vis)
# tournevis.serrer(vis)
# print(vis)

# # Instanciez un clou, puis enfoncez-le avec le marteau.
# # Affichez le clou avant et après avoir été enfoncé.
# clou = Clou()
# print(clou)
# marteau.marteau_enfonce(clou)
# print(clou)


# # --------------------------------------------------------------
# # Que pouvez-vous faire d’autre avec ces classes et ces objets ?

# # enlever un outil
# print("outils dans la boîte:", boite_a_outils.trousse_a_outils)
# boite_a_outils.enlever_outil(marteau)
# print("on a enlevé le marteau")
# print("outils dans la boîte:", boite_a_outils.trousse_a_outils)

# # désserrer la vis
# tournevis.desserer(vis)
# print(vis)

# # enlever le clou
# marteau.remove(clou)
# print(clou)

# # repeindre le marteau
# marteau.paint("yellow")
# print(Marteau)