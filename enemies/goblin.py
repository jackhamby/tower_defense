from .enemy import Enemy
from settings import goblin_width, goblin_height, goblin_icon
import pygame

class Goblin(Enemy):


    def __init__(self, map_):

        Enemy.__init__(self, map_, goblin_width, goblin_height, goblin_icon)

        # Attributes
        self.max_speed = 8
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 100
        self.hp = self.max_hp
        self.bounty = 1
