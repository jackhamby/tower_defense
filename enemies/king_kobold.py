from .enemy import Enemy
import pygame
from settings import king_kobold_width, king_kobold_height, king_kobold_icon


# icon = pygame.transform.scale( pygame.image.load("images/kobold_king.png"), (40, 40))


class KingKobold(Enemy):


    def __init__(self, map_):
        Enemy.__init__(self, map_, king_kobold_width, king_kobold_height, king_kobold_icon)

        # Attributes
        self.max_speed = 1
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 800
        self.hp = self.max_hp
        self.bounty = 4
