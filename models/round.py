from datetime import datetime


class Round:
    def __init__(self, nombres_de_rounds):
        self.nombres_de_rounds = nombres_de_rounds

    def periode_round(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        temps = f"Date et heure du Round : {date}"
        print(temps)
