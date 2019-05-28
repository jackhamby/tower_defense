

from .projectile import Projectile
from effects import Boost
import math


class BoostWave(Projectile):

    def __init__(self, map_, x, y, attribute, amount, source_tower):
        Projectile.__init__(self, map_, x, y, None, None, None)
        self.color = (0, 0, 0)
        self.attribute = attribute
        self.amount = amount
        self.source_tower = source_tower
        self.effects = [Boost(self.map, self.x, self.y, self.amount, self.attribute, self.source_tower)]
