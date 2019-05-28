from .enemy import Enemy
from effects import Spawn
from settings import wagon_width, wagon_height, wagon_icon
import pygame

class Wagon(Enemy):


    def __init__(self, map_):

        Enemy.__init__(self, map_, wagon_width, wagon_height, wagon_icon)

        # Attributes
        self.max_speed = 3
        self.speed = self.max_speed
        self.is_alive = False
        self.damage = 2
        self.max_hp = 5000
        self.hp = self.max_hp
        self.bounty = 1

        self.effects = [Spawn(self.map, self.x, self.y)]




