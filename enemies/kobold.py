from .enemy import Enemy
from settings import kobold_width, kobold_height, kobold_icon
import pygame

class Kobold(Enemy):


    def __init__(self, map_):

        Enemy.__init__(self, map_, kobold_width, kobold_height, kobold_icon)

        # Attributes
        self.max_speed = 3
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 50
        self.hp = self.max_hp
        self.bounty = 1
