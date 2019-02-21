from .enemy import Enemy
import pygame

icon = pygame.transform.scale( pygame.image.load("images/kobold.png"), (20, 20))


class Kobold(Enemy):


    def __init__(self, rround):
        Enemy.__init__(self, rround)

        # Attributes
        self.width = 20
        self.height = 20
        self.max_speed = 3
        self.speed = self.max_speed
        self.is_alive = False
        self.attack = 2
        self.max_hp = 50
        self.hp = self.max_hp
        self.bounty = 1
        self.icon = icon