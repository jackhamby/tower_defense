from .projectile import Projectile
from effects import Dot
import math


class Fire(Projectile):

    def __init__(self, map_, x, y, target_x, target_y, damage):
        Projectile.__init__(self, map_, x, y, target_x, target_y, damage)
        self.color = (0, 0, 0)
        self.dot = math.ceil(self.damage/2)
        self.effects = [Dot(self.map, self.target_x, self.target_x, self.dot)]