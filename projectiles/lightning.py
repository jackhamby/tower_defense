from .projectile import Projectile


class Lightning(Projectile):

    def __init__(self, map_, x, y, target_x, target_y, damage):
        Projectile.__init__(self, map_, x, y, target_x, target_y, damage)

        self.color = (0, 0, 255)