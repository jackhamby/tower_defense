from .projectile import Projectile
from effects import Slow
import math


class SlimeBall(Projectile):

    def __init__(self, map_, x, y, target_x, target_y, damage):
        Projectile.__init__(self, map_, x, y, target_x, target_y, damage)
        self.color = (0, 0, 0)
        self.slow_amount = 2
        self.effects = [Slow(self.map, self.target_x, self.target_y, self.slow_amount)]