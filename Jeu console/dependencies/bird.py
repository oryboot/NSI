import time


# def attack():
#     if choose_spe_attack():
#         spe_attack()
#     else:
#         basic_attack()


class Bird:
    '''Définition d'un Bird'''

    def __init__(self, nom, PV, PVmax, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe):
        self.tour = True
        self.nom = nom
        self.PV = PV
        self.PVmax = PVmax
        self.XP = XP
        self.attaque = attaque
        self.defense = defense
        self.niveau = niveau
        self.vitesse = vitesse
        self.stamina = stamina
        self.staminamax = staminamax
        self.att_spe = att_spe

    def show_stats(self, opponent):
        print(f'{self.nom} | Stamina: {self.stamina}, PV: {self.PV}/{self.PVmax}\n{opponent.nom} | PV: {opponent.PV}')  # on rappelle les PV de chacun


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
                self.show_stats(ennemi[indice])                
            else:
                self.show_stats(ennemi)

            type_attaque = input(f'Quelle attaque souhaitez-vous lancer ? 1: Normal, 2: {self.att_spe[0]}')  # on demande au joueur quelle attaque il souhaite lancer
            
            if type_attaque == '1':  # si le joueur choisit de lancer une attaque normale
                if self.nom == 'Bomb':
                    if ennemi[indice].defense > self.attaque:  # si la défense de l'ennemi est supérieure à  l'attaque du joueur
                        ennemi[indice].PV -= 0  # le joueur ne lui fait aucun dégàt
                        print(f'{self.nom} attaque {ennemi[indice].nom}: Vous ne faites aucun dégât.')  # On le précise
                    else:
                        ennemi[indice].PV -= self.attaque - ennemi[indice].defense  # on inflige des dégà¢ts à  l'ennemi qui correspondent à  la différence entre sa défense et l'attaque du joueur
                        if ennemi[indice].PV < 0:  # si les PV de l'ennemi passe en dessous de 0
                            ennemi[indice].PV = 0  # on les passe à 0
                        print(f'{self.nom} attaque {ennemi[indice].nom}: Vous faites {self.attaque - ennemi[indice].defense} dégâts.')  # On précise les dégà¢ts infligés
                else:
                    if ennemi.defense > self.attaque:  # si la défense de l'ennemi est supérieure à  l'attaque du joueur
                        ennemi.PV -= 0  # le joueur ne lui fait aucun dégàt
                        print(f'{self.nom} attaque {ennemi.nom}: Vous ne faites aucun dégât.')  # On le précise
                    else:
                        ennemi.PV -= self.attaque - ennemi.defense  # on inflige des dégàts à l'ennemi qui correspondent à  la différence entre sa défense et l'attaque du joueur
                        if ennemi.PV < 0:  # si les PV de l'ennemi passe en dessous de 0
                            ennemi.PV = 0  # on les passe à  0
                        print(f'{self.nom} attaque {ennemi.nom}: Vous faites {self.attaque - ennemi.defense} dégâts.')  # On précise les dégà¢ts infligés
                attaque_valide = True  # on valide l'attaque

            else:  # s'il choisit son attaque spéciale
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
                            if self.att_spe[1] < enn.defense:  # si la défense de l'ennemi est supérieure à  l'attaque du bird
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
                    print('Pas assez de stamina !')  # si le joueur n'a pas assez de stamina pour lancer son attaque spéciale, on ne valide pas l'attaque

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


class Red(Bird):
    def __init__(self, PV, PVmax, backlash, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe):
        super().__init__('Red', PV, PVmax, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe)
        self.backlash = backlash


class Chuck(Bird):
    def __init__(self, PV, PVmax, backlash, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe):
        super().__init__('Chuck', PV, PVmax, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe)
        self.backlash = backlash


class Bomb(Bird):
    def __init__(self, PV, PVmax, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe):
        super().__init__('Bomb', PV, PVmax, XP, attaque, defense, niveau, vitesse, stamina, staminamax, att_spe)


birds_data = {
    'Red': {
        'PV': 100,
        'PVmax': 100,
        'backlash': 0,
        'XP': 0,
        'attaque': 85,
        'defense': 20,
        'niveau': 0,
        'vitesse': 75,
        'stamina': 40,
        'staminamax': 40,
        'att_spe': ['Rage', 150],
    },
    'Chuck': {
        'PV': 50,
        'PVmax': 50,
        'backlash': 0,
        'XP': 0,
        'attaque': 70,
        'defense': 15,
        'niveau': 0,
        'vitesse': 100,
        'stamina': 50,
        'staminamax': 50,
        'att_spe': ['Hyperactive', 0],
    },
    'Bomb': {
        'PV': 120,
        'PVmax': 120,
        'XP': 0,
        'attaque': 100,
        'defense': 25,
        'niveau': 0,
        'vitesse': 40,
        'stamina': 30,
        'staminamax': 30,
        'att_spe': ['Kamikaze', 50],
    },
}
