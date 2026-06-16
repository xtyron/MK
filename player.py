from entity import Entity

class Player(Entity):
    def __init__(self, name : str, max_hp : int, damage : int):
        super().__init__(name, max_hp, damage)
        self.movement_speed = 3
        
        