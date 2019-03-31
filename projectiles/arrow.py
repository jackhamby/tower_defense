from .projectile import Projectile


class Arrow(Projectile):

    def __init__(self, map_, x, y, target_x, target_y, damage):
        Projectile.__init__(self, map_, x, y, target_x, target_y, damage)

        self.color = (255, 0, 255)