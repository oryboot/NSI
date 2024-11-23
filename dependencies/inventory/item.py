class Item:
    def __init__(self, name, description, type, weight, unique_id):
        self.name = name
        self.description = description
        self.type = type
        self.weight = weight
        self.unique_id = unique_id


class Potion(Item):
    def __init__(self, name, description, weight, unique_id, healing=0, damaging=0, blurry_view=False, invisibility=False, speeding=False,
                 stamina_reload=False):
        super().__init__(name, description, 'potion', weight, unique_id)
        self.healing = healing
        self.damaging = damaging
        self.blurry_view = blurry_view
        self.invisibility = invisibility
        self.speeding = speeding
        self.stamina_reload = stamina_reload

    def use(self):
        pass


class Weapon(Item):
    def __init__(self, name, description, weight, unique_id, damage=0, reload=0):
        super().__init__(name, description, 'weapon', weight, unique_id)
        self.damage = damage
        self.reload = reload

    def attack(self):
        pass

class Tool(Item):
# tool object
