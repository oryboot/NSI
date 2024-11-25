from .utils import sort_speed, verif_int
from .bird import Bird
from .picoo import Picoo


def combat(perso, ennemi):
    """
    Fonction combat qui permet de lancer un combat entre deux adversaires donnés en paramètres (perso et ennemi). Elle retourne True si le perso est gagnant, False sinon
    """
    global ennemi_tour
    ennemi_tour = True
    perso.tour == True
    while perso.PV > 0 and ennemi.PV > 0:  # tant que les deux ont encore des PV, le combat se poursuit
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
        else:  # si à  l'inverse c'est l'ennemi qui est plus rapide
            if ennemi_tour == True:
                ennemi.attaquer(perso)  # il attaque le perso
            if perso.PV > 0 and perso.tour == True:  # qui s'il a encore des PV
                if perso.nom == 'Bomb':
                    perso.attaquer([ennemi])  # attaque l'ennemi
                else:
                    perso.attaquer(ennemi)
        if perso.nom == 'Chuck':
            if perso.backlash >= 1:
                perso.backlash -= 1
                perso.defense -= 5
        if perso.nom == 'Red':
            if perso.backlash > 0:
                perso.backlash -= 1
                print('Red se sent mieux.')
            elif perso.backlash == 0:
                perso.tour = True
    return perso.PV > 0  # si le joueur a encore des PV on retourne True, False sinon


def combat_multiple(perso, enemies):
    """
    Fonction qui permet de déclencher un combat avec plusieurs ennemis en tour par tour
    """
    global ennemi_tour
    ennemi_tour = True
    perso.tour = True
    while any([p.PV > 0 for p in enemies]) and perso.PV > 0:  # tant l'un au moins des picoos est encore en vie
        opponents = sort_speed(
            enemies + [perso])  # liste de tous les opposants du combat (càd bird+picoos) triés par vitesse
        if perso.tour == True:
            print('Choisis un ennemi à attaquer:')  # on demande au joueur de choisir un ennemi à attaquer
            for i in range(len(enemies)):
                print(f'{str(i + 1)}:{enemies[i].nom}- PV:{enemies[i].PV}')
            verif = False
            while not verif:
                i_ennemi = input()
                if verif_int(i_ennemi):
                    i_ennemi = int(i_ennemi)
                    verif = i_ennemi - 1 in range(len(enemies))
                else:
                    print('Entrée invalide')
            ennemi = enemies[i_ennemi - 1]  # ennemi que le joueur a choisi d'attaquer
        for opp in opponents:  # pour chaque opposants (bird compris)
            if type(opp) == Bird and opp.PV > 0 and opp.tour == True:  # si l'opposant est le bird
                print(f'{perso.nom} attaque {ennemi.nom}:')  # on le fait attaquer l'ennemi qu'il a choisi
                if perso.nom == 'Bomb':
                    opp.attaquer(enemies, i_ennemi)
                elif perso.nom in ['Chuck', 'Red']:
                    if perso.tour == True:
                        opp.attaquer(ennemi)
                if ennemi.PV <= 0:
                    print(f'{ennemi.nom} est K.O.')
                    print('')
                    enemies.pop(i_ennemi - 1)  # si le joueur bat l'ennemi, on le retire de la liste des ennemis

            elif type(opp) == Picoo and opp.PV > 0 and ennemi_tour == True:  # si l'opposant est un Picoo
                opp.attaquer(perso)  # il attaque le joueur
            elif ennemi_tour == False:
                ennemi_tour = True
        print('')
        if perso.PV > 0:
            for pic in enemies:
                print(f'PV {pic.nom}:{pic.PV}')  # on affiche les PV de chaque ennemi
            print(f'PV {perso.nom}: {perso.PV}')
            print('')
            if perso.nom == 'Chuck':
                if perso.backlash >= 1:
                    print('- 5 DEF')
                    perso.backlash -= 1
                    perso.defense -= 5
            elif perso.nom == 'Red':
                if perso.backlash > 0:
                    perso.backlash -= 1
                    print('Red se sent mieux')
                elif perso.backlash == 0:
                    perso.tour = True
    return perso.PV > 0
