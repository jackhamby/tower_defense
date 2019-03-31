from .projectile import Projectile
from effects import Explosion
import math


class Bomb(Projectile):

    def __init__(self, map_, x, y, target_x, target_y, damage):
        Projectile.__init__(self, map_, x, y, target_x, target_y, damage)
        self.color = (0, 0, 0)
        self.explosion_radius = 80
        self.effects = [Explosion(self.map, self.target_x, self.target_y, self.damage, self.explosion_radius)]