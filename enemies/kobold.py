from .enemy import Enemy

class Kobold(Enemy):


    def __init__(self, rround):
        Enemy.__init__(self, rround)

        # Attributes
        self.width = 20
        self.height = 20
        self.max_speed = 3
        self.speed = self.max_speed
        self.is_alive = False
        self.max_hp = 50
        self.hp = self.max_hp