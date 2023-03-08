import datetime


class Joueur:
    def __init__(self, nom, prenom, date_de_naissance, classement, id):
        self.nom = nom
        self.prenom = prenom
        self._date_de_naissance = date_de_naissance
        self.classement = classement
        self._id = id
        self.opposants = []
        self.score = 0

    def afficher_infos(self):
        joueur_infos = {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self._date_de_naissance,
            "classement": self.classement,
            "score": self.score,
            "id": self._id,
        }
        return joueur_infos

    def nom_complet(self):
        return f"Joueur {self.prenom} {self.nom}"

    @property
    def date_de_naissance(self):
        return self._date_de_naissance

    # value : 23/05/1994
    @date_de_naissance.setter
    def date_de_naissance(self, value):
        try:
            datetime.datetime.strptime(value, "%d/%m/%Y")
            self._date_de_naissance = value

        except ValueError:
            raise ValueError("date de naissance doit être un str (jj/mm/aaaa)")

    @property
    def id(self):
        return self._id

    # value : AB00001
    @id.setter
    def id(self, value):
        if isinstance(value, str) and value.isdigit() and len(value) == 5:
            self._id = "AB" + value
        else:
            raise ValueError("id doit être un str de 5 chiffres")
