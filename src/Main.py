import csv
from collections import defaultdict

class Noeud:
    def __init__(self, prix, joueur):
        self.prix = prix
        self.joueurs = [joueur]
        self.gauche = None
        self.droite = None