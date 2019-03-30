from .projectile import Projectile


class Arrow(Projectile):

    def __init__(self, x, y, target_x, target_y):
        Projectile.__init__(self, x, y, target_x, target_y)

        self.color = (255, 0, 255)