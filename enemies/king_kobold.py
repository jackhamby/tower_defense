from .enemy import Enemy

class KingKobold(Enemy):


    def __init__(self, rround):
        Enemy.__init__(self, rround)

        # Attributes
        self.width = 40
        self.height = 40
        self.max_speed = 1
        self.speed = self.max_speed
        self.is_alive = False
        self.attack = 2
        self.max_hp = 800
        self.hp = self.max_hp
        self.bounty = 4