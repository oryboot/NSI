class Item:
    def __init__(self, name, description, type, weight, unique_id):
        self.name = name
        self.description = description
        self.type = type
        self.weight = weight
        self.unique_id = unique_id

    def afficher(self):
        print(f'Name: {self.name}')
        print(f'Description: {self.description}')
        print(f'Type: {self.type}')
        print(f'Weight: {self.weight}')
        print(f'ID: {self.unique_id}')


class Potion(Item):
    def __init__(self, name, description, unique_id, healing=0, damaging=0,
                 stamina_reload=False):
        super().__init__(name, description, 'potion', unique_id)
        self.healing = healing
        self.damaging = damaging
        self.stamina_reload = stamina_reload

    def use(self,bird,picoo):
        bird.PV+=self.healing
        picoo.PV-=self.damaging
        bird.stamina+=self.stamina_reload


class Weapon(Item):
    def __init__(self, name, description, weight, unique_id, damage=0, reload=0):
        super().__init__(name, description, 'weapon', weight, unique_id)
        self.damage = damage
        self.reload = reload

    def attack(self):
        pass

class Tool(Item):
    def __init__(self, name, description, weight, unique_id, efficiency=0, reload=0, durability=0):
        super().__init__(name, description, 'tool', weight, unique_id)
        self.efficiency = efficiency
        self.reload = reload
        self.durability = durability

    def use(self):
        if self.durability > 0 and self.reload > 0:
            print(f"You're using {self.name} which is {self.efficiency}% efficient.")
            self.durability -= 1
        elif self.durability > 0:
            print('You need to reload!')
        else:
            print(f'{self.name} is broken!')

