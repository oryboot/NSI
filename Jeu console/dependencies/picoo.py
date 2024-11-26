import time


class Picoo:
    """Définition d'un cochon"""

    def __init__(self, picoo):
        """
        on prend en paramètres une liste de "types" de cochons
        """
        self.nom = picoo
        if self.nom == 'Minion':  # si à§a tombe sur Minion
            # on définit ses stats
            self.PV = 100
            self.attaque = 30
            self.defense = 10
            self.vitesse = 60
        elif self.nom == 'Corporal':  # pareil pour corporal
            self.PV = 100
            self.attaque = 35
            self.defense = 15
            self.vitesse = 65
        elif self.nom == 'Fat':  # pareil pour fat
            self.PV = 150
            self.attaque = 40
            self.defense = 5
            self.vitesse = 45
        elif self.nom == 'King Picoo':  # et pour King Picoo
            self.PV = 500
            self.PVmax = 500
            self.defense = 0
            self.vitesse = 50
            self.attaque = 40

    def attaquer(self, ennemi):
        """
        on définit une méthode qui permet au cochon/picoo d'attaquer le bird.
        """
        time.sleep(1)
        if self.attaque < ennemi.defense:  # si la défense de l'ennemi du cochon (càd du bird) est supérieure
            ennemi.PV -= 0  # on inflige aucun dégàt
            print(f'{self.nom} attaque {ennemi.nom}: {self.nom} ne vous fait aucun dégât.')
        else:
            ennemi.PV -= self.attaque - ennemi.defense  # sinon on inflige des dégà¢ts
            if ennemi.PV < 0:  # si les PV du bird sont inférieurs à 0
                ennemi.PV = 0  # on les passe à  0
                print(f'{ennemi.nom} est K.O.')
            print(f'{self.nom} attaque {ennemi.nom}: {self.nom} vous fait {self.attaque - ennemi.defense} dégâts.')


def combat(perso, ennemi):
    """
    Fonction combat qui permet de lancer un combat entre deux adversaires donnés en paramètres (perso et ennemi). Elle retourne True si le perso est gagnant, False sinon
    """
    global ennemi_tour
    ennemi_tour = True
    perso.tour == True
    while perso.PV > 0 and ennemi.PV > 0:  # tant que les deux ont encore des PV le combat se poursuit
        if perso.vitesse > ennemi.vitesse:  # si le perso est plus rapide que l'ennemi
            if perso.tour == True:
                if perso.nom == 'Bomb':
                    perso.attaquer([ennemi])  # le perso attaque en premier
                else:
                    perso.attaquer(ennemi)
            if ennemi.PV > 0 and ennemi_tour == True:  # et si l'ennemi a encore des PV
                ennemi.attaquer(perso)  # il attaque
            else:
                ennemi_tour = True
        else:  # si à l'inverse, c'est l'ennemi qui est plus rapide
            if ennemi_tour == True:
                ennemi.attaquer(perso)  # il attaque le perso
            if perso.PV > 0 and perso.tour == True:  # qui s'il a encore des PV
                if perso.nom == 'Bomb':
                    perso.attaquer([ennemi])  # attaque l'ennemi
                else:
                    perso.attaquer(ennemi)
        if perso.nom == 'Chuck':#si le bird est Chuck
            if perso.backlash >= 1:#s'il a encore un effet de contrecoup
                perso.backlash -= 1#on lui diminue de 1 tour
                perso.defense -= 5#et on diminue sa défense de 5
        if perso.nom == 'Red':#s'il s'agit de Red
            if perso.backlash > 0:#s'il est épuisé
                perso.backlash -= 1#on le 'réanime'
                print('Red se sent mieux.')
            elif perso.backlash == 0:
                perso.tour = True
    return perso.PV > 0  # si le joueur a encore des PV on retourne True, False sinon
