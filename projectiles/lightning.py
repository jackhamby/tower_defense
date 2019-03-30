from .projectile import Projectile


class Lightning(Projectile):

    def __init__(self, x, y, target_x, target_y):
        Projectile.__init__(self, x, y, target_x, target_y)

        self.color = (0, 0, 255)