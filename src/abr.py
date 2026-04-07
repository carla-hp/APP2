""" Création de la structure des noeuds de l'ABR """
class Noeud:
    def __init__(self, prix, joueur):
        """ on créer une liste pour mettre plusieurs joueurs sur le meme prix """
        self.joueurs = [joueur]
        self.gauche = None
        self.droite = None

""" on créé la classe de l'ABR """
class ABR:
    def __init__(self):
        self.racine = None

    def inserer(self, prix, joueur):
        if self.racoine is None:
            self.racine = Noeud(prix, joueur)
        else:
            self._inserer_recursif(self.racine, prix, joueur)

    def _inserer_recursif(self, noeud_actuel,  prix, joueur):
        if prix == noeud_actuel.prix:
            """ cas 1 : le prix existe deja donc on ajoute le joueur a la liste """
            noeud_actuel.joueurs.append(joueur)
        
        elif prix < noeud_actuel.prix:
            """ cas 2 : le prix est plus petit donc on l'insere a gauche """
            if noeud_actuel.gauche is None:
                noeud_actuel.gauche = Noeud(prix, joueur)
            else:
                self._inserer_recursif(noeud_actuel.gauche, prix, joueur)
        
        else:
            """" cas 3 : le prix est plus grand donc droite """
            if noeud_actuel.droite is None:
                noeud_actuel.droite = Noeud(prix , joueur)
            else:
                self._inserer_recursif(noeud_actuel.droite, prix, joueur)