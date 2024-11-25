import time


class Bird:
    '''Définition d'un Bird'''

    def __init__(self, nom):
        self.tour = True
        if nom == 'red':  # s'il choisit red
            # on initialise les stats du perso
            self.nom = 'Red'
            self.PV = 100
            self.PVmax = 100
            self.backlash = 0
            self.XP = 0
            self.attaque = 85
            self.defense = 20
            self.niveau = 0
            self.vitesse = 75
            self.stamina = 40
            self.staminamax = 40
            self.att_spe = ['Rage', 150]
        elif nom == 'chuck':  # de même pour chuck
            self.nom = 'Chuck'
            self.backlash = 0
            self.PV = 50
            self.PVmax = 50
            self.XP = 0
            self.attaque = 70
            self.defense = 15
            self.niveau = 0
            self.vitesse = 100
            self.stamina = 50
            self.staminamax = 50
            self.att_spe = ['Hyperactive', 0]
        elif nom == 'bomb':  # et pour bomb
            self.nom = 'Bomb'
            self.PV = 120
            self.PVmax = 120
            self.XP = 0
            self.attaque = 100
            self.defense = 25
            self.niveau = 0
            self.vitesse = 40
            self.stamina = 30
            self.staminamax = 30
            self.att_spe = ['Kamikaze', 50]

    def attaquer(self, ennemi, indice=0):
        '''
        On crée une méthode qui prend un ennemi en paramètre et permet au Bird d'attaquer l'ennemi avec l'attaque de son choix.
        '''
        global ennemi_tour
        ennemi_tour = True # cette variable renvoie True si c'est le tour de l'ennemi
        attaque_valide = False  # on initialise une variable qui permettra de vérifier que le Bird peut attaquer
        print('')
        time.sleep(1)
        while not attaque_valide:
            if self.nom == 'Bomb':
                print(
                    f'{self.nom} | Stamina: {self.stamina}, PV: {self.PV}/{self.PVmax}\n{ennemi[indice].nom} | PV: {ennemi[indice].PV}')  # on rappelle les PV de chacun
            else:
                print(
                    f'{self.nom} | Stamina: {self.stamina}, PV: {self.PV}/{self.PVmax}\n{ennemi.nom} | PV: {ennemi.PV}')  # on rappelle les PV de chacun
            attaque = input(
                f'Quelle attaque souhaitez-vous lancer ? 1: Normal, 2: {self.att_spe[0]}')  # on demande au joueur quelle attaque il souhaite lancer
            if attaque == '1':  # si le joueur choisit de lancer une attaque normale
                if self.nom == 'Bomb':
                    if self.attaque < ennemi[
                        indice].defense:  # si la défense de l'ennemi est supérieure à  l'attaque du joueur
                        ennemi[indice].PV -= 0  # le joueur ne lui fait aucun dégàt
                        print(f'{self.nom} attaque {ennemi[indice].nom}: Vous ne faites aucun dégât.')  # On le précise
                    else:
                        ennemi[indice].PV -= self.attaque - ennemi[indice].defense  # on inflige des dégà¢ts à  l'ennemi qui correspondent à  la différence entre sa défense et l'attaque du joueur
                        if ennemi[indice].PV < 0:  # si les PV de l'ennemi passe en dessous de 0
                            ennemi[indice].PV = 0  # on les passe à 0
                        print(
                            f'{self.nom} attaque {ennemi[indice].nom}: Vous faites {self.attaque - ennemi[indice].defense} dégâts.')  # On précise les dégà¢ts infligés
                else:
                    if self.attaque < ennemi.defense:  # si la défense de l'ennemi est supérieure à  l'attaque du joueur
                        ennemi.PV -= 0  # le joueur ne lui fait aucun dégàt
                        print(f'{self.nom} attaque {ennemi.nom}: Vous ne faites aucun dégât.')  # On le précise
                    else:
                        ennemi.PV -= self.attaque - ennemi.defense  # on inflige des dégàts à l'ennemi qui correspondent à  la différence entre sa défense et l'attaque du joueur
                        if ennemi.PV < 0:  # si les PV de l'ennemi passe en dessous de 0
                            ennemi.PV = 0  # on les passe à  0
                        print(
                            f'{self.nom} attaque {ennemi.nom}: Vous faites {self.attaque - ennemi.defense} dégâts.')  # On précise les dégà¢ts infligés
                attaque_valide = True  # on valide l'attaque

            elif attaque == '2':  # s'il choisit son attaque spéciale
                if self.stamina >= 20:  # on vérifie qu'il a assez de stamina
                    if self.nom == 'Chuck':
                        print('Vous utilisez Hyperactive : +20 DEF')
                        self.defense += 20
                        ennemi_tour = False
                        self.backlash = 4
                    elif self.nom == 'Red':
                        print('Vous utilisez Rage')
                        if self.att_spe[1] < ennemi.defense:  # si la défense de l'ennemi est supérieure à  l'attaque du bird
                            ennemi.PV -= 0  # le joueur ne fait aucun dégà¢t
                            print(f'{self.nom} attaque {ennemi.nom}: Vous ne faites aucun dégât.')
                        else:
                            ennemi.PV -= self.att_spe[1] - ennemi.defense  # sinon on inflige des dégà¢ts à  l'ennemi
                            if ennemi.PV < 0:  # si ses PV sont inférieurs à  0
                                ennemi.PV = 0  # on les passe à  0
                            print(f'{self.nom} attaque {ennemi.nom}: Vous faites {self.att_spe[1] - ennemi.defense} dégâts.')
                        print('Red est épuisé')
                        self.tour = False
                        self.backlash = 1
                        attaque_valide = True  # on valide l'attaque
                    else:
                        print('Vous utilisez Kamikaze.')
                        for enn in ennemi:
                            if self.att_spe[
                                1] < enn.defense:  # si la défense de l'ennemi est supérieure à  l'attaque du bird
                                enn.PV -= 0  # le joueur ne fait aucun dégât
                                print(f'{enn.nom} ne se prend aucun dégât.')
                            else:
                                enn.PV -= self.att_spe[1] - enn.defense  # sinon on inflige des dégâts à l'ennemi
                                if enn.PV < 0:  # si ses PV sont inférieurs à 0
                                    enn.PV = 0  # on les passe à 0
                                print(f'{enn.nom} se prend {self.att_spe[1] - enn.defense} dégâts.')
                        print('Vous prenez 50 dégâts de contrecoup')
                        self.PV -= 50
                        attaque_valide = True  # on valide l'attaque
                    self.stamina -= 20  # on diminue la stamina du joueur
                else:
                    print(
                        'Pas assez de stamina !')  # si le joueur n'a pas assez de stamina pour lancer son attaque spéciale, on ne valide pas l'attaque

            else:
                print('Valeur invalide !')  # de même s'il rentre autre chose que '1' ou '2'

    def gain_xp(self, nbXP):
        """
        On crée une méthode prenant en paramètre un nombre d'XP (int) qui sera ajouté à ceux du joueur.
        """
        self.XP += nbXP  # on augmente les XP du bird
        if self.XP > 100:  # si ses XP dépassent 100
            self.XP = 0  # on repasse ses XP à 0
            self.niveau += 1  # on augmente son niveau
            # on augmente toutes ses stats de 5
            self.PV += 5
            self.PVmax += 5
            self.attaque += 5
            self.defense += 5
            self.vitesse += 5
            self.stamina += 5
            self.staminamax += 5
            self.att_spe[1] += 5
