class Entity:
    def __init__(self, name : str, max_hp : int, damage : int):
        self.name = name
        self.max_hp = max_hp
        self.damage = damage
        self.level = 1
        self.x = 0
        self.y = 0

    def die(self):
        self.max_hp = 0
