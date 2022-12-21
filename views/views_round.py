from datetime import datetime


def entree_round():
    number = input("Veuillez saisir le numéro du round :")
    return number


def entree_date_round():
    date = datetime.today()
    return date.strftime("%d/%m/%y")


def entree_debut_round():
    start_time = datetime.now()
    return start_time.strftime("%H:%M:%S")


def entree_fin_round():
    end_time = datetime.now()
    return end_time.strftime("%H:%M:%S")