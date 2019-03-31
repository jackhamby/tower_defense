from .enemy import Enemy
from settings import knight_width, knight_height, knight_icon
import pygame

class Knight(Enemy):


    def __init__(self, map_):

        Enemy.__init__(self, map_, knight_width, knight_height, knight_icon)

        # Attributes
        self.max_speed = 4
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 100
        self.hp = self.max_hp
        self.bounty = 1
