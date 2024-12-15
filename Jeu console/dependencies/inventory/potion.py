class Potion:
    """Création d'une potion"""
    def __init__(self, name, unique_id, stamina=False, healing=0, damaging=0):
        self.name = name
        self.unique_id = unique_id
        self.healing = healing
        self.damaging = damaging
        self.stamina=stamina
    def use(self,bird,picoo):
        """
        Méthode qui permet d'utiliser la potion. Elle prend en paramètre le joueur(bird) et l'ennemi (picoo).
        """
        bird.PV+=self.healing
        picoo.PV-=self.damaging-picoo.defense
        if self.stamina :
            bird.stamina+=bird.staminamax-bird.stamina
        print(f'PV : +{self.healing}\nDégâts à {picoo.nom} : {self.damaging-picoo.defense}\nStamina : +{bird.staminamax-bird.stamina}')